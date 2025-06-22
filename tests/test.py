import unittest
from main import RED, BLACK, BLUE, ORANGE, RummikubSolver, Tile


class TestRummikubSolver(unittest.TestCase):
    def setUp(self):
        self.solver = RummikubSolver()

    def test_nothing(self):
        self.assertTrue(self.solver is not None)


if __name__ == "__main__":
    unittest.main()
