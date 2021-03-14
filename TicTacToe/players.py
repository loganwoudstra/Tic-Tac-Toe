import random
import math
import time


class Player:
    def __init__(self, symbol, game):
        self.symbol = symbol
        self.game = game


class Human(Player):
    def __init__(self, symbol, game):
        super().__init__(symbol, game)

    def ask_move(self, board):
        try:
            position = int(input("{} - Which square do you want to place your {}(0-9):".format(self.symbol, self.symbol)))
            if board[position - 1] == " ":
                return position
            else:
                print("\nThat move is not valid, please select a different square")
                return self.ask_move(board)
        except:
            print("\nThat move is not valid, please select a different square")
            return self.ask_move(board)


class Computer(Player):
    def __init__(self, symbol, game):
        super().__init__(symbol, game)
        self.name="Computer"

    def evaluate(self, winner, empty_squares):
        if winner == "X":
            return 1 * (empty_squares+1)
        else:
            return -1 * (empty_squares+1)

    def ask_move(self, board):
        if board.count(" ") == 9:
            position = random.randint(1, 9)
            return position
        else:
            minimax = self.minimax(board, board.count(" "), self.symbol)
            position = minimax[0] + 1
            return position

    def minimax(self, state, depth, player):
        if player == "X":
            opponent = "O"
            best = [None, -math.inf]
        else:
            opponent = "X"
            best = [None, math.inf]

        winner = self.game.win(state)
        if depth == 0 or winner is not None:
            score = self.evaluate(winner, state.count(" "))
            return[None, score]

        for i in range(9):
            if state[i] == " ":
                cell = i
                state[cell] = player

                score = self.minimax(state, depth - 1, opponent)
                state[cell] = " "

                score[0] = cell
                if player == "X":
                    if score[1] > best[1]:
                        best = score
                else:
                    if score[1] < best[1]:
                        best = score
        return best
