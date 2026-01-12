from peewee import Model , CharField , AutoField, DateTimeField  
from Database.database import db
from Database.models.base_model import BaseModel
import datetime

class Gestor(BaseModel):
    id_gestor = AutoField()
    nome = CharField(max_length=150)
    email = CharField(max_length=150)
    senha = CharField(max_length=255)
    criado_em = DateTimeField(default=datetime.datetime.now)
    atualizado_em = DateTimeField(default=datetime.datetime.now)
    
    class Meta:
        table_name = "gestor"