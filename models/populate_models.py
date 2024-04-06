from models.data.category import Category
from models.data.generator import Generator
from models.data.generator_params import GeneratorParams
import json

class PopulateModels():
    def populate_models():
        if Category.categories == []:
            f = open("data/categories.json")

            categories_data = json.load(f)

            for category in categories_data:
                Category(name=category["name"], description=category["description"])

                PopulateModels.populate_generators(category["key"], category["name"])
    
    def populate_generators(key, category):
        if Generator.list_generators_by_category(category) == []:
            f = open(f"data/generators/{key}.json")

            data = json.load(f)

            for generator in data:
                Generator(name=generator["name"], category=generator["category"], prompt=generator["prompt"])

                for param in generator["params"]:
                    GeneratorParams(text=param["text"], placeholder=param["placeholder"], options=param["options"], type=param["type"], generator=generator["name"])