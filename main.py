from flask import Flask
from configuration import configure_all, password_session


app = Flask(__name__)

good_password = password_session(length=24)
print(good_password)

app.secret_key = good_password 

configure_all(app)

app.run(debug=True)