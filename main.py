import sqlite3

from langgraph.checkpoint.sqlite import SqliteSaver

from langchain_core.messages import HumanMessage

from agent import create_agent


DB_PATH = "memory.db"


def get_projects():

    try:

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.execute("SELECT DISTINCT thread_id FROM checkpoints")

        projects = [row[0] for row in cursor.fetchall()]

        conn.close()
        
        return projects
    
    except:

        return []
    

def select_project():

    projects = get_projects()

    if projects:

        print('Список проектов:')

        for i, project in enumerate(projects):

            print(f'{i}:     {project}')

        print()

    name = input("Название проекта (Enter = новый): ").strip()

    if not name:

        name = input("Введите название нового проекта: ").strip()

    return name


def main():

    project = select_project()

    with SqliteSaver.from_conn_string(DB_PATH) as memory:

        agent = create_agent(memory)

        config = {"configurable": {"thread_id": project}}

        while True:

            user_input = input("You: ")

            if user_input.lower() in ["exit", "quit", "выход"]:
                return
 
            if not user_input.strip():
                continue

            response = agent.invoke({"messages":
                                     [HumanMessage(content=user_input)]
                                     }, config)
            
            messages = response['messages']

            print(f'CSV Analyzer: {messages[-1].content}')


        
if __name__ == '__main__':
    main()