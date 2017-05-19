"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest
from importlib import reload
from unittest.mock import MagicMock

import game_agent
import isolation
from game_agent import *
from isolation.isolation import Board

DEPTH = 3


def test_score(game, player):
    pass


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)

        self.player1 = "Player1"
        self.player2 = "Player2"
        self.game = isolation.Board(self.player1, self.player2)

        self.minimax_player = MinimaxPlayer(DEPTH)
        self.minimax_player.time_left = lambda: 10

    def test_should_return_minus_one_when_no_legal_moves(self):
        board = Node(self.player1,
                     self.player2).execute()

        coordinates = self.minimax_player.minimax(board, DEPTH)

        self.assertEquals(coordinates, (-1, -1), 'The coordinates when no moves left is -1,-1')

    def test_should_return_the_max_value_of_the_score_of_two_leafs(self):
        node = Node(self.player1,
                    self.player2)

        self.minimax_player.score = MagicMock(side_effect=[float("inf"), float("inf")])
        node.add_leaf(Leaf(self.player1, self.player2, (1, 1)))
        node.add_leaf(Leaf(self.player1, self.player2, (1, 2)))

        coordinates = self.minimax_player.minimax(node.execute(), DEPTH)

        self.assertEquals(coordinates, (1, 1), 'The coordinates is the min coordinates value is (1,1)')

    def test_should_return_the_max_value_of_the_score_of_another_two_leafs(self):
        node = Node(self.player1,
                    self.player2)

        self.minimax_player.score = MagicMock(side_effect=[float("inf"), float("inf")])
        node.add_leaf(Leaf(self.player1, self.player2, (1, 4)))
        node.add_leaf(Leaf(self.player1, self.player2, (1, 2)))

        coordinates = self.minimax_player.minimax(node.execute(), DEPTH)

        self.assertEquals(coordinates, (1, 4), 'The coordinates is the min coordinates value is (1,4)')

    def test_should_return_the_max_value_of_two_leafs_with_two_different_utilities(self):
        node = Node(self.player1,
                    self.player2)

        self.minimax_player.score = MagicMock(side_effect=[float("-inf"), float("inf")])
        node.add_leaf(Leaf(self.player1, self.player2, (1, 4)))
        node.add_leaf(Leaf(self.player1, self.player2, (1, 2)))

        coordinates = self.minimax_player.minimax(node.execute(), DEPTH)

        self.assertEquals(coordinates, (1, 2), 'The coordinates is the max min coordinates value is (1,2)')

    def test_should_return_the_max_of_min_value_of_the_score_a_node_and_a_leaf_with_node(self):
        node = Node(self.player1,
                    self.player2)

        child_node = Node(self.player1, self.player2)
        child_node.move = (1, 4)
        node.add_leaf(child_node)

        self.minimax_player.score = MagicMock(side_effect=[float("inf"), float("inf"), float("inf")])
        child_node.add_leaf(Leaf(self.player1, self.player2, (2, 1)))
        child_node.add_leaf(Leaf(self.player1, self.player2, (2, 4)))

        node.add_leaf(Leaf(self.player1, self.player2, (1, 2)))

        coordinates = self.minimax_player.minimax(node.execute(), DEPTH)

        self.assertEquals(coordinates, (1, 4), 'The coordinates is the max min coordinates value is (1,4)')

    def test_should_return_the_max_of_min_value_of_the_score_a_node_and_a_leaf(self):
        node = Node(self.player1,
                    self.player2)

        child_node = Node(self.player1, self.player2)
        child_node.move = (1, 4)
        node.add_leaf(child_node)

        self.minimax_player.score = MagicMock(side_effect=[float("inf"), float("-inf"), float("inf")])
        child_node.add_leaf(Leaf(self.player1, self.player2, (2, 1)))
        child_node.add_leaf(Leaf(self.player1, self.player2, (2, 4)))

        node.add_leaf(Leaf(self.player1, self.player2, (1, 2)))

        coordinates = self.minimax_player.minimax(node.execute(), DEPTH)

        self.assertEquals(coordinates, (1, 2), 'The coordinates is the max min coordinates value is (1,2)')

    def test_should_return_the_max_of_min_value_of_the_score_two_nodes_second_wins(self):
        node = Node(self.player1,
                    self.player2)

        child_node = Node(self.player1, self.player2)
        child_node.move = (1, 4)

        self.minimax_player.score = MagicMock(side_effect=[float("inf"), float("inf"), float("-inf"), float("-inf")])
        child_node.add_leaf(Leaf(self.player1, self.player2, (2, 1)))
        child_node.add_leaf(Leaf(self.player1, self.player2, (2, 4)))

        second_child_node = Node(self.player1, self.player2)
        second_child_node.move = (1, 2)
        second_child_node.add_leaf(Leaf(self.player1, self.player2, (3, 1)))
        second_child_node.add_leaf(Leaf(self.player1, self.player2, (4, 4)))

        node.add_leaf(child_node)
        node.add_leaf(second_child_node)

        coordinates = self.minimax_player.minimax(node.execute(), DEPTH)

        self.assertEquals(coordinates, (1, 4), 'The coordinates is the max min coordinates value is (1,4)')

    def test_should_return_the_max_of_min_value_of_the_score_two_nodes_a_leaf_and_leaf_wins(self):
        node = Node(self.player1,
                    self.player2)

        self.minimax_player.score = MagicMock(
            side_effect=[float("-inf"), float("inf"), float("-inf"), float("-inf"), float("inf")])

        child_node = Node(self.player1, self.player2)
        child_node.move = (1, 4)
        child_node.add_leaf(Leaf(self.player1, self.player2, (2, 1)))
        child_node.add_leaf(Leaf(self.player1, self.player2, (2, 4)))

        second_child_node = Node(self.player1, self.player2)
        second_child_node.move = (1, 2)
        second_child_node.add_leaf(Leaf(self.player1, self.player2, (3, 1)))
        second_child_node.add_leaf(Leaf(self.player1, self.player2, (4, 4)))

        node.add_leaf(second_child_node)
        node.add_leaf(child_node)
        node.add_leaf(Leaf(self.player1, self.player2, (3, 6)))

        coordinates = self.minimax_player.minimax(node.execute(), DEPTH)

        self.assertEquals(coordinates, (3, 6), 'The coordinates is the max min coordinates value is (3,6)')

    def test_should_return_the_max_of_min_value_of_the_score_two_nodes_with_other_nodes(self):
        self.minimax_player.score = MagicMock(
            side_effect=[float("-inf"), float("inf"), float("-inf"), float("-inf"), float("-inf"), float("inf"),
                         float("-inf"), float("inf"), float("inf")])

        node = self.create_three_levels_game()

        coordinates = self.minimax_player.minimax(node.execute(), DEPTH)

        self.assertEquals(coordinates, (1, 4), 'The coordinates is the max min coordinates value is (1,4)')

    def test_should_search_until_level_two(self):
        self.minimax_player.score = MagicMock(
            side_effect=[float("-inf"), float("inf"), float("-inf"), float("-inf"), float("-inf")])

        node = self.create_three_levels_game()

        two_level_depth = 2
        coordinates = self.minimax_player.minimax(node.execute(), two_level_depth)

        self.assertEquals(coordinates, (1, 2), 'The coordinates is the max min coordinates value is (1,2)')

    def create_three_levels_game(self):
        node = Node(self.player1,
                    self.player2)

        third_node = Node(self.player1, self.player2)
        third_node.move = (2, 2)
        third_node.add_leaf(Leaf(self.player1, self.player2, (3, 2)))
        third_node.add_leaf(Leaf(self.player1, self.player2, (3, 4)))

        fourth_child_node = Node(self.player1, self.player2)
        fourth_child_node.move = (2, 4)
        fourth_child_node.add_leaf(Leaf(self.player1, self.player2, (3, 6)))
        fourth_child_node.add_leaf(Leaf(self.player1, self.player2, (3, 8)))

        fifth_node = Node(self.player1, self.player2)
        fifth_node.move = (2, 6)
        fifth_node.add_leaf(Leaf(self.player1, self.player2, (3, 10)))
        fifth_node.add_leaf(Leaf(self.player1, self.player2, (3, 12)))

        sixth_node = Node(self.player1, self.player2)
        sixth_node.move = (2, 8)
        sixth_node.add_leaf(Leaf(self.player1, self.player2, (3, 14)))
        sixth_node.add_leaf(Leaf(self.player1, self.player2, (3, 16)))

        second_child_node = Node(self.player1, self.player2)
        second_child_node.move = (1, 2)
        second_child_node.add_leaf(third_node)
        second_child_node.add_leaf(fourth_child_node)

        first_child_node = Node(self.player1, self.player2)
        first_child_node.move = (1, 4)
        first_child_node.add_leaf(fifth_node)
        first_child_node.add_leaf(sixth_node)

        node.add_leaf(second_child_node)
        node.add_leaf(first_child_node)
        node.add_leaf(Leaf(self.player1, self.player2, (3, 6)))

        return node


class Node:
    def __init__(self, player1, player2):
        self.leafs = []
        self.move = (-1, -1)
        self.player1 = player1
        self.player2 = player2

    def execute(self):
        forecast_board = Board(self.player1, self.player2)

        moves = []
        for leaf in self.leafs:
            moves.append(leaf.get_move())

        forecast_board.get_legal_moves = MagicMock(return_value=moves)

        forecast_boards = []
        for leaf in self.leafs:
            forecast_boards.append(leaf.execute())

        forecast_board.forecast_move = MagicMock(side_effect=forecast_boards)

        return forecast_board

    def add_leaf(self, leaf):
        self.leafs.append(leaf)

    def get_move(self):
        return self.move


class Leaf:
    def __init__(self, player1, player2, move):
        self.move = move
        self.player1 = player1
        self.player2 = player2

    def execute(self):
        forecast_board = Board(self.player1, self.player2)
        forecast_board.get_legal_moves = MagicMock(return_value=list())

        return forecast_board

    def get_move(self):
        return self.move


if __name__ == '__main__':
    unittest.main()
