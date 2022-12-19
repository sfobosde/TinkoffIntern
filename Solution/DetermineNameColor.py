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
        raise Exception("Ошибка вводимых данных, надо вводить целые числа")
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


# Поиск ошибок в раскраске.
def determine_coloring_mistakes(symbol_count: int, department_name: str, coloring_idea: str) -> int:
    mistakes_count: int = 0

    coloring_schemas = create_coloring_schema(department_name, coloring_idea)

    for coloring_chema in coloring_schemas:
        if (coloring_chema.coloring.find("BB") > -1) or (coloring_chema.coloring.find("YY") > -1):
            mistakes_count += 1
    return mistakes_count

print(determine_coloring_mistakes(7, "Tinkoff", "BYBYBYB"))