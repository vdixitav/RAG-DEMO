from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI(
    title="RAG FastAPI Service",
    version="1.0.0",
    description="FastAPI-first RAG system"
)

class QueryRequest(BaseModel):
    question: str

@app.get("/health")
def health():
    return {"status": "ok", "message":"Rag API running"}

@app.post("/query")
def query(request: QueryRequest):
    return{
        "question": request.question,
        "answer":"RAG pipeline not connected yet"
    }     