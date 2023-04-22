import os
from typing import Optional

from langchain.chains import ConversationalRetrievalChain, RetrievalQAWithSourcesChain
from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain.prompts.prompt import PromptTemplate
from langchain.vectorstores import FAISS


def process_query(
        api_key:str, 
        question:str, 
        path:str, 
        temp_val:float, 
        memory:str, 
        chat_history:Optional[str]=None) -> dict:
    """
    This function processes the user's question by feeding it to the LLM and returns the result.
    The result is a dictionary containing an answer to the question, source documents (evidence), 
    and chat history (if memory is activated).
    The LLM used is OpenAI's GPT-3.5-turbo model. The temperature value affects how "deterministic" 
    or "creative" the model replies are. The higher the temperature value, the more "creative" the model is.

    Args:

        api_key (str): OpenAI API key
        question (str): User's question
        path (str): Path to the vector store
        temp_val (float): Temperature value
        memory (str): Whether to remember the context of the previous conversation
        chat_history (Optional[str], optional): Chat history. Defaults to None.

    Returns:

        dict: A dictionary containing an answer to the question, source documents (evidence),
        and chat history (if memory is activated).
    """
    if os.path.exists(path):
        vector_store = FAISS.load_local(
            path, OpenAIEmbeddings(openai_api_key=api_key)
        )
    else:
        return "Upload index.faiss and index.pkl files to {path} directory first"

    if memory == "No":
        # Does not remember the context of the previous conversation
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
        # Remembers the context of the previous conversation, memory == "Yes"
        memory_template = """
        Given the following chat history and a follow up question, rephrase the\
        follow up question to be a standalone question.\
        The follow up question may not always be based on the chat history.\
        If follow up question is not based on the chat history, do not rephrase it.\
        If follow up question is not based on the chat history, you should still answer it\
        in the context of the AI Practitioner Handbook.\
        If the question is not in the context of AI Practitioner Handbook, just say that "I don't know".\
        Chat History:{chat_history}\
        Follow Up Question: {question}\
        Standalone Question:
        """

        CONDENSE_QUESTION_PROMPT = PromptTemplate.from_template(memory_template)

        template = """You are an AI assistant for answering questions about the AI Practitioner Handbook.\
        You are given the following extracted parts of a long document and a question.\
        Provide a conversational answer.\
        If you don't know the answer, just say "I don't know". Don't try to make up an answer.\
        If the question is not about the AI Practitioner Handbook, just say that "I don't know".
        Question: {question}
        =========
        {context}
        =========
        Answer:
        """
        QA_PROMPT = PromptTemplate(template=template, input_variables=[
                                   "question", "context"])

        llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=temp_val, openai_api_key=api_key)

        chain = ConversationalRetrievalChain.from_llm(
            llm=llm,
            retriever=vector_store.as_retriever(),
            chain_type="stuff",
            return_source_documents=True,
            condense_question_prompt=CONDENSE_QUESTION_PROMPT,
            qa_prompt=QA_PROMPT,
            output_key="answer",
        )

        result = chain({"question": question, "chat_history": chat_history})

        chat_history.append((question, result["answer"]))

    return result