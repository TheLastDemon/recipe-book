from contextlib import suppress

from peewee import InterfaceError

from app.models.recipes_model import Recipes


def create_nonexissting_tables():
    with suppress(InterfaceError):
        Recipes.create_table()
