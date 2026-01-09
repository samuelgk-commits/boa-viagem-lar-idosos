from flask import Blueprint, render_template, request
from Database.models.hospedes import Hospedes
from Database.database import db

rota_hospedes = Blueprint('hospedes', __name__)

@rota_hospedes.route('/')
def lista_hospedes():

    hospedess = Hospedes.select()
    return render_template('lista_hospedes.html', hospedes = hospedess)

@rota_hospedes.route('/', methods=['POST'])
def inserir_hospede():

    data = request.json

    novo_usuario = Hospedes.create(
    nome = data['nome'],
    email = data['email'],
    )
    return render_template('item_hospede.html', hospede=novo_usuario)


@rota_hospedes.route('/new')
def formulario():
    return render_template('formulario_hospedes.html')

@rota_hospedes.route('/<int:hospede_id>')
def vizualizar_hospede(hospede_id):

    hospede = Hospedes.get_by_id(hospede_id)
    print(hospede)
    return render_template('verhospede.html', hospede = hospede)

@rota_hospedes.route('/<int:hospede_id>/edit', methods=['PUT']) 
def editar_hospedes(hospede_id):

    hospede = Hospedes.get_by_id(hospede_id)
    print(hospede)
    return render_template('formulario_hospedes.html', hospede = hospede)

@rota_hospedes.route('/<int:hospede_id>/delete', methods=['DELETE'])
def deletar_hospedes(hospede_id):
   
    hospede = Hospedes.delete_by_id(hospede_id)
    hospede.delete_instance()

    return {'id': hospede_id}