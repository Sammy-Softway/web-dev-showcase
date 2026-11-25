import os

import  requests
from dotenv import load_dotenv


load_dotenv()

def get_required_env(key: str) -> str:
    value = os.getenv(key)
    if not value:
        raise ValueError(f"Required environment variable '{key}' is missing or empty.")
    return value

ELEVENLABS_API_KEY = get_required_env("ELEVENLABS_API_KEY")
BASE_URL = get_required_env("BASE_URL")
DEFAULT_VOICE_ID = get_required_env("DEFAULT_VOICE_ID")


def text_to_speech_bytes(text: str, voice_id: str = DEFAULT_VOICE_ID) -> bytes:
    if not text.strip():
        raise ValueError("Input text cannot be empty.")

    url = f"{BASE_URL.rstrip('/')}/{voice_id}"
    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json",
    }
    payload = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"ElevenLabs API request failed: {e}") from e

    return response.content
