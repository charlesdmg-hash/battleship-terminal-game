import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

class Player:
    count = 1

    def __init__(self, name):

        if name == "":
            self.name = f"Player {Player.count}"
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
                            clear_console()
                            print("Invalid placement. Ships cannot overlap.")  
                            return
                        self.board[min(y1, y2) + i][x1] = "^"

                    else:
                        clear_console()
                        print("\nInvalid placement. The length of the ship does not match the coordinates provided.")
                        return
                self.ships[self.ship] -= 1

            elif y1 == y2:
                for i in range(length):
                    if (abs(x1 - x2)) == length -1:
                        if self.board[y1][min(x1, x2) + i] == "^":
                            clear_console() 
                            print("Invalid placement. Ships cannot overlap.")
                            return
                        self.board[y1][min(x1, x2) + i] = "^"
                        
                    else:
                        clear_console()
                        print("\nInvalid placement. The length of the ship does not match the coordinates provided.")
                        return
                self.ships[self.ship] -= 1

            else:
                clear_console()
                print("\nInvalid placement. Ships must be placed either horizontally or vertically.")

        if self.ship in self.ships:
            if self.ship == "Carrier" and self.ships[self.ship] > 0:
                length = 5
                coordinates(self.start, self.end, length)
                clear_console()
            elif self.ship == "Battleship" and self.ships[self.ship] > 0:
                length = 4
                coordinates(self.start, self.end, length)
                clear_console()
            elif self.ship == "Cruiser" and self.ships[self.ship] > 0:
                length = 3
                coordinates(self.start, self.end, length)
                clear_console() 
            elif self.ship == "Submarine" and self.ships[self.ship] > 0:
                length = 3
                coordinates(self.start, self.end, length)
                clear_console()
            elif self.ship == "Destroyer" and self.ships[self.ship] > 0:
                length = 2
                coordinates(self.start, self.end, length)
                clear_console()

print("Welcome to Battleship!\n")
name_1 = input("Enter the name of player 1: ").strip()
player_1 = Player(name_1)
name_2 = input("Enter the name of player 2: ").strip()
player_2 = Player(name_2)
print("\n")

    
turn = 0
while turn == 0:

    if all(value == 0 for value in player_1.ships.values()):
        turn += 1
        clear_console()
        print(f"{player_1.name}, you have placed all your ships!\n")
        input("Press Enter to continue...")
        clear_console()
        break
    
    else:

        print(player_1)
        print("\nPlacing ships... " + "You have five ships to place. " + "The ships are: Carrier (5), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).")
        print("Numbers measure the length of the ship.\n")

        ship = input("Enter the name of the ship you want to place (Carrier, Battleship, Cruiser, Submarine, Destroyer): ").title()

        if ship not in player_1.ships:

            clear_console()
            print("Invalid ship name. Please choose from Carrier, Battleship, Cruiser, Submarine, or Destroyer.\n")
            continue

        elif ship in player_1.ships and player_1.ships[ship] == 1:
        
            start = input(f"Enter the starting coordinate of your {ship} (e.g., A1): ").upper()
            end = input(f"Enter the ending coordinate of your {ship} (e.g., A5): " ).upper() 
            start = [start[0], start[1:]]
            end = [end[0], end[1:]]
        
            clear_console()
            player_1.place_ships(ship, start, end)
        
        else:

            clear_console()
            print("You have already placed this ship. Please choose a different ship.\n")


while turn == 1:

    if all(value == 0 for value in player_2.ships.values()):
        turn -= 1
        clear_console()
        print(f"{player_2.name}, you have placed all your ships!\n")
        input("Press Enter to continue...")
        clear_console()
        break
        
    else:

        print(player_2)
        print("\nPlacing ships... " + "You have five ships to place. " + "The ships are: Carrier (5), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).")
        print("Numbers measure the length of the ship.\n")

        ship = input("Enter the name of the ship you want to place (Carrier, Battleship, Cruiser, Submarine, Destroyer): ").title()

        if ship not in player_2.ships:

            clear_console()
            print("Invalid ship name. Please choose from Carrier, Battleship, Cruiser, Submarine, or Destroyer.\n")
            continue

        elif ship in player_2.ships and player_2.ships[ship] == 1:

            start = input(f"Enter the starting coordinate of your {ship} (e.g., A1): ").upper()
            end = input(f"Enter the ending coordinate of your {ship} (e.g., A5): " ).upper() 
            start = [start[0], start[1:]]
            end = [end[0], end[1:]]
        
            clear_console()
            player_2.place_ships(ship, start, end)
        
        else:

            clear_console()
            print("You have already placed this ship. Please choose a different ship.\n")
        

print("\n", player_1)      
print("\n", player_2)
