import os

import pandas as pd

from dotenv import load_dotenv
from langchain.llms import OpenAI
import openai
import streamlit as st

load_dotenv()
openai_key = os.getenv("MEENALI_OPENAI_API_KEY")


## streamlit framework.
st.title("Langchain demo with OpenAI Demo")
input_text = st.text_input("What are you looking for?")


# OPENAI LLMs
llm = OpenAI(temperature=0.8)

print("--" * 40)
print(openai_key)

if input_text:
    resp = llm(input_text)
    st.write(resp)
