from flask import Blueprint, render_template, session, redirect, url_for

rota_gestor = Blueprint('gestor', __name__)

@rota_gestor.route('/painel', methods=['GET'])
def painel():
    if session.get("cargo") != "gestor":
        return redirect(url_for('login.entrar'))

    return render_template('gestor/painel.html')
