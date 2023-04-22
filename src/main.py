import streamlit as st

from query_processor import process_query

# Check if the chat_history state is initialized
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Title
st.markdown("<h1 style='text-align: center; font-size: 30px;'>Ask My PDF:<br />Question Answering for AI Practitioner Handbook</h1><br /><br /><br />", unsafe_allow_html=True)

# API key input
api_key = st.text_input("Enter your OpenAI API key:", type="password")

# API key additional user info
st.markdown("<p style='font-size: 12px;'>This API key is never saved. You can get your API key from <a href='https://platform.openai.com/account/api-keys'>here</a>.</p><br />", unsafe_allow_html=True)

# Add a slider for the temperature value
temperature = st.slider("Temperature:", min_value=0.0,
                        max_value=1.0, value=0.5, step=0.01)

# Addtional info for temperature
st.markdown("<p style='font-size: 12px;'>From most deterministic to most creative reply.</p><br />", unsafe_allow_html=True)

# Add the memory checkbox
memory = st.radio("Remember chat history (conversation memory)?", ["Yes", "No"])

# dropdown options
dropdown_options = [
    "Enter your question",
    "Who are the contributors to this book?",
    "What is the job of an AI engineer?",
    "What is a technical lead?",
    "Why do AI projects fail?",
    "Is Bruce Wayne really the Batman?",
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
        # Check if the user has entered a question or selected a pre-defined one
        if custom_question:
            question = custom_question
        elif selected_option != "Enter your question":
            question = selected_option
        else:
            st.write("Please select a question or enter a custom question.")
            question = None

        # Check if the user has selected the memory checkbox
        if memory == "Yes":
            # Create containers for the answer, chat history, and source documents
            tab1, tab2, tab3 = st.tabs(["Answer", "Source", "Memory"])
            path = "data/vector_data/"
            result = process_query(api_key=api_key, question=question, path=path, temp_val=temperature, memory=memory, chat_history=st.session_state.chat_history)
            with tab1:
                st.write(result['answer'])
            with tab2:
                st.write(result['source_documents'])
            with tab3:
                st.write(result['chat_history'])

        elif memory == "No":
            # Create containers for the answer, chat history, and source documents
            tab1, tab2, tab3 = st.tabs(["Answer", "Source", "Memory"])
            path = "data/vector_data/"
            result = process_query(api_key=api_key, question=question, path=path, temp_val=temperature, memory=memory)
            with tab1:
                st.write(result['answer'])
            with tab2:
                st.write(result['source_documents'])
            with tab3:
                st.write("Memory not activated. There is no chat history to display.")

    else:
        st.write("Please provide your API key.")

# To run the app, run the following command in the terminal:
# streamlit run src/main.py