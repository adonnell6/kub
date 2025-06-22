import itertools

RED = "🟥"
BLACK = "⬛️"
BLUE = "🟦"
ORANGE = "🟧"

NUMBERS = list(range(1, 14))
COLORS = [RED, BLACK, BLUE, ORANGE]


class Tile:
    def __init__(self, color: str, number: int):
        # self.is_wild = False
        self.color = color
        self.number = number

    def __str__(self):
        return f"{self.color} {self.number:2}"


class RummikubSolver:
    def is_valid_set(self, tiles):
        numbers = [t.number for t in tiles]
        colors = [t.color for t in tiles]
        return (
            len(tiles) >= 3
            and len(set(numbers)) == 1
            and len(set(colors)) == len(tiles)
        )

    def is_valid_run(self, tiles):
        tiles.sort(key=lambda x: x.number)
        colors = [t.color for t in tiles]
        numbers = [t.number for t in tiles]
        return (
            len(tiles) >= 3
            and len(set(colors)) == 1
            and all(
                numbers[i] + 1 == numbers[i + 1]
                for i in range(len(numbers) - 1)
            )
        )

    def _is_valid_combination(self, tiles):
        if self.is_valid_set(tiles) or self.is_valid_run(tiles):
            return True
        return False

    def _backtrack(self, tiles, current_combination):
        if not tiles:
            return current_combination if current_combination else None
        for r in range(3, len(tiles) + 1):
            for subset in itertools.combinations(tiles, r):
                subset = list(subset)
                remaining_tiles = [
                    tile for tile in tiles if tile not in subset
                ]
                if self._is_valid_combination(subset):
                    new_combination = current_combination + [subset]
                    result = self._backtrack(remaining_tiles, new_combination)
                    if result is not None:
                        return result
        return None

    def find_valid_combination(self, tiles):
        if not tiles:
            return None
        result = self._backtrack(tiles, [])
        return result

    def find_best_play(self, board_tiles, hand_tiles):
        for length in range(len(hand_tiles), 0, -1):
            for subset in itertools.combinations(hand_tiles, length):
                new_board_tiles = board_tiles + list(subset)
                result = self.find_valid_combination(new_board_tiles)
                if result:
                    return {"tiles": list(subset), "combination": result}
        return None


def main():
    solver = RummikubSolver()

    board_tiles = [
        Tile(RED, 1),
        Tile(RED, 2),
        Tile(RED, 3),
        Tile(RED, 4),
        Tile(RED, 5),
        Tile(RED, 6),
        Tile(RED, 8),
        Tile(RED, 9),
        Tile(RED, 10),
    ]

    hand_tiles = [
        Tile(ORANGE, 1),
        Tile(ORANGE, 2),
        Tile(ORANGE, 3),
        Tile(ORANGE, 4),
        Tile(RED, 7),
        Tile(BLACK, 4),
    ]

    existing_combos = solver.find_valid_combination(board_tiles)

    assert (
        existing_combos is not None or board_tiles == []
    ), "Existing board is not valid"

    best_play = solver.find_best_play(board_tiles, hand_tiles)

    print("Existing combinations on board:")
    for subset in existing_combos:
        print("  ", [str(tile) for tile in subset])

    if best_play:
        print("Best play found:")
        print("  Tiles to play:", [str(tile) for tile in best_play["tiles"]])
        print("  Combination on board:")
        for subset in best_play["combination"]:
            print("    ", [str(tile) for tile in subset])
    else:
        print("No valid play found.")


if __name__ == "__main__":
    main()
