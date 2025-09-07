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

        self.ships = {
            "Carrier": 1,
            "Battleship": 1,
            "Cruiser": 1,
            "Submarine": 1,
            "Destroyer": 1
        }

        
    def __repr__(self):

        return f"{self.name}'s board:\n\n" + f"{self.default_board()}"
    

    def default_board(self):

        strboard = ("   " + " ".join(f"{chr(65+i):^{3}}" for i in range(len(self.board[0]))) + "\n")
        for i , row in enumerate(self.board):
            strboard += (f"{i+1:^{3}}" + " ".join(f"{cell:^{3}}" for cell in row) + "\n")

        return strboard
    
    def place_ships(self, ship, start, end):

        self.ship = ship
        self.start = start  
        self.end = end

        #coordinates
        def coordinates(start, end, length):
        
            x1, y1 = ord(start[0]) - 65, int(start[1]) - 1
            x2, y2 = ord(end[0]) - 65, int(end[1]) - 1

            if x1 == x2:
                for i in range(length):
                    if (abs(y1 - y2)) == length -1:
                        if self.board[min(y1, y2) + i][x1] == "^":
                            print("Invalid placement. Ships cannot overlap.")  
                            return
                        self.board[min(y1, y2) + i][x1] = "^"
                        self.ships[self.ship] -= 1
            elif y1 == y2:
                for i in range(length):
                    if (abs(x1 - x2)) == length -1:
                        if self.board[y1][min(x1, x2) + i] == "^":
                            print("Invalid placement. Ships cannot overlap.")
                            return
                        self.board[y1][min(x1, x2) + i] = "^"
                        self.ships[self.ship] -= 1

            else:
                print("\nInvalid placement. Ships must be placed either horizontally or vertically.")

        if self.ship in self.ships:
            if self.ship == "Carrier" and self.ships[self.ship] > 0:
                length = 5
                coordinates(self.start, self.end, length)
            elif self.ship == "Battleship" and self.ships[self.ship] > 0:
                length = 4
                coordinates(self.start, self.end, length)
            elif self.ship == "Cruiser" and self.ships[self.ship] > 0:
                length = 3
                coordinates(self.start, self.end, length)
            elif self.ship == "Submarine" and self.ships[self.ship] > 0:
                length = 3
                coordinates(self.start, self.end, length)
            elif self.ship == "Destroyer" and self.ships[self.ship] > 0:
                length = 2
                coordinates(self.start, self.end, length)
            else:
                print("You have already placed this ship or the ship name is invalid.")
        else:
            print("Invalid ship name. Please choose from Carrier, Battleship, Cruiser, Submarine, or Destroyer.")

#Example usage
player_1 = Player()
#print(player_1)
player_2 = Player()
#print(player_2)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    

while player_1.ships["Carrier"] > 0 or player_1.ships["Battleship"] > 0 or player_1.ships["Cruiser"] > 0 or player_1.ships["Submarine"] > 0 or player_1.ships["Destroyer"] > 0:
    print("\nPlacing ships... " + "You have five ships to place. " + "The ships are: Carrier (5), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).")
    print("Numbers measure the length of the ship.\n")

    ship = input("Enter the name of the ship you want to place (Carrier, Battleship, Cruiser, Submarine, Destroyer): ").title()

    if ship not in player_1.ships:
        clear_console()
        print("\nInvalid ship name. Please choose from Carrier, Battleship, Cruiser, Submarine, or Destroyer.")
        continue
    if player_1.ships[ship] == 0:
        clear_console() 
        print("You have already placed this ship. Please choose a different ship.")
        continue
    start = input(f"Enter the starting coordinate of your {ship} (e.g., A1): ").upper()
    end = input(f"Enter the ending coordinate of your {ship} (e.g., A5): " ).upper() 
    start = [start[0], start[1:]]
    end = [end[0], end[1:]]
    player_1.place_ships(ship, start, end)
    print("\n", player_1)

    
print("\n", player_2)
