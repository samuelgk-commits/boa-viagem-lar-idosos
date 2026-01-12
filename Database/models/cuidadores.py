from peewee import CharField , DateField ,AutoField, DateTimeField, BooleanField 
from Database.database import db
from Database.models.base_model import BaseModel
import datetime

class Cuidadores(BaseModel):
    id_cuidador = AutoField()
    nome = CharField(max_length=150)
    senha = CharField(max_length=255)
    telefone = CharField(max_length=20)
    data_contratacao = DateField()
    turno = CharField(max_length=10) 
    criado_em = DateTimeField(default=datetime.datetime.now)
    atualizado_em = DateTimeField(default=datetime.datetime.now)

    class Meta:
        table_name = "cuidadores"
