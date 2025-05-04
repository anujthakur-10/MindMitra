# MindMitra - Mental Health Support Chatbot

## Frontend (HTML + Tailwind CSS + Firebase Auth)

- Landing Page: `index.html`
- Login/Signup Page: `login.html`
- Chat Interface: `chat.html`
- About Page:`about.html`
- Firebase Authentication (Email/Password, Google, Guest)

## Backend (Python + FastAPI)

- Chat API using Google Gemini 2.0 Flash
- `/chat` POST endpoint for conversation

## Setup Instructions

1. Clone the repo or download files.

2. Frontend:
   - Update `firebase-config.js` with your Firebase project settings.

3. Backend:
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```
   - Run server:
     ```bash
     uvicorn main:app --reload
     ```

4. Open `frontend/index.html` and start using MindMitra!

## Notes
- Frontend and Backend must run on same machine (for now localhost).
- Connect backend server URL properly if hosting.

---
