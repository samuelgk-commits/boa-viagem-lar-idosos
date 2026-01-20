from Database.models.adm import Adm

def criar_adm_padrao():
    #cria um adm padrão 
    existe = Adm.select().exists()
    
    if not existe:
        Adm.create(
            nome="adm",
            senha="123",
            email="admin@boaviagem.com"
        )
        Adm.create(
            nome="Samuel Amaral",
            senha="1234",
            email="samuel@boaviagem.com"
        )