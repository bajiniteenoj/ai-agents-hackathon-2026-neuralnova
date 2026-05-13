import streamlit as st
from openai import OpenAI

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(page_title="NeuralNova AI Study Assistant", page_icon="🤖")

st.title("🤖 NeuralNova AI Study Assistant")
st.write("Ask anything and get AI help for studying!")

# -----------------------------
# OpenRouter Client
# -----------------------------
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=st.secrets["OPENROUTER_API_KEY"]
)

# -----------------------------
# Chat input
# -----------------------------
user_input = st.text_input("Ask something:")

if user_input:
    with st.spinner("Thinking... 🤔"):

        try:
            response = client.chat.completions.create(
                model="openai/gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful AI study assistant that explains things simply for students."
                    },
                    {
                        "role": "user",
                        "content": user_input
                    }
                ]
            )

            answer = response.choices[0].message.content
            st.success("AI Response:")
            st.write(answer)

        except Exception as e:
            st.error("Something went wrong. Check logs.")
            st.exception(e)

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption("NeuralNova AI Study Assistant • Built for HackIndia Hackathon 🚀")