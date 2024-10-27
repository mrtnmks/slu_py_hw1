def add_task(task1):
    with open('todo.txt', 'a') as file:
        file.write(task1 + '\n')

def read_tasks():
    try:
        with open('todo.txt', 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        return []

while True:
    print("")
    print("1. Přidat úkol")
    print("2. Zobrazit úkoly")
    print("3. Ukončení programu")
    choice = input("Vyber možnost: ")
    if choice == '1':
        task = input("Zadej úkol: ")
        add_task(task)
        print("Úkol byl přidán.")
    elif choice == '2':
        tasks = read_tasks()
        print("\nSeznam úkolů:")
        for task in tasks:
            print(task.strip())
    elif choice == '3':
        break
    else:
        print("Neplatný vstup.")