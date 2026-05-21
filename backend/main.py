from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "2Care Voice AI Agent Backend Running Successfully"
    }