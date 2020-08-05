from peewee import SqliteDatabase, Model, TextField, SmallIntegerField

from utils.base_enum import BaseEnum


db = SqliteDatabase("data.db")


class DataType(BaseEnum):
    json = 0
    html = 1
    xml = 2


class Data(Model):
    origin_data = TextField()
    data_type = SmallIntegerField(choices=DataType.values())
    class Meta:
        database = db
