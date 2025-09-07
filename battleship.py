import os

#Creating a default board
board = [
    ['～' for i in range(10)],
    ['～' for i in range(10)],
    ['～' for i in range(10)],
    ['～' for i in range(10)],
    ['～' for i in range(10)],
    ['～' for i in range(10)],
    ['～' for i in range(10)],
    ['～' for i in range(10)],
    ['～' for i in range(10)],
    ['～' for i in range(10)],
 ]

def default_board():
    print("   " + "  ".join(chr(65+i) for i in range(len(board[0]))))
    for i , row in enumerate(board):
        print(f"{i+1:2} " + " ".join(row))
    

class Player:
    count = 1
    def __init__(self, name = "Player"):
        if name == "Player":
            self.name = f"{name} {Player.count}"
            Player.count += 1
        else:
            self.name = name

        self.board = default_board()
        
default_board()
        