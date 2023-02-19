from peewee import AutoField, TextField, CharField, DateTimeField

from app.models.base_model import Base


class Recipes(Base):
    id = AutoField()

    name = CharField()
    description = TextField()
    recipe_time = DateTimeField()
    calories = CharField()
