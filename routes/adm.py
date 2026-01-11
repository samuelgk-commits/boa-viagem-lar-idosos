from flask import Blueprint, render_template, session, redirect, url_for, request
from Database.models.hospedes import Hospedes
from Database.models.quartos import Quartos
from Database.models.cuidadores import Cuidadores
from Database.models.gestor import Gestor
from Database.models.adm import Adm
import datetime

rota_adm = Blueprint('adm', __name__)

def validar_ususario():
    #validação basica para evitar que pessoas sem acesso ao cargo de adm/gestor/cuidador, tenham acesso aos seus respectivos privilegios 
    if session.get("cargo") != "adm":
        return redirect(url_for('home.login'))

@rota_adm.route('/painel', methods=['GET'])
def painel():
    #abre o painel(tela/menu) adm e verifica o ususario

    validar_ususario()
    return render_template('adm/painel.html')


@rota_adm.route('/hospedes/new', methods=['GET'])
def formulario_hospede():
    #abre o fumulario dos hospedes

    validar_ususario()
    quartos = Quartos.select()
    return render_template('adm/criarhospede.html', quartos=quartos)



@rota_adm.route('/hospedes/new', methods=['POST'])
def novo_hospede():
    
    #cria um novo hospede de acordo com o formulário preenchido
    validar_ususario() 
    quarto_selecionado = Quartos.get_or_none(Quartos.id_quarto == request.form['id_quarto'])

    Hospedes.create(
        nome=request.form['nome'],
        data_nascimento=request.form['data_nascimento'],
        sexo=request.form['sexo'],
        data_entrada=request.form['data_entrada'],
        responsavel_nome=request.form['responsavel_nome'],
        responsavel_telefone=request.form['responsavel_telefone'],
        condicoes_medicas=request.form.get('condicoes_medicas', ''),
        alergias=request.form.get('alergias', ''),
        observacoes=request.form.get('observacoes', ''),
        id_quarto=quarto_selecionado,
        criado_em=datetime.datetime.now(),
        atualizado_em=datetime.datetime.now()
    )

    return redirect(url_for('adm.painel'))

@rota_adm.route('/quartos/new', methods=['GET', 'POST'])
def novo_quarto():
    #cria um novo quarto

    validar_ususario()
    if request.method == 'POST':
        Quartos.create(
        num_quarto=request.form['numquarto'],
        andar=request.form['andar'],
        )
        return redirect(url_for('adm.painel'))

    return render_template('adm/criarquarto.html')

@rota_adm.route('/cuidador/new', methods=['GET', 'POST'])
def novo_cuidador():
    #cria um cuidador 
    validar_ususario()
    if request.method == 'POST':
        Cuidadores.create(
        nome=request.form['nome'],
        telefone=request.form['telefone'],
        senha=request.form['senha'],
        turno=request.form['turno'],
        data_contratacao=request.form['data_contratacao'],

        )
        return redirect(url_for('adm.painel'))

    return render_template('adm/criarcuidador.html')

@rota_adm.route('/gestor/new', methods=['GET', 'POST'])
def novo_gestor():
    #cria um gestor
    validar_ususario()
    if request.method == 'POST':
        Gestor.create(
        nome=request.form['nome'],
        email=request.form['email'],
        senha=request.form['senha'],
        )
        return redirect(url_for('adm.painel'))

    return render_template('adm/criargestor.html')

@rota_adm.route('/colaboradores', methods=['GET'])
def ver_colaboradores():
    #cria uma lista com todos os usuarios do sistema, permitindo edita-los. ou excluí-los 
    validar_ususario()
    administradores = list(Adm.select().dicts())
    cuidadores = list(Cuidadores.select().dicts())
    gestores = list(Gestor.select().dicts())

    colaboradores = []

    for adm in administradores:
        colaboradores.append({
            'id': adm['id_adm'],
            'nome': adm['nome'],
            'cargo': 'adm',
            'email': adm.get('email', ''),
            'telefone': '',
            'turno': '',
            'data_contratacao': adm.get('criado_em')
        })

    for c in cuidadores:
        colaboradores.append({
            'id': c['id_cuidador'],
            'nome': c['nome'],
            'cargo': 'cuidador',
            'email': '',
            'telefone': c['telefone'],
            'turno': c['turno'],
            'data_contratacao': c['data_contratacao']
        })

    for g in gestores:
        colaboradores.append({
            'id': g['id_gestor'],
            'nome': g['nome'],
            'cargo': 'gestor',
            'email': g['email'],
            'telefone': '',
            'turno': '',
            'data_contratacao': g.get('criado_em')
        })
    return render_template('adm/vercolaborador.html',colaboradores=colaboradores)

@rota_adm.route('/colaborador/<cargo>/<int:id>/editar', methods=['GET', 'POST'])
def editar_colaborador(cargo, id):
    #função que edita todos os usuarios
    validar_ususario()
    cargo = cargo.lower()

    if cargo == "adm":
        model = Adm
        id_campo = Adm.id_adm
    elif cargo == "cuidador":
        model = Cuidadores
        id_campo = Cuidadores.id_cuidador
    elif cargo == "gestor":
        model = Gestor
        id_campo = Gestor.id_gestor
    else:
        return "Cargo inválido", 404

    colaborador = model.get_or_none(id_campo == id)

    if not colaborador:
        return "Colaborador não encontrado", 404

    if request.method == 'POST':
        colaborador.nome = request.form['nome']

        if hasattr(colaborador, 'email'):
            colaborador.email = request.form.get('email', colaborador.email)

        if hasattr(colaborador, 'telefone'):
            colaborador.telefone = request.form.get('telefone', colaborador.telefone)

        if hasattr(colaborador, 'turno'):
            colaborador.turno = request.form.get('turno', colaborador.turno)

        colaborador.atualizado_em = datetime.datetime.now()
        colaborador.save()

        return redirect(url_for('adm.ver_colaboradores'))

    return render_template(
        'adm/editar_colaborador.html',
        colaborador=colaborador,
        cargo=cargo,
        colaborador_id=id
    )

@rota_adm.route('/colaborador/<cargo>/<int:id>/excluir', methods=['POST'])
def excluir_colaborador(cargo, id):
    #pode excluir todos os usuarios
    validar_ususario()
    if cargo == "adm":
        model = Adm
        id_campo = Adm.id_adm
    elif cargo == "cuidador":
        model = Cuidadores
        id_campo = Cuidadores.id_cuidador
    elif cargo == "gestor":
        model = Gestor
        id_campo = Gestor.id_gestor
    else:
        return "Cargo inválido", 404

    colaborador = model.get_or_none(id_campo == id)

    if not colaborador:
        return "Colaborador não encontrado", 404

    model.delete().where(id_campo == id).execute()
    return redirect(url_for('adm.ver_colaboradores'))


@rota_adm.route('/quartos', methods=['GET'])
def ver_quartos():
    #mostra todos o quartos cadastrados

    validar_ususario()
    quartos = list(Quartos.select().dicts())
    return render_template('adm/verquarto.html', quartos=quartos)

@rota_adm.route('/quartos/<int:id_quarto>/hospedes', methods=['GET'])
def ver_hospedes_quarto(id_quarto):
    #mostra o hospede, que esta no quarto que foi selecionado
    validar_ususario()

    quarto = Quartos.get_or_none(Quartos.id_quarto == id_quarto)
    if not quarto:
        return "Quarto não encontrado", 404

    hospedes = list(quarto.hospedes)
    return render_template('adm/hospede_quarto.html', quarto=quarto, hospedes=hospedes)
