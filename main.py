from fastapi import FastAPI
from rag_pipeline import ingest_urls, answer_query

app = FastAPI()

# Initial ingestion (you can change URLs)
URLS = [
    "https://example.com"
]

@app.on_event("startup")
def startup_event():
    ingest_urls(URLS)


@app.get("/")
def home():
    return {"message": "RAG Q&A Bot is running"}


@app.get("/ask")
def ask(question: str):
    answer = answer_query(question)
    return {"question": question, "answer": answer}