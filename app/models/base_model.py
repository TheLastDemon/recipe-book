from peewee import Model, PostgresqlDatabase

from core.databases import postgres_database


class Base(Model):
    class Meta:
        database: PostgresqlDatabase = postgres_database
