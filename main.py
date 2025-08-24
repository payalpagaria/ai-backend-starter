from fastapi import FastAPI
from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI(title="My AI Backend")

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def health_check():
    return {"status": "AI Backend is running!"}

@app.post("/chat")
def chat(request: ChatRequest):
    return {"response": f"You said: {request.message}"}

# Add this for Railway
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)