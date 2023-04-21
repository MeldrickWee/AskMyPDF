# AskMyPDF - Question Answering for AI Practitioner Handbook

The link to the deployed Streamlit app is: https://meldrickwee-askmypdf-srcmain-mqlwnj.streamlit.app/

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
git clone https://github.com/your_username/your_repository.git
```

### 2. Set up a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use "venv\Scripts\activate"
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

## Usage

### 1. Run the Streamlit app

```bash
streamlit run app.py
```

### 2. Open the app in your web browser

Open your web browser and navigate to the URL displayed in your terminal, usually `http://localhost:8501`.

### 3. Enter your OpenAI API key

Type your OpenAI API key into the text input field, which is masked for security purposes.

### 4. Select a predefined question or enter a custom question

Choose a question from the dropdown menu or type a custom question into the input box.

### 5. Enable the memory feature (optional)

Check the "Remember chat history" checkbox if you want the AI to remember the context of previous conversations.

### 6. Adjust the temperature value (optional)

Use the slider to adjust the temperature value, which controls the randomness in AI-generated responses.

### 7. View the AI-generated answer

The answer to your question will be displayed below the input fields.

---

Please note that this app requires an OpenAI API key to function. Make sure to provide a valid key when using the app.

Feel free to customize and extend the app as needed. If you encounter any issues or have suggestions, please open an issue or submit a pull request.
