from flask import Blueprint, render_template, session, redirect, url_for


rota_cuidador = Blueprint('cuidador', __name__)

@rota_cuidador.route('/painel', methods=['GET'])
def painel():
    if session.get("cargo") != "cuidador":
        return redirect(url_for('login.entrar'))

    return render_template('cuidador/painel.html')


