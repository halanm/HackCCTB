import sys
sys.dont_write_bytecode = True

from models.populate_models import PopulateModels
from models.data.generator import Generator
from models.data.generator_params import GeneratorParams
from tool.llm import Llm

import streamlit as st


def main():
    PopulateModels.populate_models()

    generators = Generator.list_generators_by_category("Headlines")

    for generator in generators:
        if(generator.name == "Persuasive Topic"):
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

if __name__ == '__main__':
    main()
