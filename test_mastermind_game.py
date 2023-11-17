'''
Amare Diotte
CS 5001
Spring 2021
Final Project
'''

import unittest
from mastermind_game import *
from Marble import Marble

ROUND = Round(0, 10)


class TestMastermindGame(unittest.TestCase):
    '''
    Tests for functions in mastermind_game
    '''

    def test_generate_code(self):
        # wasn't sure how to do an expected with a random number
        # generator, so I'm checking that the list is the right length
        self.assertEqual(4, len(generate_code()))

    def test_count_bulls_and_cows(self):
        # cows
        secret_code = ["red", "blue", "blue", "red"]
        guess = ["blue", "red", "red", "blue"]
        self.assertEqual((0,4), count_bulls_and_cows(secret_code, guess))
        # bulls
        secret_code = ["blue", "red", "red", "blue"]
        guess = ["blue", "red", "red", "blue"]
        self.assertEqual((4,0), count_bulls_and_cows(secret_code, guess))
        # bulls & cows
        secret_code = ["blue", "red", "blue", "red"]
        guess = ["blue", "red", "red", "blue"]
        self.assertEqual((2,2), count_bulls_and_cows(secret_code, guess))

    def test_load_winners(self):
        # returns list of strings
        file_name = "test_text.txt"
        print(load_winners(file_name))
        self.assertEqual(["test!\n"], load_winners(file_name))

    # Round testing starts here:
    def test__init__(self):
        self.assertEqual(0 , ROUND.start)
        self.assertEqual(0 , ROUND.current)
        self.assertEqual(10 , ROUND.end)

    def test_bad__init__(self):
        with self.assertRaises(ValueError):
            round1 = Round("0", "10")

    def test__eq__(self):
        round2 = Round(0, 10)
        self.assertTrue(round2, ROUND)

    def test__str__(self):
        self.assertEqual("The current round is 0", str(ROUND))

    def test_add(self):
        round3 = Round(4, 10)
        round3.add()
        self.assertEqual(5, round3.current)

    def test_subtract(self):
        round3 = Round(4, 10)
        round3.subtract()
        self.assertEqual(3, round3.current)

    def test_set_to_zero(self):
        round3 = Round(4, 10)
        round3.set_to_zero()
        self.assertEqual(0, round3.current)
        


def main():
    unittest.main(verbosity = 3)

if __name__ == "__main__":
    main()
