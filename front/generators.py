
from models.data.generator import Generator
from models.data.generator_params import GeneratorParams
from tool.llm import Llm

import streamlit as st

class GeneratorFront:
    def generators_front(sbsb):
        generators = []
        for generator in Generator.list_generators_by_category(sbsb):
            generators.append(generator.name)
        generatorName = st.selectbox(sbsb, generators)
        
        generator = Generator.get_generator_by_name(generatorName)

        st.header(generator.name)
        params = []

        for param in GeneratorParams.list_params_by_generator(generator.name):
            if(param.type == "text"):
                params.append({
                    "text": param.text,
                    "value": st.text_input(placeholder=param.placeholder, label=param.text, value="")
                })
            elif(param.type == "number"):
                params.append({
                    "text": param.text,
                    "value": st.number_input(label=param.text, value=0)
                })
            elif(param.type == "textarea"):
                params.append({
                    "text": param.text,
                    "value": st.text_area(placeholder=param.placeholder, label=param.text, value="")
                })
            elif(param.type == "select"):
                options = param.options.split(";")
                params.append({
                    "text": param.text,
                    "value": st.selectbox(label=param.text, options=options)
                })

        if(st.button(f"Generate {generator.name}")):
            canProceed = True
            for param in params:
                if(param["value"] == ""):
                    st.error("Please fill all the fields.")
                    canProceed = False
                    break
            
            if(canProceed):
                response = Llm.get_response(Llm.get_prompt(generator, params))
                st.write(response)