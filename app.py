import streamlit as st

st.title("NeuralNova AI Study Assistant")

user_input = st.text_input("Ask something:")

if user_input:
st.write("You asked:", user_input)
st.write("AI response will come here soon.")
