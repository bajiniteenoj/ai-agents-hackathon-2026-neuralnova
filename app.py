import streamlit as st

st.title("NeuralNova AI Study Assistant")

user_input = st.text_input("Ask something:")

if user_input:
    st.write("You asked:", user_input)


if "python" in user_input.lower():
    st.write("Python is a powerful programming language used in AI and automation.")

elif "ai" in user_input.lower():
    st.write("Artificial Intelligence helps machines learn and make decisions.")

else:
    st.write("I'm still learning. More AI features coming soon.")
