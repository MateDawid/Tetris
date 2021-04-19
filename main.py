import random
from copy import deepcopy


class Tetris:
    def __init__(self):
        self.size = 22
        self.pieces = [
            [[1], [1], [1], [1]],

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

    def create_board(self):
        board = [[0 for _ in range(self.size)] for _ in range(self.size)]
        for i in range(self.size):
            board[i][0] = 1
            board[i][self.size - 1] = 1
        for i in range(self.size):
            board[self.size - 1][i] = 1
        return board

    def display_board(self, board, piece_position, piece):
        board_copy = deepcopy(board)
        x = len(piece)
        y = len(piece[0])
        for i in range(x):
            for j in range(y):
                board_copy[piece_position[0] + i][piece_position[1] + j] = piece[i][j]
        for i in range(self.size):
            for j in range(self.size):
                if board_copy[i][j] == 1:
                    print("*", end='')
                else:
                    print(" ", end='')
            print("")

    def is_game_over(self, board, piece_position, piece):
        if (not self.can_move_down(board, piece_position, piece)) and piece_position[0] == 0:
            return True
        return False

    def select_piece(self):
        return self.pieces[random.randrange(len(self.pieces))]

    @staticmethod
    def move_left(piece_position):
        next_position = [piece_position[0], piece_position[1] - 1]
        return next_position

    @staticmethod
    def move_right(piece_position):
        next_position = [piece_position[0], piece_position[1] + 1]
        return next_position

    @staticmethod
    def move_down(piece_position):
        next_position = [piece_position[0] + 1, piece_position[1]]
        return next_position

    @staticmethod
    def rotate_clocwise(piece):
        copy = deepcopy(piece)
        next_piece = list(list(elem) for elem in zip(*(copy[::-1])))
        return next_piece

    @staticmethod
    def rotate_anticlockwise(piece):
        copy = deepcopy(piece)
        first_rotation = list(list(elem) for elem in zip(*(copy[::-1])))
        second_rotation = list(list(elem) for elem in zip(*first_rotation))
        third_rotation = list(list(elem) for elem in zip(*second_rotation))
        next_piece = third_rotation
        return next_piece

    @staticmethod
    def can_move(board, piece_position, piece):
        x = len(piece)
        y = len(piece[0])
        for i in range(x):
            for j in range(y):
                if board[piece_position[0] + i][piece_position[1] + j] == 1 and piece[i][j] == 1:
                    return False
        return True

    def can_move_left(self, board, piece_position, piece):
        next_position = self.move_left(piece_position)
        return self.can_move(board, next_position, piece)

    def can_move_right(self, board, piece_position, piece):
        next_position = self.move_right(piece_position)
        return self.can_move(board, next_position, piece)

    def can_move_down(self, board, piece_position, piece):
        next_position = self.move_down(piece_position)
        return self.can_move(board, next_position, piece)

    def can_rotate_clockwise(self, board, piece_position, piece):
        next_piece = self.rotate_clockwise(piece)
        return self.can_move(board, piece_position, next_piece)

    def can_rotate_anticlockwise(self, board, piece_position, piece):
        next_piece = self.rotate_anticlockwise(piece)
        return self.can_move(board, piece_position, next_piece)

    @staticmethod
    def update_board(board, piece_position, piece):
        x = len(piece)
        y = len(piece[0])
        for i in range(x):
            for j in range(y):
                board[piece_position[0] + i][piece_position[1] + j] = piece[i][j]

    def play_game(self):
        instruction = "INSTRUCTION:\na (move left), d (move right), w (rotate counter clockwise), s (rotate clockwise)"
        board = self.create_board()
        piece = self.select_piece()
        piece_position = [0, (self.size-2)//2]
        self.display_board(board, piece_position, piece)
        print(instruction)
        player_move = input("Move - ")

        while not self.is_game_over(board, piece_position, piece):
            go_down = False
            message = ""
            if player_move == "a":
                if self.can_move_left(board, piece_position, piece):
                    piece_position = self.move_left(piece_position)
                    go_down = True
                else:
                    message = "ALERT: You can't make that move!"
            elif player_move == "d":
                if self.can_move_right(board, piece_position, piece):
                    piece_position = self.move_right(piece_position)
                    go_down = True
                else:
                    message = "ALERT: You can't make that move!"
            elif player_move == "w":
                if self.can_rotate_anticlockwise(board, piece_position, piece):
                    piece = self.rotate_anticlockwise(piece)
                    go_down = True
                else:
                    message = "ALERT: You can't make that move!"
            elif player_move == "s":
                if self.can_rotate_clockwise(board, piece_position, piece):
                    piece = self.rotate_clockwise(piece)
                    go_down = True
                else:
                    message = "ALERT: You can't make that move!"
            else:
                message = "ALERT: Wrong key!"

            if go_down and self.can_move_down(board, piece_position, piece):
                piece_position = self.move_down(piece_position)

            if not self.can_move_down(board, piece_position, piece):
                self.update_board(board, piece_position, piece)
                piece = self.select_piece()
                piece_position = [0, (self.size-2)//2]

            self.display_board(board, piece_position, piece)
            print(instruction)
            print(message)
            player_move = input("Move - ")

        print("ALERT: No moves left. The game is over.")


if __name__ == "__main__":
    game = Tetris()
    game.play_game()
