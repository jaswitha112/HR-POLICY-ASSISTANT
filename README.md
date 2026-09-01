# 🤖 HR Policy Assistant

🚀 **Live Demo:** [HR Policy Assistant] (https://hr-policy-assistant-vhau.onrender.com)

A lightweight Retrieval-Augmented Generation (RAG) application for answering employee questions from an internal HR policy document. The project combines a local policy corpus, embeddings, semantic retrieval, and an LLM-powered agent to provide grounded answers instead of relying on memory alone.

## 🎯 Why this project?

Organizations often store policies in long documents such as employee handbooks, onboarding guides, and internal policy PDFs. Searching these documents manually is time-consuming and error-prone. This project demonstrates how to build a simple but effective HR assistant that:

- reads and splits a policy document into searchable chunks
- converts chunks into vector embeddings
- retrieves the most relevant policy passages
- uses a language model to answer based only on retrieved evidence
- exposes the assistant through a CLI or a Streamlit web app
  
## ✨ Features

- HR policy Q&A using RAG
- FAISS vector search for fast retrieval
- Jina embeddings for semantic matching
- Groq-hosted LLM support
- LangChain agent workflow with tool-based retrieval
- Streamlit UI for interactive conversations
- Persistent FAISS index to avoid reindexing on every run
- Easy setup using environment variables and a Python virtual environment

## 🛠️ Tech Stack

- Python 3.11
- LangChain and LangChain Community
- Groq LLM provider
- Jina Embeddings
- FAISS for vector storage and retrieval
- Streamlit for the web interface
- Python-dotenv for environment configuration
- FAISS local index stored in the project data directory
  
## 🏗️ Architecture

The project follows a standard RAG pattern:

1. Document ingestion
   - The HR policy text file is loaded from the data folder.

2. Chunking
   - The document is divided into smaller text chunks with overlap to retain nearby context.

3. Embedding generation
   - Each chunk is converted into vectors using Jina embeddings.

4. Vector storage
   - The embeddings are stored in a FAISS index for fast similarity search.

5. Retrieval
   - A retriever fetches the top matching chunks for the user question.

6. Agent reasoning
   - A LangChain agent passes the retrieved context to an LLM and answers using the search results as evidence.

7. User interface
   - The assistant can be used through the terminal demo or a Streamlit chat app.

A simple view of the flow looks like this:

```text
HR policy text file
        ↓
Document loader
        ↓
Text splitter
        ↓
Embedding model
        ↓
FAISS vector store
        ↓
Retriever
        ↓
LangChain agent + LLM
        ↓
Answer to the user
```

## 📁 Project Structure

```text
HR-POLICY-ASSISTANT/
├── app.py                     # Streamlit web app
├── main.py                    # CLI demo entry point
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
├── LICENSE                    # MIT license
├── data/
│   ├── hr_policy.txt          # Source HR policy content
│   └── faiss_index/           # Saved FAISS index files
├── hr_assistant/
│   ├── __init__.py
│   ├── agent.py               # LangChain agent setup
│   ├── config.py              # App configuration and environment variables
│   ├── document_loader.py     # Loads raw policy text
│   ├── embeddings.py          # Jina embedding model wrapper
│   ├── llm.py                 # LLM setup
│   ├── pipeline.py            # Main orchestration for the assistant
│   ├── splitter.py            # Chunking logic
│   ├── tools.py               # Retrieval tool used by the agent
│   └── vector_store.py        # FAISS build/save/load logic
└── ragenv/                    # Local virtual environment
```

## 🚀 Getting Started

### 📋 Prerequisites

- Python 3.11+
- A Groq API key
- A Jina API key
- Git

### 1️⃣ Clone the repository

```bash
git clone https://github.com/jaswitha112/HR-POLICY-ASSISTANT.git
cd HR-POLICY-ASSISTANT
```

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
```

On Windows:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure environment variables

Create a `.env` file in the project root with the following values:

```env
GROQ_API_KEY=your_groq_api_key
JINA_API_KEY=your_jina_api_key
```

The app loads these automatically from the environment using `python-dotenv`.

### 5️⃣ Run the project

#### 💻 CLI demo

```bash
python main.py
```

This runs a few example HR questions and prints the assistant responses.

####  🌐 Streamlit app

```bash
streamlit run app.py
```

Then open the local URL shown in the terminal and ask policy-related questions in the browser.

## 💡 Usage Example

Example questions you can ask:

- How many paid leave days do I get?
- What is the notice period during probation?
- Can I work from home every day?
- What are the employee reimbursement rules?

## 📝 Notes

- The first run may take longer because the vector store is being built from the policy file.
- The generated FAISS index is stored in `data/faiss_index/` so future runs can load it quickly.
- The assistant is designed to answer from retrieved policy evidence and avoid guessing when the information is not present.

## 📜 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## 🤝 Contributing

Contributions are welcome. If you want to improve the assistant, add new features, or make the retrieval pipeline more robust, feel free to open a pull request with a clear description of the change.

## 🙏 Acknowledgements

- LangChain for orchestration and agent tooling
- Groq for LLM inference
- Jina for embedding models
- FAISS for vector similarity search
- Streamlit for the interactive interface
