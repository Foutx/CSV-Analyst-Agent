import sys

import subprocess

from langchain.tools import tool


@tool
def install_package(package: str):
    """
    Устанавливает Python пакет через pip
    Args:
        package - название пакета который нужно установить
    """

    try:

        result = subprocess.run(
            [sys.executable, '-m', 'pip', 'install', package],
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='replace'
        )

        if result.returncode != 0:

            return f'Error: {result.stderr}'

        return 'Done!'

    except Exception as e:

        return f'Error: {e}'
