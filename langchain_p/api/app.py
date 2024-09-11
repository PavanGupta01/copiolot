from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes

import uvicorn
import os
from langchain_community.llms.ollama import Ollama


app = FastAPI(title="Langchain server", version="1.0", description="My first langserve API server")

# add_routes(app, ChatOpenAI(), path="/openai")

model = ChatOpenAI()

## Ollama llama2
llm = Ollama(model="llama3")

essay_prompt = ChatPromptTemplate.from_template("Write me an essay about {topic} with 50 words")
poem_prompt = ChatPromptTemplate.from_template("Write me a poem about {topic} in 10 lines")

add_routes(app, essay_prompt | llm, path="/essay")

add_routes(app, poem_prompt | llm, path="/poem")


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
