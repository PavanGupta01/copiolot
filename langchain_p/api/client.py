import requests
import streamlit as st


def get_llama2_response(input_text):
    response = requests.post("http://localhost:8000/essay/invoke", json={"input": {"topic": input_text}})
    return response.json()["output"]


## Streamlit framework
st.title("Langserve demo with FastAPI and Ollama")
input_text = st.text_input("Write essay on: ")

if input_text:
    st.write(get_llama2_response(input_text))
