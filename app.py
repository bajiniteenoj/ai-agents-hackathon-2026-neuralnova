import streamlit as st
from openai import OpenAI

client = OpenAI(
base_url="https://openrouter.ai/api/v1",
api_key=st.secrets["OPENROUTER_API_KEY"]
)

st.title("NeuralNova AI Study Assistant")

user_input = st.text_input("Ask something:")

if user_input:
	response = client.chat.completions.create(
		model="openai/gpt-3.5-turbo",
		messages=[
			{
				"role": "system",
				"content": "You are NeuralNova, an AI study assistant that helps students learn programming, AI, productivity, and exam preparation in a simple and friendly way."
			},
			{
				"role": "user",
				"content": user_input
			}
		]
	)

	st.write("AI Response:")
	st.write(response.choices[0].message.content)
