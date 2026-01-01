from peewee import Model
from Database.database import db

class BaseModel(Model):
    class Meta:
        database = db
