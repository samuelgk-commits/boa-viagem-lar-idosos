from flask import Flask
from configuration import configure_all
from utils import password_session, abrir_nav
import webbrowser, threading

app = Flask(__name__)

good_password = password_session(length=24)

app.secret_key = good_password 

configure_all(app)

if __name__ == "__main__":
    threading.Timer(1.5, abrir_nav).start()
    app.run()