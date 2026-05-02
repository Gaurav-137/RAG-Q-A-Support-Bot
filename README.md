# RAG Q&A Support Bot

## Overview
This project implements a Retrieval-Augmented Generation (RAG) pipeline:
- Crawl website content
- Chunk text
- Generate embeddings
- Store in FAISS vector database
- Retrieve relevant chunks
- Generate answers using LLM

## Tech Stack
- Python
- FastAPI
- FAISS
- OpenAI API

## Setup

1. Clone repo
2. Create virtual environment
3. Install dependencies:

pip install -r requirements.txt

4. Set API key:

export OPENAI_API_KEY=your_key_here

## Run

uvicorn main:app --reload

## API Usage

GET /ask?question=your_question

Example:
curl "http://127.0.0.1:8000/ask?question=What is this site about?"

## Notes
- Answers are generated only from crawled content
- If answer is not found → returns "I don't know"