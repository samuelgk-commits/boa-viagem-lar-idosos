from routes.home import rota_home 
from routes.hospedes import rota_hospedes
from routes.login import rota_login
from routes.adm import rota_adm
from routes.gestor import rota_gestor
from routes.cuidador import rota_cuidador
from Database.database import db
from Database.models.hospedes import Hospedes
from Database.models.adm import Adm
from Database.models.gestor import Gestor
from Database.models.atendimentos import Atendimentos
from Database.models.cuidadores import Cuidadores
from Database.models.cuidados import Cuidados
from Database.models.quartos import Quartos

def configure_all(app):
    configure_routes(app)
    configure_db()

def configure_routes(app):
    app.register_blueprint(rota_home)
    app.register_blueprint(rota_hospedes, url_prefix='/hospedes') 
    app.register_blueprint(rota_login) 
    app.register_blueprint(rota_adm, url_prefix="/adm")
    app.register_blueprint(rota_gestor, url_prefix="/gestor") 
    app.register_blueprint(rota_cuidador, url_prefix="/cuidador") 

def configure_db():

    if db.is_closed():
        db.connect()

    db.create_tables(
        [Hospedes, Adm, Gestor, Quartos, Cuidados, Cuidadores, Atendimentos],
        safe=True 
    )

   
