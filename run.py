import subprocess
import sys
import os

def start_backend():
    # Navigate to the backend directory and start the FastAPI server
    backend_path = os.path.join(os.getcwd(), 'backend')
    subprocess.Popen([sys.executable, '-m', 'uvicorn', 'main:app', '--reload'], cwd=backend_path)

def start_frontend():
    # Navigate to the frontend directory and start a simple HTTP server
    frontend_path = os.path.join(os.getcwd(), 'frontend')
    subprocess.Popen([sys.executable, '-m', 'http.server', '5500'], cwd=frontend_path)

if __name__ == '__main__':
    start_backend()
    start_frontend()
    print("🚀 Both servers are running:")
    print("🔹 Backend: http://127.0.0.1:8000")
    print("🔹 Frontend: http://127.0.0.1:5500")
