class Generator():
    generators = []

    def __init__(self, name, description, category, prompt):
        self.name = name
        self.description = description
        self.category = category
        self.prompt = prompt
        Generator.generators.append(self)

    def list_generators_by_category(category):
        return [model for model in Generator.generators if model.category == category]