import streamlit as st
from streamlit_chat import message
from tool.llm import Llm
 
class ChatFront:
    def chat_front():
        st.session_state['history'] = []
        
        if 'last_messages' not in st.session_state:
            st.session_state['last_messages'] = [{"role": "system", "content": "You are an AI called Hysis that helps users with their queries."}]
        if 'history' not in st.session_state:
            st.session_state['history'] = []
        if 'generated' not in st.session_state:
            st.session_state['generated'] = ["Hello ! My name is Hysis and I am virtual chat! If you have a questions, ask me! 🤗"]
        if 'past' not in st.session_state:
            st.session_state['past'] = ["Hey ! 👋"]
        
        user_input = st.chat_input("Talk to csv data 👉 (:", key='input')
    
        if user_input:    
            output = Llm.get_response_chat(user_input, st.session_state['last_messages'])
            st.session_state['past'].append(user_input)
            st.session_state['generated'].append(output["response"])

            st.session_state['last_messages'].append({"role": "assistant", "content": output["response"]})
            
        if st.session_state['generated']:
            for i in range(len(st.session_state['generated'])):
                message(st.session_state["past"][i], is_user=True, key=str(i) + '_user', avatar_style="big-smile")
                message(st.session_state["generated"][i], key=str(i), avatar_style="thumbs")