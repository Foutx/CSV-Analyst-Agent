from langchain.tools import tool


@tool
def read_file(path: str):
    """
    Возвращает содержимое файла
    Args:
        path - путь до файла
    """
    
    try:

        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()

        return content
    
    except Exception as e:

        return f'Error: {e}'