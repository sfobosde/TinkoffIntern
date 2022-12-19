from Solution.Entities.WordColoringClass import WordColoring

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

def create_coloring_schema(department_name: str, coloring_idea: str) -> []:
    # Разбитие названия на отдельные слова.
    words = department_name.split(' ')

    # Список для хранения схемы раскраски.
    coloring_schema = []

    mistakes_count: int = 0

    for word in words:
        coloring_schema.append(WordColoring(word, coloring_idea[0:len(word)]))
        coloring_idea = coloring_idea[len(word):len(coloring_idea)]

    return coloring_schema


def determine_coloring_mistakes(symbol_count: int, department_name: str, coloring_idea: str) -> int:
    pass
