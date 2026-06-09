import os

from langchain.tools import tool


@tool
def create_file(path: str, content: str):
    """
    Создает файл с указанным содержимым
    Args:
        path - путь до файла включая сам файл и его расширение
        content - содержимое которое будет записано в файл
    """

    try:

        os.makedirs(os.path.dirname(path), exist_ok=True)

        with open(path, 'w', encoding='utf-8') as f:
            
            f.write(content)

        return 'Done!'
    
    except Exception as e:

        return f'Error: {e}'