import os

from langchain.chains import RetrievalQAWithSourcesChain, ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain.vectorstores import FAISS

# TODO: Add memory to the conversation
# TODO: Add more context to the question template
# TODO: Type hinting and docstrings
def process_query(api_key, question, path, temp_val, memory):
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
    If the question is not related to the AI Practitioner Handbook, just say that "I don't know".\
    ----------------
    {summaries}"""

    messages = [
        SystemMessagePromptTemplate.from_template(system_template),
        HumanMessagePromptTemplate.from_template("{question}"),
    ]
    prompt = ChatPromptTemplate.from_messages(messages)

    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=temp_val, openai_api_key=api_key)

    if not memory:
        # Does not remember the context of the previous conversation
        chain_type_kwargs = {"prompt": prompt}

        chain = RetrievalQAWithSourcesChain.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=vector_store.as_retriever(),
            return_source_documents=True,
            chain_type_kwargs=chain_type_kwargs,
        )

        result = chain(question)

    else:
        # Remembers the context of the previous conversation
        

    return result