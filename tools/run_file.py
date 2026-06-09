import sys

import os

import subprocess

from langchain.tools import tool


@tool
def run_file(path: str):
    """
    Запускает файл по указанной директории
    Args:
        path - путь до файла
    """
    
    result = subprocess.run(
        [sys.executable, path],
        capture_output=True,
        text=True,
        encoding='utf-8',
        errors='replace',
        env={**os.environ, 'PYTHONIOENCODING': 'utf-8'}
    )

    if result.stderr:

        return f"Error: {result.stderr}"

    return f"Success: {result.stdout}"