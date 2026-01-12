from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from Database.models.gestor import Gestor
from Database.models.adm import Adm
from Database.models.cuidadores import Cuidadores

rota_home = Blueprint('home', __name__)

@rota_home.route('/', methods=['GET', 'POST'])
def login():
    #essa função tem como objetivo pegar as informações do formulário e validar os dados de acordo com o banco, como cargo, nome e senha, e retornar um feedback caso haja erro ou as informações estejam incorretas  

        if request.method == 'POST':

            nome = request.form.get('nome')
            senha = request.form.get('senha')
            cargo = request.form.get('cargo')

            nome_usuario = None
            error = "senha ou nome inválidos"

            match cargo:
                case 'adm':
                    nome_usuario = Adm.get_or_none(Adm.nome == nome)
                    if not nome_usuario:
                        return render_template('login.html', error = error)
                case 'gestor':
                    nome_usuario = Gestor.get_or_none(Gestor.nome == nome)
                    if not nome_usuario:
                        return render_template('login.html', error = error)   
                case 'cuidador':
                    nome_usuario = Cuidadores.get_or_none(Cuidadores.nome == nome)
                    if not nome_usuario:
                        return render_template('login.html', error = error)
                
            if not senha:
                return render_template('login.html', error = error)
            
            if nome_usuario.senha != senha:
                return render_template('login.html', error = error)
            
            session['cargo'] = cargo

            match cargo:
                case 'adm':
                    session['usuario_id'] = nome_usuario.id_adm
                    return redirect(url_for('adm.painel'))
                
                case 'gestor':
                    session['usuario_id'] = nome_usuario.id_gestor
                    return redirect(url_for('gestor.painel'))
                
                case 'cuidador':
                    session['usuario_id'] = nome_usuario.id_cuidador
                    return redirect(url_for('cuidador.painel'))


        return render_template('login.html')