from flask import Flask

from app.controllers import recipes
from app.utilities.helpers import create_nonexissting_tables
from core.cache import cache
from core.databases import cache_redis_database

create_nonexissting_tables()


app: Flask = Flask(import_name=__name__)
cache.init_app(app,
               # cache_redis_database
               )

app.register_blueprint(recipes)


