# Класс для хранения раскрасок слова.
class WordColoring:
    word: str
    coloring: str

    def __init__(self, word: str, coloring: str):
        if len(word) == len(coloring):
            self.word = word
            self.coloring = coloring
        else:
            raise Exception(f"Количество раскрашеных букв не соответсвует количеству букв в слове."
                            f"{word} {len(word)} "
                            f"{coloring} {len(coloring)}")