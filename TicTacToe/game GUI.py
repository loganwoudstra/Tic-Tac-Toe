import sys
sys.path.append(".")

from computer import Computer
import tkinter as tk


class TicTacToe:
    def __init__(self, master):
        # create variables
        self.board = [" " for _ in range(9)]
        self.start_board = ["T", "I", "C", "T", "A", "C", "T", "O", "E"]
        self.line = '-----------\n'
        self.symbol = "X"
        self.x_score = 0
        self.o_score = 0

        # create GUI
        master.geometry('410x400')
        master.title("Tic Tac Toe")

        frame = tk.Frame(master, bg='light gray')
        frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        # create dropdown menus
        player_list = ["Human", "Computer"]
        self.player1_select = tk.StringVar()
        self.player2_select = tk.StringVar()
        self.player1_select.set(player_list[0])
        self.player2_select.set(player_list[1])

        self.player_1_dropdown = tk.OptionMenu(frame, self.player1_select, *player_list)
        self.player_1_dropdown.place(anchor='s', rely=1, relx=0.166666)
        self.player_1_dropdown.config(bg="light gray")

        self.player_2_dropdown = tk.OptionMenu(frame, self.player2_select, *player_list)
        self.player_2_dropdown.place(anchor='s', rely=1, relx=0.83333)
        self.player_2_dropdown.config(bg="light gray")

        # create buttons(X/O and New Game)
        self.square_list = []
        for i in range(1, 10):
            self.board[i - 1] = tk.StringVar()
            square = tk.Button(frame, width=2, height=1, highlightthickness=0,
                               textvariable=self.board[i - 1], bg='gray', compound=tk.CENTER,
                               command=lambda i=i - 1: self.square_select(i))
            self.board[i - 1].set(self.start_board[i - 1])
            square.grid(column=(i - 1) % 3, row=(i - 1) // 3)
            square['font'] = ('Arial', 90)
            self.square_list.append(square)

        new_game_btn = tk.Button(frame, text="New\nGame", width=9, height=2, highlightbackground="#3E4149",
                                 highlightthickness=0, command=lambda: self.new_game())
        new_game_btn.place(relx=0.5, rely=0.995, anchor="s")
        new_game_btn['font'] = ('Arial', 19, 'bold')

        # create player labels
        self.x_label = tk.StringVar()
        player_1_label = tk.Label(frame, width=8, textvariable=self.x_label, bg="light gray")
        player_1_label.place(relx=0.03, rely=0.86)
        player_1_label['font'] = ('Arial', 18, 'bold')
        self.x_label.set("Player X({})".format(self.x_score))

        self.o_label = tk.StringVar()
        player_2_label = tk.Label(frame, width=8, textvariable=self.o_label, bg="light gray")
        player_2_label.place(relx=0.685, rely=0.86)
        player_2_label['font'] = ('Arial', 18, 'bold')
        self.o_label.set("Player O({})".format(self.o_score))

    def square_select(self, move):
        # creates board
        board = [self.board[i].get() for i in range(9)]

        # checks if square is empty or board is already won
        if self.win(board) is None and not board[move].isalpha():
            self.board[move].set(self.symbol)
            board[move] = self.symbol

            if self.symbol == "X":
                colour = 'dark blue'
            else:
                colour = 'dark red'
            self.square_list[move].config(fg=colour)

            # changes turns
            if self.symbol == "X":
                self.symbol = "O"
            else:
                self.symbol = "X"

            # checks if new move is a winner or tie
            if self.win(board) is not None:
                self.winner_screen(self.win(board))

            if self.num_empty_spaces() == 0:
                self.winner_screen(self.win(board))

        # makes computers move
        try:
            if self.symbol == "O" and self.player2 == "Computer":
                self.player_1_dropdown.after(500, self.square_list[self.o.ask_move(board)-1].invoke)

            if self.symbol == "X" and self.player1 == "Computer":
                self.player_1_dropdown.after(500,self.square_list[self.x.ask_move(board)-1].invoke)
        except:
            pass

    def winner_screen(self, winner):
        # create GUI
        screen = tk.Tk()
        screen.geometry('200x60')
        frame = tk.Frame(screen)
        frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        label = tk.Label(frame, text="")
        label.place(relx=0.15, rely=0.1)
        label['font'] = ("Arial", 15)
        ok_btn = tk.Button(frame, text="OK", command=lambda: screen.destroy(), highlightthickness=0, bg='gray')
        ok_btn.place(relx=0.5, rely=0.6, anchor='n')
        ok_btn['font'] = ("Arial", 15)

        # if game is a tie
        if winner is None:
            screen.title('Tie Game')
            label.config(text="      Draw game!")

        # if game has a winner
        else:
            screen.title("Winner")
            label.config(text=winner + " has won the game!")

            # Add to winners score
            if winner == "X":
                self.x_score += 1
                self.x_label.set("Player X({})".format(self.x_score))
            elif winner == "O":
                self.o_score += 1
                self.o_label.set("Player O({})".format(self.o_score))

        screen.mainloop()

    def new_game(self):
        # clears board and creates copy of board
        for i in range(9):
            self.board[i].set(" ")
        board = [self.board[i].get() for i in range(9)]

        # sets first turn to X
        self.player1 = self.player1_select.get()
        self.player2 = self.player2_select.get()
        self.symbol = "X"

        # creates computer players if needed
        if self.player1 == "Computer":
            self.x = Computer("X", game)
            if self.player2 == "Computer":
                self.o = Computer("O", game)
            self.square_list[self.x.ask_move(board)-1].invoke()

        if self.player2 == "Computer":
            self.o = Computer("O", game)

    def empty_squares(self):
        return ' ' in self.board

    @staticmethod
    def win(board):
        # row
        for i in range(0, 9, 3):
            if board[i] == board[i + 1] == board[i + 2] != " ":
                return board[i]

        # column
        for i in range(3):
            if board[i] == board[i + 3] == board[i + 6] != " ":
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
        num = 0
        for i in range(9):
            if self.board[i].get() == " ":
                num += 1
        return num


root = tk.Tk()
game = TicTacToe(root)
root.mainloop()
