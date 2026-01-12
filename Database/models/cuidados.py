from peewee import Model, CharField, AutoField, TextField, DateTimeField,  ForeignKeyField
from Database.database import db
from Database.models.hospedes import Hospedes
from Database.models.cuidadores import Cuidadores
from Database.models.base_model import BaseModel

class Cuidados(BaseModel):
    id_cuidado = AutoField()
    hospede = ForeignKeyField(Hospedes, backref="cuidados", column_name="id_hospede")
    cuidador = ForeignKeyField(Cuidadores, backref="cuidados", column_name="id_cuidador")
    tipo = CharField(max_length=50)  
    descricao = TextField(null=True)
    data_hora = DateTimeField()

    class Meta:
        table_name = "cuidados"
