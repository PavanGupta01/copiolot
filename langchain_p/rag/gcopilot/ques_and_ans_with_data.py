from langchain_community.llms import Ollama
from langchain_community.embeddings import OllamaEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.vectorstores import DocArrayInMemorySearch
from operator import itemgetter
import streamlit as st


loader = DirectoryLoader("/Users/pavangupta/Documents/projects/copiolot/langchain_practice/rag/gcopilot/data")
pages = loader.load()
pages


MODEL = "llama3"
model = Ollama(model=MODEL)
embeddings = OllamaEmbeddings(model=MODEL)

parser = StrOutputParser()


template = """
You are a Q&A assistant for Employees. Your goal is to answer questions as
accurately as possible based on the instructions and context policy documents provided.

Context: {context}

Question: {question}
"""

prompt = PromptTemplate.from_template(template)
# prompt.format(context="Here is some context", question="Here is a question")

chain = prompt | model | parser


vectorstore = DocArrayInMemorySearch.from_documents(pages, embedding=embeddings)
retriever = vectorstore.as_retriever()


chain = (
    {
        "context": itemgetter("question") | retriever,
        "question": itemgetter("question"),
    }
    | prompt
    | model
    | parser
)

## Streamlit framework
st.title("G-Copilot Demo")
input_text = st.text_input("Search any topic here")

if input_text:
    st.write(chain.invoke({"question": input_text}))

# questions = [
#     "all Type of leave are there",
#     "What are the leave policy guidelines?",
#     # "Get me the Pune and Vadodara holiday list",
#     "What is Group Personal Accident Policy?",
#     # "What are the Policies in effect?",
#     # "How much is the night shift allowns?",
#     # "High Level Overview of the insurrance Process?",
#     # "What is Group Term Life Insurance Policy",
#     # "How many coding assignments are there in the program?",
#     # "Is there a program certificate upon completion?",
#     # "What programming language will be used in the program?",
#     # "How much does the program cost?",
# ]

# for question in questions:
#     print(f"Question: {question}")
#     print(f"Answer: {chain.invoke({'question': question})}")
#     print()
