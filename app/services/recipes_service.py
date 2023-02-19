from playhouse.shortcuts import model_to_dict

from app.models import Recipes


def get_all_recipes():
    recipes = [author for author in Recipes.select().dicts()]

    return recipes


def get_recipe_by_id(recipe_id):
    recipe = Recipes.get_by_id(recipe_id)

    return model_to_dict(recipe)


def create_recipe(name, description, recipe_time, calories):
    (recipe, _) = Recipes.get_or_create(name=name, description=description, recipe_time=recipe_time, calories=calories)

    return model_to_dict(recipe)
