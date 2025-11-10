# JobGenie Backend

A FastAPI backend service for **JobGenie**, an AI-powered cover letter generator and job application assistant. It integrates with Hugging Face and OpenAI-compatible models to generate professional cover letters.

---

## Features

- Generate professional cover letters from a **CV** and **job description**.
- Support for multiple AI models (Hugging Face, OpenAI API compatible).
- Handles PDF CVs for automatic extraction.
- Exposes a **REST API** for frontend integration.

---

## Requirements

- Python 3.10+
- `fastapi`
- `uvicorn`
- `openai` (or `huggingface_hub` if using Hugging Face API)
- `python-dotenv` (optional, for managing environment variables)
- `selenium` (optional, for job board automation)

---

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/jobgenie-backend.git
cd jobgenie-backend

```

# Create and activate a virtual environment:

python -m venv venv

# Windows

venv\Scripts\activate

# macOS/Linux

source venv/bin/activate

# Install dependencies:

pip install -r requirements.txt

# Set environment variables:

# Create a .env file or export directly

HF_TOKEN=your_huggingface_api_token

# Start the API server

uvicorn app.main:app --reload
