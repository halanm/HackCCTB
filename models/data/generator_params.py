class GeneratorParams:
    params = []

    def __init__(self, text, placeholder, options, type, generator):
        self.text = text
        self.placeholder = placeholder
        self.options = options
        self.type = type
        self.generator = generator

        GeneratorParams.params.append(self)

    def list_params_by_generator(generator):
        return [params for params in GeneratorParams.params if params.generator == generator]