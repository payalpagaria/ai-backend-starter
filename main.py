from fastapi import FastAPI
from pydantic import BaseModel
import os 
from dotenv import load_dotenv

load_dotenv()
app=FastAPI(title="My ai backend")


class ChatRequest(BaseModel):
     message: str
    
@app.get("/")
def health():
     return {"status":"App is running"}

@app.post("/chat")
def chat(request:ChatRequest):
     return {"response":f"You said: {request.message}"}