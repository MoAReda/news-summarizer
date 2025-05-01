# News Summarization Application
Fetches news via NewsAPI, creates embeddings with Sentence Transformers, stores them in Chroma, and summarizes with LangChain/Groq.

## Demonstration
Watch a short demonstration video: [Demo Video](https://drive.google.com/file/d/1Uv6ZV1Tmo-e2On9HRrS_u9bGZZewW8EF/view?usp=sharing)

## Prerequisites
- Python 3.9+
- [NewsAPI](https://newsapi.org/register) and [Groq](https://console.groq.com/keys) keys

## Setup
1. Clone repo:
   ```bash
   git clone https://github.com/MoAReda/news-summarizer.git
   cd news-summarizer
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Create .env:
   ```bash
   echo NEWSAPI_KEY=your_key > .env
   echo GROQ_API_KEY=your_key >> .env
4. Run:
   ```bash
   python main.py
