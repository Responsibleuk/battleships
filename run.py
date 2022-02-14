from random import randint

# Legend
# "@" for placing ship
# " " for available space
# "X" for hit battleship
# "-" for missed shot
# Code taken from Knowledge Mavens video, 
HIDDEN_BOARD = [[" "] * 10 for x in range(8)]

GUESS_BOARD = [[" "] * 10 for x in range(8)]




letters_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4,
                      "F": 5, "G": 6, "H": 7, "I": 8, "J": 9}


numbers_to_letters = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E",
                      5: "F", 6: "G", 7: "H", 8: "I" 9: "J"}

def print_board(board):
    
   
    print("  A B C D E F G H I J")
    print("  -----------------")
    row_number = 1
    for row in board:
        print(row_number, "|".join(row))
        row_number += 1


