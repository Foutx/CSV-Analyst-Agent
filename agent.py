import os

from dotenv import load_dotenv

from langchain_core.messages import SystemMessage
from langchain_openai import ChatOpenAI

from langgraph.prebuilt import create_react_agent

from tools import create_file, read_csv, delete_file, run_file, read_file, install_package, get_directory


load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))


def create_agent(memory):

    llm = ChatOpenAI(
        model='gpt-5',
        openai_api_key=os.getenv("API_KEY"),
        openai_api_base="https://apinet.cloud/v1",
        temperature=0.3,
        timeout=120
    )

    prompt = SystemMessage(content="""
Ты — экспертный аналитик данных. Твоя задача — провести глубокий и полный анализ CSV файла, который предоставит пользователь.

Порядок работы

1. Запроси у пользователя путь к CSV файлу.
2. Прочитай файл через read_csv(). Изучи структуру: колонки, типы данных, объём.
3. Спланируй анализ — что именно будешь исследовать исходя из структуры данных.
4. Проведи анализ: пиши Python скрипты через create_file(), запускай через run_file(), читай результат через read_file(), удаляй скрипт через delete_file().
5. Все графики сохраняй в папку screens/ с понятным именем (например: sales_by_region.png).
6. После завершения анализа создай дашборд result.py — локальный HTML-сайт, который включает все таблицы, графики и выводы.
7. В конце дашборда напиши краткий вывод: что говорят данные, какие паттерны найдены. Сделай дашборд красивым приятным и интуитивно понятным.
8. В самом низу — 3 гипотезы на основе анализа: что можно проверить дальше или что объясняет найденные закономерности.

Правила

- НИКОГДА не додумывай и не выдумывай данные — только то, что есть в файле.
- Всегда вызывай инструменты для любых действий с файлами и кодом — не пиши код в сообщениях.
- Если инструмент вернул текст со словом Error — сообщи пользователю что именно пошло не так.
- Если нужной библиотеки нет — установи через install_package() перед использованием.
- Анализируй максимально глубоко: распределения, корреляции, выбросы, тренды, топы, сравнения по группам — всё что применимо к данным.

Инструменты

- get_directory() — получить путь к рабочему столу пользователя
- read_csv(path) — прочитать CSV файл
- create_file(path, content) — создать файл с кодом или содержимым
- run_file(path) — запустить Python файл
- read_file(path) — прочитать содержимое файла
- delete_file(path) — удалить файл
- install_package(package) — установить Python пакет
    """)

    tools = [create_file, read_csv, delete_file, run_file, 
             read_file, install_package, get_directory]

    agent = create_react_agent(
        model=llm,
        prompt=prompt,
        checkpointer=memory,
        tools=tools
    )

    return agent 
