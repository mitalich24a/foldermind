"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Environment checks.
"""

from __future__ import annotations

import shutil
import subprocess


def is_ollama_installed() -> bool:
    """
    Returns True if Ollama is installed.
    """
    return shutil.which("ollama") is not None


def is_ollama_running() -> bool:
    """
    Returns True if the Ollama server is running.
    """
    if not is_ollama_installed():
        return False

    try:
        result = subprocess.run(
            ["ollama", "list"],
            capture_output=True,
            text=True,
            timeout=5,
        )

        return result.returncode == 0

    except (
        subprocess.SubprocessError,
        FileNotFoundError,
        OSError,
    ):
        return False


def model_exists(model: str) -> bool:
    """
    Returns True if the specified model exists locally.
    """
    if not is_ollama_running():
        return False

    try:
        result = subprocess.run(
            ["ollama", "list"],
            capture_output=True,
            text=True,
            timeout=5,
        )

        if result.returncode != 0:
            return False

        return model.lower() in result.stdout.lower()

    except (
        subprocess.SubprocessError,
        FileNotFoundError,
        OSError,
    ):
        return False


def pull_model(model: str) -> bool:
    """
    Downloads the specified model.
    """
    if not is_ollama_installed():
        return False

    try:
        result = subprocess.run(
            ["ollama", "pull", model],
            check=False,
        )

        return result.returncode == 0

    except (
        subprocess.SubprocessError,
        FileNotFoundError,
        OSError,
    ):
        return False


def check_environment(model: str) -> None:
    """
    Performs all startup checks.
    Raises RuntimeError if a requirement is not met.
    """

    print("Checking environment...\n")

    if not is_ollama_installed():
        raise RuntimeError(
            "Ollama is not installed.\n"
            "Download it from https://ollama.com/download"
        )

    print("✓ Ollama installed")

    if not is_ollama_running():
        raise RuntimeError(
            "Ollama is installed but is not running."
        )

    print("✓ Ollama running")

    if not model_exists(model):
        print(f"Downloading model '{model}'...\n")

        if not pull_model(model):
            raise RuntimeError(
                f"Failed to download model '{model}'."
            )

    print(f"✓ Model '{model}' available\n")