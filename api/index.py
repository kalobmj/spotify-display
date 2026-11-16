from fastapi import FastAPI
import os
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
redirect_uri = os.getenv("SPOTIFY_REDIRECT_URI")

app = FastAPI()

@app.get("/")
@app.get("/")
def home():
    return {
        "message": "Spotify backend is running!",
        "credentials_loaded": bool(client_id and client_secret and redirect_uri)
    }