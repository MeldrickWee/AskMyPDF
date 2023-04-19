import os
import streamlit as st
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain.vectorstores import FAISS

# TODO: Add more context to the question template
# TODO: Type hinting and docstrings


def process_query(api_key, question):
    path = "../data/vector_data/"
    if os.path.exists(path):
        vector_store = FAISS.load_local(
            path, OpenAIEmbeddings(openai_api_key=api_key)
        )
    else:
        return "Upload index.faiss and index.pkl files to {path} directory first"

    system_template = """Use the following pieces of context to answer the users question.\
    No matter what the question is, you should always answer it in the context of the AI Practitioner Handbook.\
    Even if the question does not end in a question mark, you should still answer it as if it were a question.\
    If you don't know the answer, just say that "I don't know", don't try to make up an answer.\
    ----------------
    {summaries}"""

    messages = [
        SystemMessagePromptTemplate.from_template(system_template),
        HumanMessagePromptTemplate.from_template("{question}"),
    ]
    prompt = ChatPromptTemplate.from_messages(messages)

    chain_type_kwargs = {"prompt": prompt}

    llm = ChatOpenAI(
        model_name="gpt-3.5-turbo", temperature=0, openai_api_key=api_key)

    chain = RetrievalQAWithSourcesChain.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vector_store.as_retriever(),
        return_source_documents=True,
        chain_type_kwargs=chain_type_kwargs,
    )

    result = chain(question)
    return result


st.markdown("<h1 style='text-align: center; font-size: 30px;'>Ask A PDF:<br />Question Answering for AI Practitioner Handbook</h1><br /><br /><br />", unsafe_allow_html=True)

api_key = st.text_input("Enter your OpenAI API key:", type="password")

st.markdown("<p style='font-size: 12px;'>This API key is never saved. You can get your API key from <a href='https://platform.openai.com/account/api-keys'>here</a>.</p><br /><br /><br />", unsafe_allow_html=True)

dropdown_options = [
    "Enter a question",
    "Who are the contributors to this book?",
    "What is the job of an AI engineer?",
    "What is a technical lead?",
    "What are the various data splitting strategies?",
    "Is Bruce Wayne the real Batman?",
]
selected_option = st.selectbox(
    "Enter your own question or select a pre-defined one:", dropdown_options)

if selected_option == "Enter a question":
    custom_question_expander = st.expander("Enter your custom question here:")
    custom_question = custom_question_expander.text_input(
        "", key="custom_question")
else:
    custom_question = ""

if st.button("Submit"):
    if api_key:
        if custom_question:
            question = custom_question
        elif selected_option != "Enter a question":
            question = selected_option
        else:
            st.write("Please select a question or enter a custom question.")
            question = None

        if question:
            answer = process_query(api_key, question)
            st.write(answer)
    else:
        st.write("Please provide your API key.")
