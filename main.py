import random

class Tetris():
    def __init__(self):
        self.width = 22
        self.height = 22
        self.board = self.create_board()
        self.piece =
        self.piece_position = [0, 10]


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

        self.piece = pieces[random.randrange(len(pieces))]

    def add_new_piece(self):
        self.piece_position = [0, 10]
        y = len(self.piece)
        x = len(self.piece[0])
        for i in range(y):
            for j in range(x):
                self.board[self.piece_position[0]+i][self.piece_position[1]+j] = self.piece[i][j]


    def move_left(self):
        self.piece_position = [self.piece_position[0]+1, self.piece_position[1] - 1]

    def move_right(self):
        self.piece_position = [self.piece_position[0]+1, self.piece_position[1] + 1]

    def rotate_clocwise(self):
        self.piece = list(list(elem) for elem in zip(*(self.piece[::-1])))
        self.piece_position = [self.piece_position[0] + 1, self.piece_position[1]]

    def rotate_anticlockwise(self):
        first_rotation = list(list(elem) for elem in zip(*(self.piece[::-1])))
        second_rotation = list(list(elem) for elem in zip(*first_rotation))
        third_rotation = list(list(elem) for elem in zip(*second_rotation))
        self.piece = third_rotation
        self.piece_position = [self.piece_position[0] + 1, self.piece_position[1]]




if __name__ == "__main__":
    game = Tetris()
    game.add_new_piece()
    game.display_board()

