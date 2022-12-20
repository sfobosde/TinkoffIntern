from unittest import TestCase
from Solution.mathLotary import find_min_lcm_pair


class MathLotteryTest(TestCase):
    def test_find_min_lcm_pair(self):
        self.assertEqual((1, 2), find_min_lcm_pair(3))
        self.assertEqual((3, 3), find_min_lcm_pair(6))
        self.assertEqual((3, 6), find_min_lcm_pair(9))
