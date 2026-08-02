
# Задача 1

from pathlib import Path

def total_salary(path):
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    new_lines = text.splitlines()

    if not new_lines:
        return 0, 0

    total_sum = 0
    for line in new_lines:
        if line.strip():
            new_lists = line.split(',')
            total_sum += int(new_lists[1])

    average_salary = total_sum / len(new_lines)
    
    return (total_sum, average_salary)


# Задача 1 покращений варіан з трай ексепт та with open() as file:

def total_salary(path):
    try:
        total_sum = 0
        count = 0

        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    name, salary = line.split(',')
                    total_sum += int(salary)
                    count += 1

        if count == 0:
            return 0, 0

        average_salary = total_sum / count
        return total_sum, average_salary

    except FileNotFoundError:
        print(f"Помилка: Файл '{path}' не знайдено.")
        return 0, 0
    except (ValueError, IndexError):
        print(f"Помилка: Файл '{path}' пошкоджений.")
        return 0, 0

#Задача 2 - про котів

def get_cats_info(path):
    try:
        cats_info = []

        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    cat_id, name, age = line.split(',')
                    cat_dict = {
                        "id": cat_id,
                        "name": name,
                        "age": age
                    }
                    cats_info.append(cat_dict)

        return cats_info

    except (FileNotFoundError):
        print(f"Помилка: Файл '{path}' не знайдено.")
        return []

    except (ValueError, IndexError):
            print(f"Помилка: Файл '{path}' пошкоджений.")
            return []

#Задача 3 - розробка скрипта

import sys
from pathlib import Path
from colorama import Fore, init


init(autoreset=True) # скидаємо автоматично колір після кожного прінт


IGNORE_DIRS = {".venv", "venv", ".git", "__pycache__"} # ігноруємо підпапки для чистоти виводу


def print_directory_tree(path: Path, indent: str = ""):
    """Показує всі папки та файли всередині з кольорами та відступами"""
    try:
        items = list(path.iterdir())
    except PermissionError:
        print(f"{indent}{Fore.RED}[Access Denied]")
        return

    for item in items:

        if item.name in IGNORE_DIRS:
            continue

        if item.is_dir():

            print(f"{indent}{Fore.BLUE}{item.name}/")

            print_directory_tree(item, indent + "    ")
        else:

            print(f"{indent}{Fore.GREEN}{item.name}")


def main():
    if len(sys.argv) < 2:
        print(f"{Fore.RED}Помилка: шлях до директорії не вказаний.")
        print("Використання: python \"Home_work_5.py\" /шлях/до/директорії або постав крапку через пробіл")
        sys.exit(1)

    dir_path = Path(sys.argv[1])

    if not dir_path.exists():
        print(f"{Fore.RED}Помилка: Шлях '{dir_path}' не існує")
        sys.exit(1)

    if not dir_path.is_dir():
        print(f"{Fore.RED}Помилка: Вказаний шлях '{dir_path}' не є директорією!")
        sys.exit(1)

    print(f"{Fore.BLUE}{dir_path.resolve().name}/")
    
    print_directory_tree(dir_path, indent="    ")


if __name__ == "__main__":
    main()


#Задача 4 - CLI бот

def parse_input(user_input):
    """Розбір на команду та аргументи, команда буде приведена до нижнього регістру."""
    if not user_input.strip():
        return "", []
    command, *args = user_input.split()
    command = command.strip().lower()
    return command, args


def add_contact(args, contacts):
    """Додає новий контакт або перезаписує існуючий."""
    if len(args) < 2:
        return "Error: Give me name and phone please."
    name, phone = args[0], args[1]
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    """Змінює номер телефону для існуючого контакту."""
    if len(args) < 2:
        return "Error: Give me name and new phone please."
    name, phone = args[0], args[1]
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."


def show_phone(args, contacts):
    """Виводить номер телефону за ім'ям контакту."""
    if not args:
        return "Error: Enter user name."
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."


def show_all(contacts):
    """Повертає рядок з усіма збереженими контактами."""
    if not contacts:
        return "No contacts saved."
    
    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    return "\n".join(result)


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if not command:
            continue

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()