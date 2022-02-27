import numpy as np
from random import randint


class TicTacToe:

    def __init__(self, b):
        self.b=b

    def gametime(self):
        print("Hello! Welcome to Tic Tac Toe. You are going to play against the computer.")
        print("xoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxo \n\n")
        print("Press x to play with X")
        print("Press o to play with O ")
        symbol = input()
        print(f"Great! You chose {symbol}")
        print("\n")
        player = randint(0, 1)
        self.simulate(symbol, player)

    def strategy(self):
        while True:
            row = randint(0, 2)
            col = randint(0, 2)
            if self.b[row][col] == " ":
                break
        return [row, col]

    def board(self, s, row, col):
        i = 0
        flag = True
        while i < 3:
            if flag is False:
                break
            j = 0
            while j < 3:
                if i == row and j == col:
                    if self.b[i][j] == " ":
                        self.b[i][j] = s
                        flag = False
                        break
                    else:
                        print("Not empty. Choose again wisely")
                        self.gamePlayer(s)
                else:
                    j += 1
            i += 1

        return self.b

    def whitespaces(self):
        if " " in self.b:
            return True
        else:
            return False

    def whoWins(self):

        win = ""

        if self.b[0, 0] == self.b[1, 1] == self.b[2, 2] and self.b[0, 0] != " ":
            win = self.b[0, 0]
        elif self.b[2, 0] == self.b[1, 1] == self.b[0, 2] and self.b[2, 0] != " ":
            win = self.b[2, 0]
        for i in range(3):
            if self.b[i, 0] == self.b[i, 1] == self.b[i, 2] and self.b[i, 0] != " ":
                win = self.b[i, 0]
            elif self.b[0, i] == self.b[1, i] == self.b[2, i] and self.b[0, i] != " ":
                win = self.b[0, i]

        if win != "":
            return win
        else:
            return False

    def graph(self):
        for i in range(3):
            for j in range(3):
                if j != 2:
                    print(f"{self.b[i][j]} |", end=" ")
                else:
                    print(f"{self.b[i][j]}")
            if i != 2:
                print("_________")

    def gamePlayer(self, s):
        print("Your turn. Insert first the row number, then the column number")
        row = int(input("Choose a row: "))
        col = int(input("Choose a column: "))
        self.b = self.board(s, row - 1, col - 1)
        print("\n")
        return self.b

    def gameComputer(self, s):
        [row, col] = self.strategy()
        self.b = self.board(s, row, col)
        print("Computer chose:")
        self.graph()
        print("\n")
        return self.b

    def simulate(self, s, player):
        self.b = np.array([[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]], dtype=str)
        pawns = ["x", "o"]

        if s == pawns[0]:
            ss = "o"
        else:
            ss = "x"

        if player == 0:
            while self.whitespaces() is True and self.whoWins() is False:
                self.b = self.gamePlayer(s)
                if self.whoWins() is False and self.whitespaces() is True:
                    self.b = self.gameComputer(ss)
                else:
                    break
        else:
            print("First is the computer!")
            while self.whitespaces() is True and self.whoWins() is False:
                self.b = self.gameComputer(ss)
                if self.whoWins() is False and self.whitespaces() is True:
                    self.b = self.gamePlayer(s)
                else:
                    break

        self.graph()
        if self.whoWins() == s:
            print("YOU WIN!!!")
        elif self.whoWins() == ss:
            print("COMPUTER WON!!!")
        else:
            print("TIE")




b=[]
game=TicTacToe(b)
game.gametime()