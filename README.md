<h1 align="center">AskMyPDF</h1>
<h2 align="center">Question Answering for AI Practitioner Handbook</h2>

The link to the deployed Streamlit app is: https://meldrickwee-askmypdf-srcmain-1ni4g8.streamlit.app/

TODO: Screen record of using the app

---

This project allows users to ask questions and receive answers based on the AI Practitioner Handbook.
This project was developed in Python 3 with LangChain and deployed with Streamlit.
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
which cost approximately $0.086 for 94 pages of text content. An embedding can be thought of as an information dense
representation of a string of text. The information captured refers to the semantic and syntatic meanings when words are
used to form a coherent sentence. Such embeddings are in the form of a vector of numbers represented in the same
latent space. By residing in the same latent space, the distance between embeddings can be understood as an indication of 
their semantic similarity or dissimilarity. Using Facebook AI Similarity Search (FAISS), developed by Facebook, the 
embeddings were indexed and saved locally as a vector store for efficient similarity search.

The first and most basic implementation of the Q&A task in this project is with the RetrievalQAWithSourcesChain class. 
This class is known as a "chain" which allows for question and answering over an index. The chain takes an input question and 
retrieves the most semantically relevant pieces of text (sources). The chain then passes the question and sources within a 
prompt template into the LLM. The LLM is able to generate a coherent answer for the user.

The second more complex implementation is using the ConversationalRetrievalChain class. The basic workings of this chain is the same
as the first implementation. However, it is interesting that this particular chain allows the LLM the ability to "remember" previous 
questions that were asked by the user. Therefore, the LLM is able to generate context-aware answers based on chat history. 
For example, when the question "What is the job of an AI engineer?" is asked, the LLM may reply "According to the context provided, 
an AI engineer is responsible for building and delivering AI projects on time and on target  by building an effective AI development team.". 
The user can then ask "How does he/she build an effective team?". The LLM is able to be aware that "he/she" is referring to the noun
"AI engineer" asked in the first question when generating its response.

While working on this project, my most significant takeaway involved gaining proficiency in the LangChain framework and recognizing the 
crucial role of prompt templates. LangChain streamlines the substantial engineering effort needed when employing LLMs, 
particularly for targeted business use cases. However, there are still many aspects of LangChain, such as agents, that warrant further 
exploration. The importance of prompt templates is paramount when creating applications with LLMs. A considerable amount of time was 
dedicated to refining the prompt templates to minimize the model's generation of irrelevant or hallucinated responses.

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

- Summarizing discussed content with memory enabled:
   To improve the user experience and provide a comprehensive understanding of the conversation, incorporate a feature that allows the LLM to summarize all the topics discussed so far. With summarization enabled, the LLM can keep track of the conversation history and generate a concise summary upon request, helping users recall important points and maintain context throughout the interaction.

- Utilizing agents for accessing external tools:
   Enhance the capabilities of the LLM by integrating agents that can access external tools and resources. These agents can assist the LLM in gathering relevant information or performing specific tasks beyond its innate knowledge, ultimately providing more accurate and useful answers. For example, an agent could fetch real-time data from an API or interact with a third-party service to offer a more informed response.

- Expanding the knowledge base to AI Singapore's entire website:
   To broaden the scope of the LLM's expertise, extend its knowledge base to encompass not only the AI Practitioner Handbook but also the entirety of AI Singapore's website and its associated resources. By doing so, the LLM can provide more comprehensive and diverse information, ensuring users receive well-rounded support across various AI-related topics.

- Scaling and productionalizing with Pinecone:
   To effectively scale and productionalize the LLM, consider leveraging Pinecone, a managed vector database service that enables fast and scalable similarity search. Pinecone can help optimize the LLM's performance by efficiently managing embeddings and handling large-scale data. With Pinecone, the LLM can deliver fast, accurate, and scalable responses, ensuring a seamless experience for users in a production environment.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/MeldrickWee/AskMyPDF.git
```

### 2. Set up a conda environment "questionanswer" with dependencies installed

```bash
conda create --name questionanswer python=3.9
```

```bash
conda activate questionanswer
```

```bash
pip install requirements.txt
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
Your OpenAI account needs to have a payment method entered or you will run into a rate limit error since every
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

