import streamlit as st
from streamlit_chat import message
from tool.llm import Llm
 
class ImageFront:
    def image_front():
        prompt = st.text_input(placeholder="Your image prompt", label="Prompt", value="")

        if st.button("Generate"):
            response = Llm.get_image(prompt)
            
            st.image(response)