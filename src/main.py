import os

import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, html
from dash.dependencies import Input, Output
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain.vectorstores import FAISS

# # User inputs--------------------------------
# # Allow user input for key
# OPENAI_API_KEY = input("Enter your OpenAI API key: ")
# # Allow user input for question
# query = input("Enter your question: ")


app = dash.Dash(__name__)

app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H1("Language Model Query Tool"),
                    ]
                ),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.CardGroup(
                            [
                                dbc.Label("OpenAI API Key"),
                                dbc.Input(
                                    id="api_key",
                                    type="password",
                                    placeholder="Enter your OpenAI API key",
                                ),
                            ]
                        ),
                        dbc.CardGroup(
                            [
                                dbc.Label("Question"),
                                dbc.Input(
                                    id="question",
                                    type="text",
                                    placeholder="Enter your question",
                                ),
                            ]
                        ),
                        dbc.Button(
                            "Submit",
                            id="submit_button",
                            color="primary",
                            className="mt-3",
                        ),
                    ],
                    width=6,
                ),
                dbc.Col(
                    [
                        html.H2("Answer"),
                        html.Div(id="answer"),
                    ]
                ),
            ]
        ),
    ],
    fluid=True,
)


@app.callback(
    Output("answer", "children"),
    [Input("submit_button", "n_clicks")],
    [
        dash.dependencies.State("api_key", "value"),
        dash.dependencies.State("question", "value"),
    ],
)
def process_query(n_clicks, api_key, question):
    if n_clicks is None or api_key is None or question is None:
        return ""

    else:
        OPENAI_API_KEY = api_key
        query = question

        path = "./data/vector_data/"
        if os.path.exists(path):
            vector_store = FAISS.load_local(
                path, OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
            )
        else:
            return f"Upload index.faiss and index.pkl files to {path} directory first"

        system_template = """Use the following pieces of context to answer the users question.\
        Take note of the sources and include them in the answer in the format: "SOURCES: source1 source2",\
        use "SOURCES" in capital letters regardless of the number of sources.\
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
            model_name="gpt-3.5-turbo", temperature=0, openai_api_key=OPENAI_API_KEY)

        chain = RetrievalQAWithSourcesChain.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=vector_store.as_retriever(),
            return_source_documents=True,
            chain_type_kwargs=chain_type_kwargs,
        )

        result = chain(query)

        return result["answer"]


if __name__ == "__main__":
    app.run_server(debug=True)
