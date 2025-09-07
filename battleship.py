import os

class Player:
    count = 1
    def __init__(self, name = "Player"):
        if name == "Player":
            self.name = f"{name} {Player.count}"
            Player.count += 1
        else:
            self.name = name

        self.board = [
    ['~' for i in range(10)],
    ['~' for i in range(10)],
    ['~' for i in range(10)],
    ['~' for i in range(10)],
    ['~' for i in range(10)],
    ['~' for i in range(10)],
    ['~' for i in range(10)],
    ['~' for i in range(10)],
    ['~' for i in range(10)],
    ['~' for i in range(10)],
        ]

        
    def __repr__(self):
        return f"{self.name}'s board:\n" + f"{self.default_board():^{3}}"
    

    def default_board(self):
        #Creating a default board

        strboard = ("   " + " ".join(f"{chr(65+i):^{3}}" for i in range(len(self.board[0]))) + "\n")
        for i , row in enumerate(self.board):
            strboard += (f"{i+1:^{3}}" + " ".join(f"{cell:^{3}}" for cell in row) + "\n")

        return strboard
    
    def place_ships(self, ship, start, end):

        self.ship = ship
        self.start = start  
        self.end = end

        self.ships = {
            "Carrier": 1,
            "Battleship": 1,
            "Cruiser": 1,
            "Submarine": 1,
            "Destroyer": 1
        }

        if self.ships.get(ship):
            if ship == "Carrier":
                length = 5
            elif ship == "Battleship":
                length = 4
            elif ship == "Cruiser":
                length = 3
            elif ship == "Submarine":
                length = 3
            elif ship == "Destroyer":
                length = 2

            #coordinates
            x1, y1 = ord(start[0]) - 65, int(start[1]) - 1
            x2, y2 = ord(end[0]) - 65, int(end[1]) - 1

            if x1 == x2:
                for i in range(length):
                    if (abs(y1 - y2)) == length -1:
                        self.board[y1 + i][x1] = "^"
            elif y1 == y2:
                for i in range(length):
                    if (abs(x1 - x2)) == length -1:
                        self.board[y1][x1 + i] = "^"

            else:
                print("Invalid placement. Ships must be placed either horizontally or vertically.")

#Example usage
player_1 = Player()
print(player_1)
player_2 = Player()
print(player_2)

print("Placing ship... " + "You have five ships to place. " + "The ships are: Carrier (5), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).\n")
print("Numbers measure the length of the ship.\n")

start = input("Enter the starting coordinate of your Carrier (e.g., A1): ").upper()
end = input("Enter the ending coordinate of your Carrier (e.g., A5): ").upper()
start = [start[0], start[1:]]
end = [end[0], end[1:]]
player_1.place_ships("Carrier", start, end)
print(player_1)

