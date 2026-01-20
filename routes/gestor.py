from flask import Blueprint, render_template, session, redirect, url_for, request
from Database.models.hospedes import Hospedes
from Database.models.quartos import Quartos
from utils import validar_gestor
import datetime

rota_gestor = Blueprint('gestor', __name__)


@rota_gestor.route('/painel', methods=['GET'])
def painel():
    #abre o painel(tela/menu) gestor e verifica o usuario

    check = validar_gestor()
    if check:
        return check
    
    return render_template('gestor/painel.html')

@rota_gestor.route('/hospedes/new', methods=['GET'])
def formulario_hospede():
    #abre o fumulario dos hospedes

    check = validar_gestor()
    if check:
        return check
    
    quartos = Quartos.select()
    return render_template('gestor/criarhospede.html', quartos=quartos)

@rota_gestor.route('/hospedes/new', methods=['POST'])
def novo_hospede():
    
    #cria um novo hospede de acordo com o formulário preenchido
    check = validar_gestor()
    if check:
        return check 
    
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

    return redirect(url_for('gestor.painel'))

@rota_gestor.route('/quartos/<int:id_quarto>/hospedes', methods=['GET'])
def ver_hospedes_quarto(id_quarto):
    #mostra o hospede, que esta no quarto que foi selecionado
    check = validar_gestor()
    if check:
        return check

    quarto = Quartos.get_or_none(Quartos.id_quarto == id_quarto)
    if not quarto:
        return "Quarto não encontrado", 404
    print(session)
    hospedes = list(quarto.hospedes)

    return render_template('gestor/hospede_quarto.html', quarto=quarto,hospedes=hospedes )

@rota_gestor.route('/quartos', methods=['GET'])
def ver_quartos():
    #mostra todos o quartos cadastrados
    check = validar_gestor()
    if check:
        return check
    
    quartos = list(Quartos.select().dicts())
    return render_template('gestor/verquarto.html', quartos=quartos)

@rota_gestor.route('/quartos/new', methods=['GET', 'POST'])
def novo_quarto():
    #cria um novo quarto

    check = validar_gestor()
    if check:
        return check
    
    if request.method == 'POST':
        Quartos.create(
        num_quarto=request.form['numquarto'],
        andar=request.form['andar'],
        )
        return redirect(url_for('gestor.painel'))

    return render_template('gestor/criarquarto.html')

@rota_gestor.route('/hospede/<int:id>/editar', methods=['GET', 'POST'])
def editar_hospede(id):
        #edita algum hospede selecionado
    check = validar_gestor()
    if check:
        return check

    hospede = Hospedes.get_or_none(Hospedes.id_hospede == id)
    if not hospede:
        return 'Hóspede não encontrado', 404
    
    if request.method == 'POST':
        hospede.nome = request.form['nome']
        hospede.data_nascimento = request.form['data_nascimento']
        hospede.sexo = request.form['sexo']
        hospede.responsavel_nome = request.form['responsavel_nome']
        hospede.responsavel_telefone = request.form['responsavel_telefone']
        hospede.condicoes_medicas = request.form.get('condicoes_medicas', '')
        hospede.alergias = request.form.get('alergias', '')
        hospede.observacoes = request.form.get('observacoes', '')
        hospede.atualizado_em = datetime.datetime.now()
        nome = session.get("nome")
        cargo = session.get("cargo")
        id = session.get('usuario_id')
        hospede.atualizado_por = f"#ID: {id} | cargo: {cargo} |  nome: {nome}" 
        
        hospede.save()

        return redirect(url_for('gestor.ver_hospedes_quarto', id_quarto=hospede.id_quarto.id_quarto))

    return render_template('gestor/editarhospede.html', hospede=hospede)


@rota_gestor.route('/hospede/<int:id>/excluir', methods=['POST'])
def excluir_hospede(id):
    check = validar_gestor()
    if check:
        return check
    
    hospede = Hospedes.get_or_none(Hospedes.id_hospede == id)
    if not hospede:
        return 'Hóspede não encontrado', 404

    id_quarto = hospede.id_quarto.id_quarto
    hospede.delete_instance()

    return redirect(url_for('gestor.ver_hospedes_quarto', id_quarto=id_quarto))