# Автоматическое тестировние для раскрашивания логотипа.
from unittest import TestCase
import Solution.DetermineNameColor as detMistakes
from Solution.Tests.DetermineNameColoringTestCaseClass import DetermineNameColoringClass as TestCaseClass
import Solution.DetermineNameColor as detMistakes

class TestDetermineColoring(TestCase):
    # Тест кейсы.
    test_data = [TestCaseClass(7, "Tinkoff", "BYBYBYB", 0),
                 TestCaseClass(27, "Algorithms and Data Structures", "BBBBBBBBBBBYBYYYYBBBBBBBBBB", 3)]

    def test_split(self):
        with self.assertRaises(Exception):
            for test_case in self.test_data:
                test_case.name.split('a')

    def test_determine_coloring_mistakes(self):
        for test_case in self.test_data:
            self.assertEqual(
                test_case.awaiting_value,
                detMistakes.determine_coloring_mistakes(test_case.count, test_case.name, test_case.coloring))
