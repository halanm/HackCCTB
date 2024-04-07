import sys
sys.dont_write_bytecode = True

from models.populate_models import PopulateModels
from models.data.category import Category
from front.generators import GeneratorFront
from front.chat import ChatFront

import streamlit as st

def main():
    PopulateModels.populate_models()
    
    categories = []
    for category in Category.list_categories():
        categories.append(category.name)
        
    categories.append("Chat")
        

    st.sidebar.header("Generation AI")

    sbsb = st.sidebar.selectbox(label="Categories", options=categories)
    if sbsb == "Chat":
        ChatFront.chat_front()
    else:
        GeneratorFront.generators_front(sbsb)
        


   
        
    
    

if __name__ == '__main__':
    main()