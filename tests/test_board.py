import unittest

from board import Board
from player import Player

class Test_isPositionOccupied(unittest.TestCase):
    def test_is_position_Occupied(self):

        test_board = Board()
        test_player = Player("X")

        test_board.grid[0][0] = test_player

        self.assertTrue(test_board.is_position_occupied(0,0))
        self.assertFalse(test_board.is_position_occupied(0, 1))
        self.assertFalse(test_board.is_position_occupied(1, 0))
