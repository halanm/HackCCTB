class Category:
    categories = []

    def __init__(self, name, description):
        self.name = name
        self.description = description
        Category.categories.append(self)
    
    def list_categories():
        return Category.categories