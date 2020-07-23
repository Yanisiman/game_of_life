import unittest
import game_of_life


class TestGameOfLife(unittest.TestCase):

    def test_zero_generations(self):
        input_board_state = [
            [1, 0, 0],
            [0, 1, 1],
            [1, 1, 0]
        ]
        generation_count = 0
        output_board_state = game_of_life.get_generation(
            input_board_state, generation_count)
        self.assertEquals(input_board_state, output_board_state)

    def test_static_one_generation(self):
        input_board_state = [
            [1, 0, 0],
            [0, 1, 1],
            [1, 1, 0]
        ]
        generation_count = 1
        output_board_state = game_of_life.get_generation(
            input_board_state, generation_count)
        self.assertEquals(input_board_state, output_board_state)

    """
    def test_static_two_generations(self):
        input_board_state = [
            [1, 0, 0],
            [0, 1, 1],
            [1, 1, 0]
        ]
        generation_count = 2
        output_board_state = game_of_life.get_generation(
            input_board_state, output_board_state)
        self.assertEquals()

    """


t = TestGameOfLife()
t.test_static_one_generation()
t.test_zero_generations()
