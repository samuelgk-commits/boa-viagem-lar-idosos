from flask import Flask
from configuration import configure_all
from utils import password_session
import webbrowser
from flask import make_response

app = Flask(__name__)

good_password = password_session(length=24)

app.secret_key = good_password 

configure_all(app)

#if __name__ == "__main__":
 #   webbrowser.open("http://127.0.0.1:5000")
app.run(debug=True)

