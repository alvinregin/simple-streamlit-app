import streamlit as st

st.title("Simple Streamlit App")

name = st.text_input("Enter your name:")

if name:
    st.write(f"Hello, {name}! Welcome to Streamlit.")
else:
    st.write("Please enter your name above.")
