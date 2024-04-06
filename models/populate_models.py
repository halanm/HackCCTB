from models.data.category import Category
from models.data.generator import Generator

def populate_categories():
    Category(name="Category 1", description="Description 1")
def populate_generators():
    Generator(name="Model 1", description="Description 1", category="Category 1", prompt="Prompt 1")