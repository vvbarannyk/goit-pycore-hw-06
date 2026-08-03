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