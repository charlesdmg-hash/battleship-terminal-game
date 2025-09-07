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


class Player:
    count = 1
    def __init__(self, name = "Player"):
        if name == "Player":
            self.name = f"{name} {Player.count}"
            Player.count += 1
        else:
            self.name = name

        
    def __repr__(self):
        return f"{self.name}'s board:\n" + f"{self.default_board()}"
    

    def default_board(self):
        strboard = ("   " + "  ".join(chr(65+i) for i in range(len(board[0]))) + "\n")
        for i , row in enumerate(board):
            strboard += (f"{i+1:2} " + " ".join(row) + "\n")
        
        return strboard

    
player_1 = Player("Charles")
print(player_1)
        