import sys
sys.dont_write_bytecode = True

from models.populate_models import populate_categories, populate_generators

populate_categories()
populate_generators()
