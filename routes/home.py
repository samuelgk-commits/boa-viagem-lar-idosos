from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from Database.models.gestor import Gestor
from Database.models.adm import Adm
from Database.models.cuidadores import Cuidadores


rota_home = Blueprint('home', __name__)

@rota_home.route('/login', methods=['GET', 'POST'])
def entrar():
        
    if request.method == 'POST':
        nome = request.form.get('nome')
        senha = request.form.get('senha')
        cargo = request.form.get('cargo')

        usuario = None

        if cargo == 'ADM':
            usuario = Adm.get_or_none(Adm.nome == nome)

        elif cargo == 'gestor':
            usuario = Gestor.get_or_none(Gestor.nome == nome)

        elif cargo == 'cuidador':
            usuario = Cuidadores.get_or_none(Cuidadores.nome == nome)

        if not usuario:
            flash("Usuário não encontrado!")
            return render_template('login.html')

        if usuario.senha != senha:
            flash("Senha incorreta!")
            return render_template('login.html')


        if cargo == 'ADM':
            session['usuario_id'] = usuario.id_adm
        elif cargo == 'gestor':
            session['usuario_id'] = usuario.id_gestor
        elif cargo == 'cuidador':
            session['usuario_id'] = usuario.id_cuidador

        session['cargo'] = cargo

        if cargo == 'ADM':
            return redirect(url_for('adm.painel'))
        elif cargo == 'gestor':
            return redirect(url_for('gestor.painel'))
        elif cargo == 'cuidador':
            return redirect(url_for('cuidador.painel'))

    return render_template('login.html')
