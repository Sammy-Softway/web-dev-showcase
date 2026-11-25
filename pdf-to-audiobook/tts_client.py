import os

import  requests
from dotenv import load_dotenv
from pathlib import Path


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

def save_audio_chunks(audio_chunks: list[bytes], output_path: str | Path) -> Path:
    """Combine MP3 byte chunks and save them to a local .mp3 file."""
    if not audio_chunks:
        raise ValueError("Input audio chunks cannot be empty.")

    path = Path(output_path)
    if path.suffix.lower() != ".mp3":
        path = path.with_suffix(".mp3")

    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("wb") as audio_file:
            for chunk in audio_chunks:
                audio_file.write(chunk)
    except OSError as e:
        raise RuntimeError(f"Failed to save audio file to '{path}': {e}") from e

    if path.stat().st_size == 0:
        raise ValueError("Written audio file is empty.")

    return path
