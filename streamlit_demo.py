from langchain_openai import ChatOpenAI
import streamlit as st

st.title("question and answer session")

with st.sidebar:
    st.title("Provide your Api Key")
    OPENAI_API_KEY=st.text_input("OpenAI API Key", type="password")

if not OPENAI_API_KEY:
    st.info("OpenAI API Key not provided")
    st.stop()

llm = ChatOpenAI(model="gpt-4o", api_key=OPENAI_API_KEY)

question = st.text_input("What is the question : ")

if question:
    response = llm.invoke(question)
    st.write(response.content)