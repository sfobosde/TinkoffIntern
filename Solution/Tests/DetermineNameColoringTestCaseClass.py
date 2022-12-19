# Класс тест кейсов для задачи корректности раскраски.
class DetermineNameColoringClass:
    count: int
    name: str
    coloring: str
    awaiting_value: int

    def __init__(self, count: int, name: str, coloring: str, awaiting_value: int):
        self.count = count
        self.name = name
        self.coloring = coloring
        self.awaiting_value = awaiting_value