import functools
import itertools


RED = "🟥"
BLACK = "⬛️"
BLUE = "🟦"
ORANGE = "🟧"

NUMBERS = list(range(1, 14))
COLORS = [RED, BLACK, BLUE, ORANGE]


class Tile:

    def __init__(self, color: str, number: int, is_wild: bool = False):
        self.color = color
        self.number = number
        self.is_wild = is_wild

    def __str__(self):
        if self.is_wild:
            return "🌟"
        else:
            return f"{self.color} {self.number:2}"


class RummikubSolver:
    def is_valid_set(self, tiles):
        numbers = [t.number for t in tiles if not t.is_wild]
        colors = [t.color for t in tiles if not t.is_wild]
        return (
            len(tiles) >= 3
            and len(set(numbers)) == 1
            and len(set(colors)) == len(colors)
        )

    def is_valid_run(self, tiles):
        if (len(tiles) < 3) or len(
            set(t.color for t in tiles if not t.is_wild)
        ) > 1:
            return False

        numbers = [t.number for t in tiles if not t.is_wild]
        numbers.sort()
        wild_count = len([t for t in tiles if t.is_wild])
        for i in range(len(numbers) - 1):
            if numbers[i] + 1 == numbers[i + 1]:
                continue
            if numbers[i] + 2 == numbers[i + 1]:
                if wild_count > 0:
                    wild_count -= 1
                else:
                    return False
            else:
                return False
        return True

    @functools.lru_cache(maxsize=None)
    def _is_valid_combination(self, tiles):
        return self.is_valid_set(list(tiles)) or self.is_valid_run(list(tiles))

    def _backtrack(self, tiles, current_combination):
        if not tiles:
            return current_combination if current_combination else None
        for r in range(3, len(tiles) + 1):
            for subset in itertools.combinations(tiles, r):
                subset = list(subset)
                remaining_tiles = [
                    tile for tile in tiles if tile not in subset
                ]
                if self._is_valid_combination(tuple(subset)):
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
        # wildcard
        Tile(None, None, True),
    ]

    hand_tiles = [
        Tile(ORANGE, 1),
        Tile(ORANGE, 2),
        Tile(ORANGE, 3),
        Tile(ORANGE, 4),
        Tile(RED, 7),
        Tile(BLACK, 4),
        # Tile(BLUE, 13),
        # Tile(BLUE, 9),
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
