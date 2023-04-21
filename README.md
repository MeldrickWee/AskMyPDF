<h1 align="center">AskMyPDF</h1>
<h2 align="center">Question Answering for AI Practitioner Handbook</h2>

The link to the deployed Streamlit app is: https://meldrickwee-askmypdf-srcmain-1ni4g8.streamlit.app/

TODO: Add explanation of the langchain workflow behind the scenes

TODO: Screen record of using the app

TODO: Write the potential improvements to app

---

This project allows users to ask questions and receive answers based on the AI Practitioner Handbook.
This project was built in Python 3 with LangChain and deployed with Streamlit.
The AI Practitioner Handbook was created by AI Engineers at AI Singapore.

The underlying large language model (LLM) utilized for this Q&A task is ChatGPT 3.5 Turbo, developed by OpenAI. 
It is specifically designed to answer user questions in the context of the AI Practitioner Handbook. 
By carefully refining and iterating upon the prompt templates, I have minimized the model's tendency to 
hallucinate or produce irrelevant responses. As a result, the LLM generates answers only when it can draw from 
credible sources within the book. In cases where a user's question falls outside the context of the AI Practitioner 
Handbook, the LLM responds with "I don't know" rather than attempting to fabricate a non-factual answer. 
This approach ensures that the generated answers are as accurate and relevant as possible, 
ultimately enhancing the user experience and the usefulness of the Q&A tool.

The AI Practitioner Handbook was first converted from a PDF file into embeddings with OpenAIEmbeddings (OpenAI), 
which cost approximately $0.077 for 91 pages of text content. Using FAISS (Facebook), the embeddings were saved as a vector store for 
efficient similarity search.

## Features

- Input for your OpenAI API key (never saved for security reasons)
- Customizable temperature value for controlling randomness in AI-generated responses
- Option to remember chat history for context-aware responses
- Predefined questions available in a dropdown menu
- Custom question input option
- Displays the AI-generated answer to user questions, the source evidence that were used to generate the answer,
and the chat history used for context (if option is chosen)

## Risks

- Reliance on OpenAI's API: 

  This project heavily depends on OpenAI's API to function, which means that users are at the mercy of any potential changes to the API's cost or availability. If OpenAI decides to change their pricing structure or impose limitations, it could significantly impact the usability and affordability of the script.

- Difficulty in asking questions without prior knowledge of the content: 

  Since users need to provide a specific question to retrieve an answer, it can be challenging to ask meaningful questions if they don't have any prior knowledge of the content. This limitation might make it difficult for users to discover valuable information in the document.

- Potential inaccuracies: 

  The AI may not always provide accurate results, as demonstrated by the example of miscalculating the number of editors. Users should be cautious when relying on the script's answers and might need to verify the information independently.

- Dependence on well-tuned prompt templates: 

  The script relies heavily on the proper tuning of prompt templates to generate meaningful answers. This tuning process can be complex, and it might be possible to miss edge cases or create templates that produce less-than-ideal results. This shortcoming could lead to less accurate or less relevant answers, which may require additional manual intervention or refinement.

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

### 1. Run the Streamlit app from terminal (Local Host Only)

```bash
streamlit run src/main.py
```

### 2. Open the app in your web browser (Local Host Only)

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

The answer to your question will be displayed in the "Answer" tab. The source evidence that are referred to by the AI before
answering are displayed in the "Source" tab. If you have selected "Yes" for chat history, the previous conversations between you and
the AI that were used to generate context-aware answers are displayed in the "Memory" tab.

## Citations
```bash
@book{aisg_aiprac_hbook, author={AISingapore}, title={AIPractitionerHandbook}, howpublished={\url{https://aisingapore.github.io/ai-practitioner-handbook/}}, year={2023}}
```
---

