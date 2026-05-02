from crawler import fetch_page, chunk_text
from embeddings import get_embedding
from vector_store import VectorStore
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

vector_store = VectorStore()

def ingest_urls(urls):
    all_chunks = []

    for url in urls:
        text = fetch_page(url)
        chunks = chunk_text(text)
        all_chunks.extend(chunks)

    embeddings = [get_embedding(chunk) for chunk in all_chunks]

    vector_store.add(embeddings, all_chunks)


def retrieve_context(query, k=3):
    query_embedding = get_embedding(query)
    return vector_store.search(query_embedding, k)


def generate_answer(query, context_chunks):
    context = "\n\n".join(context_chunks)

    prompt = f"""
You are a support assistant.

Answer ONLY from the context below.
If the answer is not present, say "I don't know".

Context:
{context}

Question:
{query}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


def answer_query(query):
    context = retrieve_context(query)
    return generate_answer(query, context)