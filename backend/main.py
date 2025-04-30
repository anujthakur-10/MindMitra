from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import google.generativeai as genai

app = FastAPI()

# CORS
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# ✅ Global model instance
genai.configure(api_key="AIzaSyA1K8iJHzi9mID_x43wXCsfQR5PlxRWjME")
model = genai.GenerativeModel('gemini-2.0-flash')

# Pydantic model
class ChatRequest(BaseModel):
    message: str

# Chat endpoint
@app.post("/chat")
async def chat(req: ChatRequest):
    # Use Gemini API to generate content
    response = model.generate_content(
        f"You are a helpful and friendly mental health support chatbot called MindMitra.\nUser: {req.message}\nAssistant:"
    )
    reply = response.text
    return {"reply": reply}
