import os

from langchain.tools import tool


@tool
def get_directory():

    """Возвращает путь до рабочего стола пользователя."""
    
    return os.path.join(os.path.expanduser("~"), "Desktop")