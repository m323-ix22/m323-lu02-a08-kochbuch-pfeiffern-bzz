"""
Kochbuch
"""
import json

def load_recipe(json_string):
    return json.loads(json_string)

def adjust_recipe(recipe, persons):
    factor = persons / recipe['servings']
    adjusted_ingredients = {ingredient: int(amount * factor) for ingredient, amount in recipe['ingredients'].items()}
    return {
        "title": recipe['title'],
        "ingredients": adjusted_ingredients,
        "servings": persons
    }

if __name__ == '__main__':
    recipe_json = '{"title": "Spaghetti Bolognese", "ingredients": {"Spaghetti": 400, "Tomato Sauce": 300, "Minced Meat": 500}, "servings": 4}'

    recipe = load_recipe(recipe_json)

    adjusted_recipe = adjust_recipe(recipe, 2)

    print("Angepasstes Rezept:")
    print(json.dumps(adjusted_recipe, indent=4))
