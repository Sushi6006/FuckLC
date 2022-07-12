class Solution:

    WIDTH = 3

    def tictactoe(self, moves: list[list[int]]) -> str:

        def check_straight(moves: list[list[int]]) -> bool:
            if len(moves) < self.WIDTH:  # not enough
                return False
            for dir in range(2):
                for _ in range(self.WIDTH):
                    a_pos = set([move[dir] for move in moves])
                    for num in a_pos:
                        if list([move[dir] for move in moves]).count(
                                num) == self.WIDTH:
                            return True  # WIN
            return False  # criteria not met

        def check_diag(moves: list[list[int]]) -> bool:
            diag_line_1 = [[0, 0], [1, 1], [2, 2]]
            diag_line_2 = [[0, 2], [1, 1], [2, 0]]
            if all([slot in moves for slot in diag_line_1]) or \
                    all([slot in moves for slot in diag_line_2]):
                return True  # WIN
            return False  # criteria not met

        # check if anyone won, regardless the game is finished or not
        a_moves = [moves[i] for i in range(0, len(moves), 2)]
        b_moves = [moves[i] for i in range(1, len(moves), 2)]
        # print("a_moves: {}".format(a_moves))
        # print("b_moves: {}".format(b_moves))

        if check_straight(a_moves) or check_diag(a_moves):
            return "A"
        elif check_straight(b_moves) or check_diag(b_moves):
            return "B"

        # check if a game is NOT finished yet
        if len(moves) < 9:
            return "Pending"

        # else, draw
        return "Draw"


if __name__ == "__main__":
    solution = Solution()

    moves = [[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]
    print("\n======================\nMoves:   {}".format(moves))
    print("Result: ", solution.tictactoe(moves))

    moves = [[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]]
    print("\n======================\nMoves:   {}".format(moves))
    print("Result: ", solution.tictactoe(moves))

    moves = [[0, 0], [1, 1], [2, 0], [1, 0], [
        1, 2], [2, 1], [0, 1], [0, 2], [2, 2]]
    print("\n======================\nMoves:   {}".format(moves))
    print("Result: ", solution.tictactoe(moves))

    moves = [[0, 0], [1, 1]]
    print("\n======================\nMoves:   {}".format(moves))
    print("Result: ", solution.tictactoe(moves))

    moves = [[1, 2], [2, 1], [1, 0], [0, 0], [0, 1], [2, 0], [1, 1]]
    print("\n======================\nMoves:   {}".format(moves))
    print("Result: ", solution.tictactoe(moves))
