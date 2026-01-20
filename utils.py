import secrets, string, webbrowser
from flask import session, redirect, url_for

def abrir_nav():
    #abre a aplicação no navegador ao clicar no icone
    webbrowser.open_new("http://127.0.0.1:5000")

def password_session(length = 24):
    #cria uma senha aleatoria para proteger os dados numa sessão, podem ser vistos porem não editados
    all_caracters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(all_caracters) for i in range(length))
    return password

def validar_adm():
    #validação para que cada um só acesse oque seu privilegio permite
    if 'cargo' not in session:
        return redirect(url_for('home.login'))

    if session.get("cargo") != "adm":
        return redirect(url_for('home.login'))

    return None

def validar_gestor():
    #validação para que cada um só acesse oque seu privilegio permite
    if 'cargo' not in session:
        return redirect(url_for('home.login'))

    if session.get("cargo") != "gestor":
        return redirect(url_for('home.login'))

    return None

def validar_cuidador():
    #validação para que cada um só acesse oque seu privilegio permite
    if 'cargo' not in session:
        return redirect(url_for('home.login'))

    if session.get("cargo") != "cuidador":
        return redirect(url_for('home.login'))

    return None

