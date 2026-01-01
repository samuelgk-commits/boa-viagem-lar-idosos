from peewee import CharField , DateField ,AutoField, DateTimeField, BooleanField 
from Database.database import db
from Database.models.base_model import BaseModel

class Cuidadores(BaseModel):
    id_cuidador = AutoField()
    nome = CharField(max_length=150)
    senha = CharField(max_length=255)
    telefone = CharField(max_length=20)
    data_contratacao = DateField()
    turno = CharField(max_length=10)  # enum('manha','tarde','noite','integral')
    criado_em = DateTimeField()
    atualizado_em = DateTimeField()

    class Meta:
        table_name = "cuidadores"
