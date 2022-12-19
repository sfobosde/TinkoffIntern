# Автоматическое тестировние для раскрашивания логотипа.
from unittest import TestCase
import Solution.DetermineNameColor as detMistakes


class TestDetermineColoring(TestCase):
    def test_determine_coloring_mistakes(self):
        self.assertEqual(0, detMistakes.determine_coloring_mistakes(
            7,
            "Tinkoff",
            "BYBYBYB"))

        self.assertEqual(3, detMistakes.determine_coloring_mistakes(
            27,
            "Algorithms and Data Structures",
            "BBBBBBBBBBBYBYYYYBBBBBBBBBB"))
