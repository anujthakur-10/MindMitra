from fastapi import FastAPI, Request
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

# Configure Gemini API
genai.configure(api_key="AIzaSyA1K8iJHzi9mID_x43wXCsfQR5PlxRWjME")
model = genai.GenerativeModel('gemini-2.0-flash')

# ---- Configurations ----

CRITICAL_KEYWORDS = {"suicide", "die", "kill myself", "end my life", "worthless", "hopeless", "no way out", "can't live"}
HELPLINES_INDIA = [
    {"name": "iCall", "number": "+91-9152987821"},
    {"name": "Vandrevala Foundation", "number": "1860-266-2345"},
]

# GOOGLE_PLACES_API_KEY = "YOUR_GOOGLE_MAPS_API_KEY"  # Optional for therapist suggestions

# ---- Pydantic Request ----

class ChatRequest(BaseModel):
    message: str
    location: str = None  # Optional, for therapist lookup

# ---- Keyword Detection ----

def detect_critical_keywords(text: str) -> bool:
    text = text.lower()
    return any(kw in text for kw in CRITICAL_KEYWORDS)

# ---- Therapist Search ----

# def get_nearby_therapists(location: str):
#     try:
#         url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query=mental+health+therapist+near+{location}&key={GOOGLE_PLACES_API_KEY}"
#         response = requests.get(url).json()
#         results = response.get("results", [])
#         return [{
#             "name": r["name"],
#             "address": r["formatted_address"]
#         } for r in results[:3]]
#     except Exception as e:
#         return []

# ---- Main Chat Endpoint ----

@app.post("/chat")
async def chat(req: ChatRequest):
    if detect_critical_keywords(req.message):
         # Create a more structured prompt for crisis situations
        crisis_prompt = """You are MindMitra, a mental health support chatbot specifically serving users in India. 
        When responding to crisis situations, DO NOT suggest international helplines. 
        Instead, respond with empathy and encourage the user to use these specific Indian helplines:
        - iCall: +91-9152987821
        - Vandrevala Foundation: 1860-266-2345
        
        User: {message}
        Assistant:"""
        
        gemini_response = model.generate_content(crisis_prompt.format(message=req.message))
        reply = gemini_response.text
        
        return {
            "reply": reply,
            "helplines": HELPLINES_INDIA
        }

        # Optional therapist suggestion
        # if req.location:
        #     response["therapists"] = get_nearby_therapists(req.location)
        # return response

    # If no critical keywords, proceed with Gemini response
    gemini_response = model.generate_content(
        f"You are a helpful and friendly mental health support chatbot called MindMitra.\nUser: {req.message}\nAssistant:"
    )
    reply = gemini_response.text

    return {"reply": reply}
