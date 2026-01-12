from peewee import SqliteDatabase
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db = SqliteDatabase(os.path.join(BASE_DIR, "boaviagem.db"))
