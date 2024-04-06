class Generator:
    generators = []

    def __init__(self, name, category, prompt):
        self.name = name
        self.category = category
        self.prompt = prompt
        Generator.generators.append(self)

    def list_generators_by_category(category):
        return [model for model in Generator.generators if model.category == category]