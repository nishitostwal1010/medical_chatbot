# 🩺 MediBot: A Medical Chatbot Powered by RAG & Gemini

**MediBot** is a medical Q&A chatbot that uses Retrieval-Augmented Generation (RAG) with Google's Gemini models and a local vector database to provide accurate, contextual answers based only on a trusted source document.

---

## 📂 Project Structure

```
.
├── data/
│   └── The_GALE_ENCYCLOPEDIA_of_MEDICINE_SECOND (1).pdf   # Medical knowledge base
├── chroma_db/                                             # Persisted vector DB (generated locally)
├── indexing.ipynb                                         # Indexes the PDF into vector DB
├── rag.ipynb                                              # Sample RAG chain invocation
├── medibot.py                                             # Streamlit chatbot app
├── requirements.txt                                       # Python dependencies
├── .env                                                   # Environment variables (API key)
└── README.md
```

---

## ✨ Features

- 💡 Uses [LangChain](https://docs.langchain.com/) with [Google Generative AI](https://ai.google.dev/) (Gemini models)
- 📚 Context retrieval from `The Gale Encyclopedia of Medicine`
- 🧠 ChromaDB-powered persistent vector store
- 🧾 Clean and instructive prompt design
- 🌐 User-friendly Streamlit interface

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/medibot-rag-chatbot.git
cd medibot-rag-chatbot
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 3. Add Your API Key

Create a `.env` file with:

```env
GOOGLE_API_KEY=your_google_api_key
```

Ensure this file is added to `.gitignore`.

---

## ⚠️ Note on `chroma_db/` Folder

The `chroma_db/` folder is **not included in the repository** because it exceeds GitHub's file size limits.

> 🔄 To generate it locally, simply run:
>
> ```bash
> jupyter notebook indexing.ipynb
> ```
> 
> This will:
> - Load the PDF from `data/`
> - Embed it using `GoogleGenerativeAIEmbeddings`
> - Persist the vector store to `chroma_db/`

---

## 📌 Workflow Overview

### ✅ Step 1: Index the PDF

Run `indexing.ipynb` to:

- Load the PDF from `data/`
- Split it into chunks
- Embed using Gemini embeddings
- Store them in `chroma_db/`

### ✅ Step 2: Test the RAG Chain

Run `rag.ipynb` to:

- Load ChromaDB
- Invoke Gemini via LangChain
- Return accurate responses based on context

### ✅ Step 3: Launch the Chatbot

```bash
streamlit run medibot.py
```

---

## 📦 `requirements.txt`

```txt
streamlit
langchain
langchain-google-genai
langchain-core
langchain-chroma
python-dotenv
PyPDF
```

---

## 📚 Source Document

- 📘 **The Gale Encyclopedia of Medicine**  
  Located in `data/The_GALE_ENCYCLOPEDIA_of_MEDICINE_SECOND (1).pdf`  
  Used as the sole knowledge base for all responses.
