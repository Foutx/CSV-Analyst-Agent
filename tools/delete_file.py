import os

from langchain.tools import tool


@tool
def delete_file(path: str):
    """
    Удаляет файл по указанному пути
    Args:
        path - путь до файла который нужно удалить
    """

    try:

        os.remove(path)

        return 'Done!'

    except Exception as e:

        return f'Error: {e}'
