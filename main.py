import random

class Tetris():
    def __init__(self):
        self.width = 22
        self.height = 22
        self.board = self.create_board()

    def create_board(self):
        # row = [1] + [0 for _ in range(self.width)] + [1]
        # endline = [1] * 22
        # return 20 * [row] + [endline]
        board = [[0 for _ in range(self.width)] for _ in range(self.height)]
        for i in range(self.height):
            board[i][0] = 1
            board[i][self.width - 1] = 1
        for i in range(self.width):
            board[self.width - 1][i] = 1
        return board

    def display_board(self):
        for row in self.board:
            print (row)

    def select_piece(self):
        pieces = [
            [[1, 1, 1, 1]],

            [[1, 0],
             [1, 0],
             [1, 1]],

            [[0, 1],
             [0, 1],
             [1, 1]],

            [[0, 1],
             [1, 1],
             [1, 0]],

            [[1, 1],
             [1, 1]]
        ]

        return pieces[random.randrange(len(pieces))]

    def add_new_piece(self):
        piece = self.select_piece()
        y = len(piece)
        x = len(piece[0])
        if x == 4:
            for i in range(y):
                for j in range(x):
                    self.board[i][9+j] = piece[i][j]
        else:
            for i in range(y):
                for j in range(x):
                    self.board[i][10+j] = piece[i][j]


if __name__ == "__main__":
    game = Tetris()
    game.add_new_piece()
    game.display_board()

