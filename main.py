from flask import Flask
from configuration import configure_all, password_session
import webbrowser
from flask import make_response

app = Flask(__name__)

good_password = password_session(length=24)
print(good_password)

app.secret_key = good_password 

configure_all(app)

@app.after_request
def bloquear_cache(response):
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, private"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

#if __name__ == "__main__":
 #   webbrowser.open("http://127.0.0.1:5000")
app.run(debug=True)

