from flask import Flask
from configuration import configure_all, password_session
import webbrowser

app = Flask(__name__)

good_password = password_session(length=24)
print(good_password)

app.secret_key = good_password 

configure_all(app)

#if __name__ == "__main__":
 #   webbrowser.open("http://127.0.0.1:5000")
app.run(debug=True)

