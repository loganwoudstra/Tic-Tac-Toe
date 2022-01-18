from TicTacToe import computer
import time


class TicTacToe:
    def __init__(self):
        self.board = self.new_board()
        self.line = '-----------\n'

    @staticmethod
    def new_board():
        return [" " for _ in range(9)]

    def show_board(self):
        board1 = '\n  {} | {} | {} \n'.format(self.board[0], self.board[1], self.board[2])
        board2 = ' {} | {} | {} \n'.format(self.board[3], self.board[4], self.board[5])
        board3 = ' {} | {} | {} \n'.format(self.board[6], self.board[7], self.board[8])
        print(" " + board1, self.line, board2, self.line, board3)

    @staticmethod
    def start_board():
        print("\n 1 | 2 | 3 \n"
              "-----------\n"
              " 4 | 5 | 6 \n"
              "-----------\n"
              " 7 | 8 | 9 \n")

    def empty_squares(self):
        return ' ' in self.board

    def win(self, board):
        # row
        for i in range(0, 9, 3):
            if board[i] == board[i + 1] == board[i + 2] != " ":
                return board[i]

        # column
        for i in range(3):
            if board[i] == board[i + 3] == board[i + 6]!= " ":
                return board[i]

        # diagonals
        if board[0] == board[4] == board[8] != " ":
            return board[0]

        if board[2] == board[4] == board[6] != " ":
            return board[2]

        return None

    def make_move(self, square, symbol):
        self.board[square - 1] = symbol
        return self.win(self.board)

    def num_empty_spaces(self):
        return self.board.count(' ')


def play(ttt, player1, player2):
    symbol = 'X'
    ttt.start_board()
    board = ['','','','','','','','','']
    while ttt.empty_squares():
        # determines who's turn it is
        for i in range(9):
            board[i] = ttt.board[i]
        if symbol == "X":
            move = player1.ask_move(board)
            if player1.name == "Computer":
                print("Computer {} placed their {} on square {}".format(symbol, symbol, move))

        else:
            move = player2.ask_move(board)
            if player2.name == "Computer":
                print("Computer {} placed their {} on square {}".format(symbol, symbol, move))

        # makes move and checks for winner
        if ttt.make_move(move, symbol) is not None:
            ttt.show_board()
            return symbol + " HAS WON!"

        ttt.show_board()
        time.sleep(1)

        # switches turns
        if symbol == "X":
            symbol = "O"
        else:
            symbol = "X"
    return "TIE GAME!"


game = TicTacToe()
print(play(game, computer.Computer('X', game), computer.Computer('O', game)))
