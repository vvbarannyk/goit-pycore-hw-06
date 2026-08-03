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
        print("Використання: python \"Ex_03.py\" /шлях/до/директорії або постав крапку через пробіл")
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