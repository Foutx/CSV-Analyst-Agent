from langchain.tools import tool

import pandas as pd


@tool
def read_csv(path: str) -> str:
    """
    Читает CSV файл и возвращает его содержимое в виде текста
    Args:
        path - путь к CSV файлу
    """

    try:

        df = pd.read_csv(path)
        
        return df.to_string()
    
    except Exception as e:

        return f"Error: \n{e}"