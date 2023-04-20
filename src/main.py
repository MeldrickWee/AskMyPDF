import streamlit as st

from query_processor import process_query

# Title 
st.markdown("<h1 style='text-align: center; font-size: 30px;'>Ask My PDF:<br />Question Answering for AI Practitioner Handbook</h1><br /><br /><br />", unsafe_allow_html=True)

# API key input
api_key = st.text_input("Enter your OpenAI API key:", type="password")

# API key additional user info
st.markdown("<p style='font-size: 12px;'>This API key is never saved. You can get your API key from <a href='https://platform.openai.com/account/api-keys'>here</a>.</p><br /><br /><br />", unsafe_allow_html=True)

# dropdown options
dropdown_options = [
    "Enter your question",
    "Who are the contributors to this book?",
    "What is the job of an AI engineer?",
    "What is a technical lead?",
    "What are the various data splitting strategies?",
    "Is Bruce Wayne the real Batman?",
]
# dropdown box selection
selected_option = st.selectbox(
    "Enter your own question or select a pre-defined one:", dropdown_options)

if selected_option == "Enter your question":
    custom_question_expander = st.expander("Enter your custom question here:")
    custom_question = custom_question_expander.text_input(
        "...", key="custom_question", label_visibility="collapsed")
else:
    custom_question = ""

# submit button actions
if st.button("Submit"):
    if api_key:
        if custom_question:
            question = custom_question
        elif selected_option != "Enter your question":
            question = selected_option
        else:
            st.write("Please select a question or enter a custom question.")
            question = None

        if question:
            path = "data/vector_data/"
            answer = process_query(api_key, question, path)
            st.write(answer)
    else:
        st.write("Please provide your API key.")

