# PDF to Audiobook Converter

A modular Python CLI application that extracts text from PDF documents, processes and splits long content at word boundaries, and converts it into natural-sounding MP3 audiobooks using the **ElevenLabs Text-to-Speech API**.

---

## Engineering Highlights

* **Separation of Concerns:** Cleanly decoupled into dedicated modules for PDF processing (`pdf_handler.py`), API communication and binary audio persistence (`tts_client.py`), and user workflow orchestration (`main.py`).
* **Defensive Input Validation:** Validates file existence, extensions, corruption (`PdfReadError`), encryption, and scanned/image-only PDFs before making any external API requests.
* **Word-Aware Text Chunking:** Normalizes irregular PDF whitespace and splits long documents into API-safe chunks (`<= 4,500` characters) without cutting words in half.
* **API Resilience & Cost Guardrails:** Enforces request timeouts, chains HTTP/network exceptions cleanly, displays total character/chunk counts, and requires user confirmation before consuming API credits.
* **Flexible File Selection:** Supports both a native OS file-picker dialog (`tkinter.filedialog`) and manual file path input in the terminal.

---

## Project Structure

```text
pdf-to-audiobook/
├── main.py             # CLI entry point, user prompts, and workflow orchestration
├── pdf_handler.py      # PDF validation, text extraction, normalization, and chunking
├── tts_client.py       # ElevenLabs REST API client and binary MP3 export
├── requirements.txt    # Direct project dependencies
├── .env.example        # Environment variable template
└── README.md           # Project documentation
```

---

## Prerequisites

* **Python 3.10+**
* A free or paid **ElevenLabs API Key** (create one at [ElevenLabs Settings](https://elevenlabs.io))

---

## Setup & Installation

1. **Navigate to the project directory:**
   ```bash
   cd pdf-to-audiobook
   ```

2. **Create and activate a virtual environment (recommended):**
   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # macOS/Linux:
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   Copy `.env.example` to `.env` and add your ElevenLabs API key:
   ```bash
   cp .env.example .env
   ```
   Update `.env`:
   ```env
   ELEVENLABS_API_KEY=your_actual_api_key_here
   BASE_URL=https://elevenlabs.io
   DEFAULT_VOICE_ID=JBFqnCBsd6RMkjVDRZzb
   ```

---

## Usage

Run the application from your terminal:

```bash
python main.py
```

1. Choose **Option 1** to browse for a `.pdf` file using the native file dialog, or **Option 2** to paste a file path directly.
2. Review the extracted character and chunk count summary.
3. Enter `y` to confirm and start generating audio.
4. Your combined audiobook is saved automatically to `output/<pdf_filename>.mp3`.

---

## Tech Stack

* **[pypdf](https://readthedocs.io):** Pure-Python PDF parsing and text extraction
* **[Requests](https://readthedocs.io):** REST API communication and HTTP error handling
* **[python-dotenv](https://saurabh-kumar.com):** Secure environment variable management
* **[ElevenLabs Text-to-Speech API](https://elevenlabs.io):** Neural voice synthesis (`eleven_flash_v2_5`)



## Project Reflection

### 1. What was easy?
**Answer:**  
Breaking the project down into logical stages before writing any code felt very natural. Once the core modules (`pdf_handler.py` and `tts_client.py`) were cleanly separated, wiring everything together inside `main.py` and adding user-friendly touches—like the credit-saving confirmation prompt and the file-picker dialog—came together smoothly.

### 2. What was hard?
**Answer:**  
Reading external API documentation and translating it directly into working Python code was the toughest part at first. Understanding how `cURL` examples map to `requests.post` headers and payloads, writing the word-boundary chunking math from scratch, and handling binary audio bytes (`bytes` vs. `str`) took real patience and trial-and-error to fully grasp.

### 3. How I might improve for the next project? / What I would do differently?
**Answer:**  
Next time, I will design the user experience upfront rather than realizing mid-testing that a file-picker dialog feels much better than pasting file paths into the terminal. I would also write automated unit tests (`pytest`) for my text-chunking and validation edge cases instead of relying solely on manual testing, and avoid over-engineering stateless logic into classes when simple, focused functions do the job better.

### 4. What was my biggest learning from today?
**Answer:**  
I learned how to read documentation surgically instead of feeling overwhelmed by it—focusing on the core entry points, required headers/payloads, and failure modes. More importantly, I saw firsthand why separation of concerns matters: because my PDF extraction and API logic were completely decoupled from the UI, I was able to upgrade how users select files in `main.py` without touching a single line of backend code.
