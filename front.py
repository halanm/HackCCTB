import streamlit as st
import pandas as pd

def main():
    st.write("""
    # My first app
    Hello *world!*
    """)
    
    df = pd.read_csv("my_data.csv")
    st.line_chart(df)


if __name__ =='__main__':
    main()