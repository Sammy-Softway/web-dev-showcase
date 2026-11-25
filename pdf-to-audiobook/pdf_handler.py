from pathlib import Path
import re
from pypdf import PdfReader
from pypdf.errors import PdfReadError


def extract_text_from_pdf(file_path: str | Path) -> str:
    """Validate a PDF file and extract all readable text across its pages."""
    path = Path(file_path)

    if not path.is_file():
        raise FileNotFoundError(f"File not found: {path}")
    if path.suffix.lower() != ".pdf":
        raise ValueError(f"Expected a .pdf file, got '{path.name}'")

    try:
        reader = PdfReader(path)
    except (ValueError, PdfReadError) as e:
        raise ValueError(f"Corrupted or unreadable PDF: {e}") from e

    if reader.is_encrypted:
        raise ValueError("Encrypted PDFs are not supported.")

    pages_text = [page.extract_text() or "" for page in reader.pages]
    return "\n".join(pages_text)


def clean_text(raw_text: str) -> str:
    """Normalize whitespace and verify that extractable text exists."""
    cleaned = re.sub(r"\s+", " ", raw_text).strip()
    if not cleaned:
        raise ValueError("No extractable text found (PDF may be scanned or image-only).")
    return cleaned


def chunk_text(text: str, max_chars: int = 4500) -> list[str]:
    """Split text into chunks under max_chars without cutting words in half."""
    if max_chars <= 0:
        raise ValueError("max_chars must be a positive integer.")

    words = text.split(" ")
    chunks: list[str] = []
    current_chunk: list[str] = []
    current_length = 0

    for word in words:
        if len(word) > max_chars:
            raise ValueError(f"Single word exceeds max_chars limit ({max_chars}).")

        # +1 accounts for the space separator if current_chunk already has words
        space_needed = 1 if current_chunk else 0

        if current_length + len(word) + space_needed <= max_chars:
            current_chunk.append(word)
            current_length += len(word) + space_needed
        else:
            chunks.append(" ".join(current_chunk))
            current_chunk = [word]
            current_length = len(word)

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks
