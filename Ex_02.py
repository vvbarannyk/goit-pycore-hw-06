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