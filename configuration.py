from Database.database import db
from routes.home import rota_home 
from routes.hospedes import rota_hospedes
from routes.adm import rota_adm
from routes.gestor import rota_gestor
from routes.cuidador import rota_cuidador
from Database.models.hospedes import Hospedes
from Database.models.adm import Adm
from Database.models.gestor import Gestor
from Database.models.atendimentos import Atendimentos
from Database.models.cuidadores import Cuidadores
from Database.models.cuidados import Cuidados
from Database.models.quartos import Quartos
import secrets, string

def criar_adm_padrao():
    #cria um adm padrão 
    existe = Adm.select().exists()
    
    if not existe:
        Adm.create(
            nome="adm",
            senha="123",
            email="admin@boaviagem.com"
        )

def password_session(length = 24):
    #cria uma senha aleatoria para proteger os dados numa sessão, podem ser vistos porem não editados
    all_caracters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(all_caracters) for i in range(length))
    return password
    
def configure_all(app):
    #junta todas as configurações feitas aqui para mandar pro main
    configure_routes(app)
    configure_db()

def configure_routes(app):
    #função que agrupa os blueprints para melhor organização dentro do main
    app.register_blueprint(rota_home)
    app.register_blueprint(rota_hospedes, url_prefix='/hospedes')  
    app.register_blueprint(rota_adm, url_prefix="/adm")
    app.register_blueprint(rota_gestor, url_prefix="/gestor") 
    app.register_blueprint(rota_cuidador, url_prefix="/cuidador") 



def configure_db():
    #função para testar/abrir o banco 
    if db.is_closed():
        db.connect()


    db.create_tables(
        [Hospedes, Adm, Gestor, Quartos, Cuidados, Cuidadores, Atendimentos],
        safe=True 
    )
    criar_adm_padrao()


