# Ввод текста.
def inputData():
    # Количество символов в названии отдела.
    symbol_count: int

    # Название отдела.
    department_name: str

    # Идея раскраски.
    coloring_idea: str

    try:
        symbol_count = int(input("Введите количество букв в названии отдела:"))
    except ValueError:
        print("Необходимо ввести число.")

    department_name = input("Введите название отдела:")

    coloring_idea = input("Введите идею раскраски:")