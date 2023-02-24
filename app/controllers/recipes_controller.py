import datetime

from flask import Blueprint, request, jsonify

from app.services import recipes_service
from core.cache import cache

recipes = Blueprint(name=__name__.split('.')[-1], import_name=__name__)


@recipes.route('/get-recipes', methods=['GET'])
@cache.cached(timeout=30, query_string=True)
def get_all_recipes():
    entrypoint = datetime.datetime.now()
    print('entrypoint: ', entrypoint)

    data = recipes_service.get_all_recipes()

    response = jsonify(data)

    exitpoint = datetime.datetime.now()
    print('exitpoint: ', exitpoint)
    print('diff: ', (exitpoint-entrypoint).microseconds)

    return response, 200


@recipes.route('/get-recipe-by-recipe-id', methods=['POST'])
@cache.cached(timeout=30, query_string=True)
def get_recipe_by_id():
    entrypoint = datetime.datetime.now()
    print('entrypoint: ', entrypoint)

    recipe_id = request.json.get('recipe_id', None)

    data = recipes_service.get_recipe_by_id(recipe_id)

    response = jsonify(data)

    exitpoint = datetime.datetime.now()
    print('exitpoint: ', exitpoint)
    print('diff: ', (exitpoint-entrypoint).microseconds)

    return response, 200


@recipes.route('/create-recipe', methods=['POST'])
@cache.cached(timeout=30, query_string=True)
def create_recipe():
    entrypoint = datetime.datetime.now()
    print('entrypoint: ', entrypoint)

    name = request.json.get('name', None)
    description = request.json.get('description', None)
    recipe_time = request.json.get('recipe_time', None)
    calories = request.json.get('calories', None)

    recipe_time = datetime.datetime.fromtimestamp(recipe_time)

    data = recipes_service.create_recipe(name, description, recipe_time, calories)

    response = jsonify(data)

    exitpoint = datetime.datetime.now()
    print('exitpoint: ', exitpoint)
    print('diff: ', (exitpoint-entrypoint).microseconds)

    return response, 200
