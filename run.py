from random import randint

# Legend
# "H" for placing ship
# " " for available space
# "X" for hit battleship
# "-" for missed shot
# Code taken from Knowledge Mavens video, 
HIDDEN_BOARD = [[" "] * 9 for x in range(9))]

GUESS_BOARD = [[" "] * 9 for x in range(9)]




letters_to_numbers = {"A": 0 , "B": 1 , "C": 2 , "D": 3 , "E": 4 ,
                      "F": 5 , "G": 6 , "H": 7 , "I": 8}


numbers_to_letters = {0 : "A", 1 : "B", 2 : "C", 3 : "D", 4 : "E",
                      5 : "F", 6 : "G", 7 : "H", 8 : "I"}

def print_board(board):
    
   
    print("  A B C D E F G H I")
    print("  ----------------")
    row_number = 1
    for row in board:
        print(row_number, "|".join(row))
        row_number += 1


# Create ships
def create_ships(board):
    
   
    for ship in range(5):
        ship_row, ship_column = randint(0, 8), randint(0, 8)
        while board[ship_row][ship_column] == "H":
            ship_row, ship_column = randint(0, 8), randint(0, 8)
        board[ship_row][ship_column] = "H"





def get_ship_position():
 
    row = input("Please enter a ship row 1-9\n")
    while row not in "123456789" or len(row) > 1 or row == "":
        validate_row(row)
        print("Please enter a valid row")
        row = input("Please enter a ship row 1-9\n")
    column = input("Please enter a ship column A-I\n”).upper()
    while column not in "ABCDEFGHI" or len(column) > 1 or column == "":
        validate_column(column)
        print("Please enter a valid column")
        column = input("Please enter a ship column A-I\n").upper()
    return int(row) - 1, letters_to_numbers[column]



# Column = input(‘Enter column’)
# 	while row not in ’ABCDEFGH’ :
# 		print(‘try again, enter column A-J’)
# 		Column = input(‘Enter column’)

# Return int(row) - 1, letters_to_numbers[column]

print("print board hidden board")
print_board(HIDDEN_BOARD)
print("print board guess board")
print_board(GUESS_BOARD)