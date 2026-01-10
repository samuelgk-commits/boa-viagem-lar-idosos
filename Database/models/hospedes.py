from peewee import Model , CharField , DateField , AutoField, TextField,ForeignKeyField, DateTimeField
import datetime
from Database.database import db
from Database.models.base_model import BaseModel
from Database.models.quartos import Quartos

class Hospedes(BaseModel):
    id_hospede = AutoField()
    nome = CharField()
    data_nascimento = DateField()
    sexo = CharField(max_length=10)  
    responsavel_nome = CharField(max_length=150)
    responsavel_telefone = CharField(max_length=20)
    condicoes_medicas = TextField(null=True)
    alergias = TextField(null=True)
    observacoes = TextField(null=True)
   
    criado_em = DateTimeField()
    atualizado_em = DateTimeField()
    id_quarto = ForeignKeyField(Quartos, backref="hospedes", column_name="id_quarto", null=True)
    class Meta:
        database = db
        #nome da tabela = "hospedes"
