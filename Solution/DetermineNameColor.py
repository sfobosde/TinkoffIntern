# Ввод текста.
def input_data():
    # Symbol count.
    symbol_count: int

    # Название отдела.
    department_name: str

    # Идея раскраски.
    coloring_idea: str

    # Контроль ввода и обработка исключения.
    # Используется проброска исключений.
    try:
        symbol_count = int(input("Введите количество букв в названии отдела:"))
    except ValueError:
        print("Необходимо ввести число.")
        raise Exception("Ошибка вводимых данных")
    except TypeError:
        print("Необходимо ввести целое число.")
        raise Exception("Ошибка вводимых данных")

    department_name = input("Введите название отдела:")

    coloring_idea = input("Введите идею раскраски:")

    return symbol_count, department_name, coloring_idea


def determine_coloring_mistakes(symbol_count: int, department_name: str, coloring_idea: str) -> int:
    pass
