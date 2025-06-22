from collections import defaultdict, Counter
from itertools import combinations


RED = "🟥"
BLACK = "⬛️"
BLUE = "🟦"
ORANGE = "🟧"

NUMBERS = list(range(1, 14))
COLORS = [RED, BLACK, BLUE, ORANGE]


class Tile:

    def __init__(self, color, number, is_wild=False):
        self.color = color
        self.number = number
        self.is_wild = is_wild

    def __hash__(self):
        return hash((self.color, self.number, self.is_wild))

    def __eq__(self, other):
        return (self.color, self.number, self.is_wild) == (
            other.color,
            other.number,
            other.is_wild,
        )

    def __str__(self):
        return "🌟" if self.is_wild else f"{self.color}{self.number:2}"

    def __repr__(self):
        return str(self)


class RummikubSolver:

    def find_all_valid_groups(self, tiles):
        wilds = [t for t in tiles if t.is_wild]
        non_wilds = [t for t in tiles if not t.is_wild]

        sets = self._find_valid_sets(non_wilds, wilds)
        runs = self._find_valid_runs(non_wilds, wilds)

        return sets + runs

    def _find_valid_sets(self, tiles, wilds):
        number_groups = defaultdict(list)
        for t in tiles:
            number_groups[t.number].append(t)

        valid_sets = []
        for number, group in number_groups.items():
            unique_colors = {t.color for t in group}
            base_tiles = list({t.color: t for t in group}.values())
            for k in range(3, min(4, len(base_tiles) + len(wilds)) + 1):
                needed = k - len(base_tiles)
                if needed <= len(wilds):
                    for wild_combo in combinations(wilds, needed):
                        valid_sets.append(base_tiles + list(wild_combo))
        return valid_sets

    def _find_valid_runs(self, tiles, wilds):
        color_groups = defaultdict(list)
        for t in tiles:
            color_groups[t.color].append(t)

        valid_runs = []
        for color, group in color_groups.items():
            numbers = sorted(set(t.number for t in group))
            num_set = {t.number: t for t in group}
            for start in range(1, 12):
                run, needed = [], 0
                for offset in range(0, 13):
                    num = start + offset
                    if num > 13:
                        break
                    if num in num_set:
                        run.append(num_set[num])
                    elif needed < len(wilds):
                        run.append(Tile(None, None, True))
                        needed += 1
                    else:
                        break
                    if len(run) >= 3:
                        valid_runs.append(run[:])
        return valid_runs

    def find_optimal_play(self, board_tiles, hand_tiles):
        all_tiles = board_tiles + hand_tiles
        all_groups = self.find_all_valid_groups(all_tiles)
        board_set = set(board_tiles)

        best_result = {"tiles": [], "combination": []}

        def backtrack(idx, used, used_hand, used_board, path):
            nonlocal best_result
            if idx == len(all_groups):
                if board_set.issubset(used):
                    if len(used_hand) > len(best_result["tiles"]):
                        best_result = {
                            "tiles": list(used_hand),
                            "combination": list(path),
                        }
                return

            group = all_groups[idx]
            group_set = set(group)

            if not group_set & used:
                new_used = used | group_set
                new_hand = used_hand | {t for t in group if t in hand_tiles}
                new_board = used_board | {t for t in group if t in board_tiles}
                path.append(group)
                backtrack(idx + 1, new_used, new_hand, new_board, path)
                path.pop()

            backtrack(idx + 1, used, used_hand, used_board, path)

        backtrack(0, set(), set(), set(), [])
        return best_result if best_result["tiles"] else None


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
        Tile(BLUE, 13),
        Tile(BLUE, 9),
    ]

    # existing_combos = solver.find_valid_combination(board_tiles)

    # assert (
    #     existing_combos is not None or board_tiles == []
    # ), "Existing board is not valid"

    best_play = solver.find_optimal_play(board_tiles, hand_tiles)

    # print("Existing combinations on board:")
    # for subset in existing_combos:
    #     print("  ", [str(tile) for tile in subset])

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
