<h1 align="center">AskMyPDF</h1>
<h2 align="center">Question Answering for AI Practitioner Handbook</h2>

The link to the deployed Streamlit app is: https://meldrickwee-askmypdf-srcmain-1ni4g8.streamlit.app/

TODO: Add explanation of the langchain workflow behind the scenes
TODO: Screen record of using the app
TODO: Include in usage that a paid OpenAI account is requried to play with the app
TODO: Write the risks, potential improvements, installation and usage guide
---

This project allows users to ask questions and receive answers based on the AI Practitioner Handbook.
This project was built in Python 3 with LangChain and deployed with Streamlit.
The AI Practitioner Handbook was created by AI Engineers at AI Singapore.

The AI Practitioner Handbook was first converted from a PDF file into embeddings with OpenAIEmbeddings (OpenAI), 
which cost approximately $0.077. Using FAISS (Facebook), the embeddings are saved as a vector store for 
efficient similaritY search.

The underlying large language model (LLM) implemented for the question and answer task is ChatGPT 3.5 Turbo (OpenAI). 
During question and answering, the LLM is able to answer user questions in context of the AI Practitioner Handbook.
Through iterative experimentations to tune the prompt templates, the LLM does not hallucinate. It generates answers
only when it has the proper sources found from the book. When questions asked are not in the context of the book, 
the LLM replies "I don't know".

## Features

- Input for OpenAI API key which is never saved for security reasons
- Customizable temperature value for controlling randomness in AI-generated responses
- Option to remember chat history for context-aware responses
- Predefined questions available in a dropdown menu
- Custom question input option
- Displays the AI-generated answer to user questions, the source evidence that were used to generate the answer,
and the chat history used for context (if option is chosen)

## Risks

- too reliant on chatgpt
- cant ask questions when you dont know whats the book about
- bad at math

## Potential Improvements

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/MeldrickWee/AskMyPDF.git
```

### 2. Set up a virtual environment "questionanswer" with dependencies installed

```bash
conda create --name questionanswer --file requirements.txt
```

## Usage

### 1. Run the Streamlit app from terminal (Local Deployment Only)

```bash
streamlit run src/main.py
```

### 2. Open the app in your web browser (Local Deployment Only)

Open your web browser and navigate to the URL displayed in your terminal, usually `http://localhost:8501`.

### 3. Enter your OpenAI API key

Type your OpenAI API key into the input field, which is masked for security purposes. The API key is never
saved. However, it is recommended that you still deactivate and delete the key from your OpenAI account after 
trying out the app. 
Your OpenAI account needs to have a payment method entered or you will run into a ratelimit error since every
API request is charged at $0.002 per 1k tokens.

### 4. Adjust the temperature value (optional)

Use the slider to adjust the temperature value, which controls the randomness in AI-generated responses. Spans from most
deterministic to most creative reply.

### 5. Enable the memory feature (optional)

Check the "Yes" button if you want the AI to remember the context of previous conversations.

### 6. Select a predefined question or enter a custom question

Choose a question from the dropdown menu or type a custom question into the input box.

### 7. View the AI-generated answer

The answer to your question will be displayed in the "Answer" tab. The evidence sources that were referred to by the AI before
answering are displayed in the "Source" tab. If you have selected "Yes" for chat history, the previous conversations between you and
the AI that were used to generate context-aware answers are displayed in the "Memory" tab.

---

