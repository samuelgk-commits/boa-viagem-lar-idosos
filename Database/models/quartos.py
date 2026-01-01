from peewee import IntegerField, AutoField
from Database.database import db
from Database.models.base_model import BaseModel

class Quartos(BaseModel):
    id_quarto = AutoField()
    num_quarto = IntegerField()
    andar = IntegerField()

    class Meta:
        table_name = "quartos"
