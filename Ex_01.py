
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

