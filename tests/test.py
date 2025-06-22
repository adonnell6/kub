import unittest
from main import RED, BLACK, BLUE, ORANGE, RummikubSolver, Tile


class TestRummikubSolver(unittest.TestCase):
    def setUp(self):
        self.solver = RummikubSolver()

    def test_is_valid_set(self):
        self.assertTrue(
            self.solver.is_valid_set(
                [Tile(RED, 1), Tile(BLACK, 1), Tile(BLUE, 1)]
            )
        )

        self.assertTrue(
            self.solver.is_valid_set(
                [Tile(RED, 1), Tile(BLACK, 1), Tile(BLUE, 1), Tile(ORANGE, 1)]
            )
        )

        self.assertFalse(
            self.solver.is_valid_set(
                [Tile(RED, 1), Tile(BLACK, 1), Tile(BLUE, 2)]
            )
        )

        self.assertFalse(
            self.solver.is_valid_set([Tile(RED, 1), Tile(BLACK, 1)])
        )

        self.assertFalse(
            self.solver.is_valid_set(
                [Tile(RED, 1), Tile(BLACK, 1), Tile(RED, 1)]
            )
        )

        self.assertFalse(
            self.solver.is_valid_set(
                [Tile(RED, 1), Tile(BLACK, 1), Tile(BLUE, 1), Tile(ORANGE, 2)]
            )
        )

    def test_is_valid_run(self):
        self.assertTrue(
            self.solver.is_valid_run(
                [Tile(RED, 1), Tile(RED, 2), Tile(RED, 3)]
            )
        )

        self.assertTrue(
            self.solver.is_valid_run(
                [Tile(BLACK, 1), Tile(BLACK, 2), Tile(BLACK, 3)]
            )
        )

        self.assertTrue(
            self.solver.is_valid_run(
                [Tile(BLUE, 1), Tile(BLUE, 2), Tile(BLUE, 3), Tile(BLUE, 4)]
            )
        )

        self.assertFalse(
            self.solver.is_valid_run(
                [Tile(BLUE, 1), Tile(BLUE, 2), Tile(BLUE, 4)]
            )
        )

        self.assertFalse(
            self.solver.is_valid_run([Tile(ORANGE, 1), Tile(ORANGE, 2)])
        )

        self.assertFalse(
            self.solver.is_valid_run(
                [Tile(RED, 1), Tile(BLACK, 2), Tile(BLUE, 3)]
            )
        )

    def test_find_valid_combination(self):
        self.assertIsNone(self.solver.find_valid_combination([]))

        self.assertIsNone(
            self.solver.find_valid_combination([Tile(RED, 1), Tile(RED, 2)])
        )

        self.assertIsNone(
            self.solver.find_valid_combination(
                [Tile(RED, 1), Tile(ORANGE, 11)]
            )
        )

        self.assertIsNone(
            self.solver.find_valid_combination(
                [
                    Tile(RED, 1),
                    Tile(RED, 2),
                    Tile(RED, 3),
                    Tile(RED, 4),
                    Tile(RED, 5),
                    Tile(RED, 7),
                ]
            )
        )

        self.assertIsNotNone(
            self.solver.find_valid_combination(
                [
                    Tile(RED, 1),
                    Tile(RED, 2),
                    Tile(RED, 3),
                    Tile(RED, 4),
                    Tile(RED, 5),
                    Tile(RED, 6),
                ]
            )
        )

        self.assertIsNotNone(
            self.solver.find_valid_combination(
                [
                    Tile(RED, 1),
                    Tile(RED, 2),
                    Tile(RED, 3),
                    Tile(ORANGE, 4),
                    Tile(ORANGE, 5),
                    Tile(ORANGE, 6),
                    Tile(RED, 4),
                    Tile(BLUE, 4),
                    Tile(BLACK, 4),
                ]
            )
        )

    def test_find_valid_combination_sorted(self):
        self.assertIsNotNone(
            self.solver.find_valid_combination(
                [
                    Tile(RED, 5),
                    Tile(RED, 6),
                    Tile(RED, 7),
                    Tile(BLACK, 4),
                    Tile(ORANGE, 4),
                    Tile(RED, 4),
                ]
            )
        )

    def test_find_valid_combination_unorganized(self):
        self.assertIsNotNone(
            self.solver.find_valid_combination(
                [
                    Tile(RED, 4),
                    Tile(RED, 5),
                    Tile(RED, 6),
                    Tile(ORANGE, 4),
                    Tile(RED, 7),
                    Tile(BLACK, 4),
                ]
            )
        )

    def test_find_valid_combination_unorganized_2(self):
        self.assertIsNotNone(
            self.solver.find_valid_combination(
                [
                    Tile(RED, 4),
                    Tile(BLACK, 4),
                    Tile(RED, 5),
                    Tile(BLACK, 5),
                    Tile(RED, 6),
                    Tile(BLACK, 6),
                ]
            )
        )

    def test_find_valid_combination_uneven_length(self):
        self.assertIsNotNone(
            self.solver.find_valid_combination(
                [
                    Tile(RED, 4),
                    Tile(BLACK, 4),
                    Tile(RED, 5),
                    Tile(BLACK, 5),
                    Tile(RED, 6),
                    Tile(BLACK, 6),
                    Tile(RED, 7),
                    Tile(RED, 8),
                ]
            )
        )


if __name__ == "__main__":
    unittest.main()
