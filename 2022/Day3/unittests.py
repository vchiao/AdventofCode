from main import *
import unittest

class TestGame(unittest.TestCase):
    # def test_won(self):
    #     self.assertTrue(won_result('A','Y'))
    #     self.assertTrue(won_result('B', 'Z'))
    #     self.assertTrue(won_result('C', 'X'))
    #     self.assertFalse(won_result('A','Z'))
    #     self.assertFalse(won_result('B', 'X'))
    #     self.assertFalse(won_result('C', 'Y'))
    #
    # def test_round_pts(self):
    #     self.assertEqual(round_points('A X'), 3)
    #     self.assertEqual(round_points('B Y'), 3)
    #     self.assertEqual(round_points('C Z'), 3)

    def test_draw(self):
        self.assertEqual(my_play('A Y'), 1)
        self.assertEqual(my_play('B Y'), 2)
        self.assertEqual(my_play('C Y'), 3)

    def test_win(self):
        self.assertEqual(my_play('A Z'), 2)
        self.assertEqual(my_play('B Z'), 3)
        self.assertEqual(my_play('C Z'), 1)

    def test_lose(self):
        self.assertEqual(my_play('A X'), 3)
        self.assertEqual(my_play('B X'), 1)
        self.assertEqual(my_play('C X'), 2)

