import numpy as np
from random import randint


class TicTacToe:

    def __init__(self, b, plsymb, cpsymb):
        self.b=b
        self.plsymb=plsymb
        self.cpsymb=cpsymb

    def gametime(self):
        player = randint(0, 1)
        self.simulate(player)

    def strategy(self):
        brd=np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]], dtype=int)
        for i in range(3):
            for j in range(3):
                if self.b[i][j] == self.plsymb:
                    brd[i][j]=1
                elif self.b[i][j] == self.cpsymb or self.b[i][j] == " ":
                    brd[i][j] = 0

        if brd[0, 0] + brd[1, 1] + brd[2, 2] >= 2 and self.full([self.b[0, 0], self.b[1, 1], self.b[2, 2]]) is False:
            j=self.compare([self.b[0, 0], self.b[1, 1],  self.b[2, 2]])
            return [j, j]
        elif brd[2, 0] + brd[1, 1] + brd[0, 2] >= 2 and self.full([self.b[2, 0], self.b[1, 1], self.b[0, 2]]) is False:
            j=self.compare([self.b[2, 0], self.b[1, 1], self.b[0, 2]])
            if j == 0:
                i=2
            elif j== 1:
                i=1
            else:
                i=0
            return [i, j]
        else:
            for i in range(3):
                if brd[i, 0] + brd[i, 1] + brd[i, 2] >= 2 and self.full([self.b[i, 0], self.b[i, 1], self.b[i, 2]]) is False:
                    j=self.compare([self.b[i, 0], self.b[i, 1], self.b[i, 2]])
                    return [i, j]
                elif brd[0, i] + brd[1, i] + brd[2, i] >= 2 and self.full([self.b[0, i], self.b[1, i], self.b[2, i]]) is False:
                    j=self.compare([self.b[0, i], self.b[1, i], self.b[2, i]])
                    return [i, j]
            else:
                while True:
                    row = randint(0, 2)
                    col = randint(0, 2)
                    if self.b[row][col] == " ":
                        break
                return [row, col]

    def compare(self, arr):
        i = arr.index(" ")
        return i

    def full(self, arr):
        for i in arr:
            if i == " ":
                return False
        return True

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
                        self.gamePlayer()
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

    def gamePlayer(self):
        print("Your turn. Insert first the row number, then the column number")
        row = int(input("Choose a row: "))
        col = int(input("Choose a column: "))
        self.b = self.board(self.plsymb, row - 1, col - 1)
        print("\n")
        return self.b

    def gameComputer(self):
        [row, col] = self.strategy()
        self.b = self.board(self.cpsymb, row, col)
        print("Computer chose:")
        self.graph()
        print("\n")
        return self.b

    def simulate(self, player):
        self.b = np.array([[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]], dtype=str)

        if player == 0:
            while self.whitespaces() is True and self.whoWins() is False:
                self.b = self.gamePlayer()
                if self.whoWins() is False and self.whitespaces() is True:
                    self.b = self.gameComputer()
                else:
                    break
        else:
            print("First is the computer!")
            while self.whitespaces() is True and self.whoWins() is False:
                self.b = self.gameComputer()
                if self.whoWins() is False and self.whitespaces() is True:
                    self.b = self.gamePlayer()
                else:
                    break

        self.graph()
        if self.whoWins() == self.plsymb:
            print("YOU WIN!!!")
        elif self.whoWins() == self.cpsymb:
            print("COMPUTER WON!!!")
        else:
            print("TIE")


print("Hello! Welcome to Tic Tac Toe. You are going to play against the computer.")
print("xoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxo \n\n")
print("Press x to play with X")
print("Press o to play with O ")
player_sb = input()
print(f"Great! You chose {player_sb}")
print("\n")

pawns = ["x", "o"]
if player_sb == pawns[0]:
    computer_sb = "o"
else:
    computer_sb = "x"


b=[]
game=TicTacToe(b, player_sb, computer_sb)
game.gametime()
