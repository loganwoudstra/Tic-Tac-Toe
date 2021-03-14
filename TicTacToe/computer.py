import random
import math

class Computer:
    def __init__(self, symbol, game):
        self.symbol = symbol
        self.game = game
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
