"""
FolderMind Launcher.

Starts the application, performs startup checks,
and opens the browser automatically.
"""

import threading
import time
import webbrowser

import uvicorn

from app.environment import (
    is_ollama_installed,
    is_ollama_running,
    model_exists,
    pull_model,
)
from app.startup import ensure_directories

MODEL = "llama3.2"


def start_server() -> None:
    """
    Start the FastAPI server.
    """
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
    )


def open_browser() -> None:
    """
    Open Swagger UI after the server starts.
    """
    time.sleep(2)

    webbrowser.open(
        "http://127.0.0.1:8000/docs"
    )


def check_environment() -> None:
    """
    Perform all startup checks.
    """

    print("=" * 40)
    print("FolderMind v1.0")
    print("=" * 40)
    print()

    print("Checking environment...")

    ensure_directories()

    print("✓ Data directory")
    print("✓ Chroma directory")
    print("✓ Logs directory")

    if not is_ollama_installed():
        raise RuntimeError(
            "Ollama is not installed.\n"
            "Download it from https://ollama.com/download"
        )

    print("✓ Ollama installed")

    if not is_ollama_running():
        raise RuntimeError(
            "Ollama is installed but not running."
        )

    print("✓ Ollama running")

    if not model_exists(MODEL):
        print(f"Downloading model '{MODEL}'...")

        if not pull_model(MODEL):
            raise RuntimeError(
                f"Failed to download model '{MODEL}'."
            )

    print(f"✓ {MODEL} ready")
    print()


if __name__ == "__main__":

    check_environment()

    print("Starting API...")

    threading.Thread(
        target=open_browser,
        daemon=True,
    ).start()

    start_server()