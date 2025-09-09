import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

class Player:

    def __init__(self, name, count = 1):

        self.count = count
        if name == "":
            self.name = f"Player {self.count}"
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

        self.attack_board = [
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

        self.ships_status = {
            "Carrier": ["^","^","^","^","^"],
            "Battleship": ["^","^","^","^"],
            "Cruiser": ["^","^","^"],
            "Submarine": ["^","^","^"],
            "Destroyer": ["^","^"]
        }

        self.ships_pos = {}

        self.ships_menu = {
            "Carrier": {"length": 5, "placed": False}, 
            "Battleship": {"length": 4, "placed": False}, 
            "Cruiser": {"length": 3, "placed": False}, 
            "Submarine": {"length": 3, "placed": False}, 
            "Destroyer": {"length": 2, "placed": False}
        }

        
    def __repr__(self):

        return f"{self.name}'s board:\n\n" + f"{self.default_board()} \nAttack board:\n\n" + f"{self.playing_board()}"


    def default_board(self):

        strboard = ("   " + " ".join(f"{chr(65+i):^{3}}" for i in range(len(self.board[0]))) + "\n")
        for i , row in enumerate(self.board):
            strboard += (f"{i+1:^{3}}" + " ".join(f"{cell:^{3}}" for cell in row) + "\n")

        return strboard
    
    def playing_board(self):

        strboard = ("   " + " ".join(f"{chr(65+i):^{3}}" for i in range(len(self.attack_board[0]))) + "\n")
        for i , row in enumerate(self.attack_board):
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
                self.ships_menu[self.ship]["placed"] = True

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
                self.ships_menu[self.ship]["placed"] = True

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

#Start of the game

print("Welcome to Battleship!\n")
name_1 = input("Enter the name of player 1: ").strip()
if name_1 == "":    
    player_1 = Player(name_1)
else:
    player_1 = Player(name_1)

name_2 = input("Enter the name of player 2: ").strip()
if name_2 == "":
    player_2 = Player(name_2, count = 2)
    print("\nInvalid name. Player 2 will be named 'Player 2'. \n")
else:
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

        while 1 in player_1.ships.values():

            print(player_1)
            remaining_ships = [ship for ship, status in player_1.ships_menu.items() if status["placed"] == False]
            remaining_ships_length = [size['length'] for ship, size in player_1.ships_menu.items() if size["placed"] == False]

            print("\nPlacing ships... " + f"You have {len(remaining_ships)} ships to place. "\
                   + f"The ships are: {", ".join(f"{name} ({size})" for name, size in zip(remaining_ships, remaining_ships_length))}.")
            print("Numbers measure the length of the ship.\n")

            ship = input(f"Enter the name of the ship you want to place {", ".join(remaining_ships)}: ").title()

            if ship not in player_1.ships:

                clear_console()
                print(f"Invalid ship name. Please choose from {", ".join(remaining_ships)}.\n")
                continue

            elif ship in player_1.ships and player_1.ships[ship] == 1:
        
                start = input(f"Enter the starting coordinate of your {ship} (e.g., A1): ").upper()

                if start == "":
                    clear_console()
                    print("Invalid coordinate. Please enter a valid coordinate (e.g., A1).")
                    continue

                elif len(start) < 2 or len(start) > 3 or not start[0].isalpha() or not start[1:].isdigit():
                    clear_console()
                    print("Invalid coordinate. Please enter a valid coordinate (e.g., A1).")
                    continue

                end = input(f"Enter the ending coordinate of your {ship} (e.g., A5): " ).upper()

                if end == "":
                    clear_console()
                    print("Invalid coordinate. Please enter a valid coordinate (e.g., A1).")
                    continue

                elif len(end) < 2 or len(end) > 3 or not end[0].isalpha() or not end[1:].isdigit():
                    clear_console()
                    print("Invalid coordinate. Please enter a valid coordinate (e.g., A1).")
                    continue

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

        while 1 in player_2.ships.values():

            print(player_2)
            remaining_ships = [ship for ship, status in player_2.ships_menu.items() if status["placed"] == False]
            remaining_ships_length = [size['length'] for ship, size in player_2.ships_menu.items() if size["placed"] == False]

            print(f"\nPlacing ships... " + f"You have {len(remaining_ships)} ships to place. "\
                   + f"The ships are: {", ".join(f"{name} ({size})" for name, size in zip(remaining_ships, remaining_ships_length))}.")
            print("Numbers measure the length of the ship.\n")

            ship = input(f"Enter the name of the ship you want to place {", ".join(remaining_ships)}: ").title()

            if ship not in player_2.ships:

                clear_console()
                print(f"Invalid ship name. Please choose from {", ".join(remaining_ships)}.\n")
                continue
 
            elif ship in player_2.ships and player_2.ships[ship] == 1:

                start = input(f"Enter the starting coordinate of your {ship} (e.g., A1): ").upper()

                if start == "":
                    clear_console()
                    print("Invalid coordinate. Please enter a valid coordinate (e.g., A1).")
                    continue

                elif len(start) < 2 or len(start) > 3 or not start[0].isalpha() or not start[1:].isdigit():
                    clear_console()
                    print("Invalid coordinate. Please enter a valid coordinate (e.g., A1).")
                    continue

                end = input(f"Enter the ending coordinate of your {ship} (e.g., A5): " ).upper()

                if end == "":
                    clear_console()
                    print("Invalid coordinate. Please enter a valid coordinate (e.g., A1).")
                    continue

                elif len(end) < 2 or len(end) > 3 or not end[0].isalpha() or not end[1:].isdigit():
                    clear_console()
                    print("Invalid coordinate. Please enter a valid coordinate (e.g., A1).")
                    continue
            else:

                clear_console()
                print("You have already placed this ship. Please choose a different ship.\n")
    

            start = [start[0], start[1:]]
            end = [end[0], end[1:]]
        
            clear_console()
            player_2.place_ships(ship, start, end)
        

print("\n", player_1)      
print("\n", player_2)
