from peewee import SqliteDatabase
import os
import sys

def get_base_path():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(os.path.abspath(__file__))


BASE_DIR = get_base_path()
db_path = os.path.join(BASE_DIR, "boaviagem.db")

db = SqliteDatabase(db_path)
