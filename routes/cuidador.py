from flask import Blueprint, render_template, session, redirect, url_for
from utils import validar_cuidador
from Database.models.quartos import Quartos

rota_cuidador = Blueprint('cuidador', __name__)

@rota_cuidador.route('/painel', methods=['GET'])
def painel():
    #abre o painel(tela/menu) cuidador e verifica o usuario

    check = validar_cuidador()
    if check:
        return check
    
    return render_template('cuidador/painel.html')


@rota_cuidador.route('/quartos', methods=['GET'])
def ver_quartos():
    #mostra todos o quartos cadastrados
    check = validar_cuidador()
    if check:
        return check
    
    quartos = list(Quartos.select().dicts())
    return render_template('cuidador/verquarto.html', quartos=quartos)

@rota_cuidador.route('/quartos/<int:id_quarto>/hospedes', methods=['GET'])
def ver_hospedes_quarto(id_quarto):
    #mostra o hospede, que esta no quarto que foi selecionado
    check = validar_cuidador()
    if check:
        return check

    quarto = Quartos.get_or_none(Quartos.id_quarto == id_quarto)
    if not quarto:
        return "Quarto não encontrado", 404
    print(session)
    hospedes = list(quarto.hospedes)

    return render_template('cuidador/hospede_quarto.html', quarto=quarto,hospedes=hospedes )


