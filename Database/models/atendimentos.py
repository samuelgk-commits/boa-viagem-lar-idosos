from peewee import Model , CharField , AutoField, TextField, DateTimeField , ForeignKeyField
from Database.database import db
from Database.models.hospedes import Hospedes
from Database.models.base_model import BaseModel

class Atendimentos(BaseModel):
    id_atendimento = AutoField()
    hospede = ForeignKeyField(Hospedes, backref="atendimentos", column_name="id_hospede")
    profissional = CharField(max_length=150)
    especialidade = CharField(max_length=150)
    descricao = TextField(null=True)
    data_hora = DateTimeField()

    class Meta:
        table_name = "atendimentos"