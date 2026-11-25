from pathlib import Path

from pdf_handler import extract_text_from_pdf, clean_text, chunk_text
from tts_client import text_to_speech_bytes, save_audio_chunks


def main() -> None:
    pdf_path = input("Enter path to PDF file: ").strip().strip('"')
    audio_filename = Path(pdf_path).stem
    output_path = Path("output") / f"{audio_filename}.mp3"

    raw_text = extract_text_from_pdf(pdf_path)
    cleaned_text = clean_text(raw_text)
    text_chunks = chunk_text(cleaned_text)

    print(f"Found {len(cleaned_text):,} characters across {len(text_chunks)} chunk(s).")
    confirm = input("Proceed with text-to-speech conversion? (y/n): ").strip().lower()
    if confirm != "y":
        print("Conversion cancelled.")
        return

    audio_chunks = []
    for i, chunk in enumerate(text_chunks, start=1):
        print(f"Converting chunk {i}/{len(text_chunks)}...")
        audio_chunks.append(text_to_speech_bytes(chunk))

    saved_file = save_audio_chunks(audio_chunks, output_path)
    print(f"Success! Audiobook saved to: {saved_file}")

if __name__ == "__main__":
    try:
        main()
    except (FileNotFoundError, ValueError, RuntimeError) as e:
        print(f"\nError: {e}")