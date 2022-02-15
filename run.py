from random import randint
from pprint import pprint

# Legend
# "*" for placing ship
# " " for available space
# "X" for hit battleship
# "-" for missed shot

# Code based on Knowledge Mavens videos, link in README
# LENGTH_OF_SHIPS = [3,6,3,4,5]

# create list of 9 spaces, 9 times
HIDDEN_BOARD = [[" "] * 9 for x in range(9)]
# create list of 9 spaces, 9 times
GUESS_BOARD = [[" "] * 9 for x in range(9)]
# create list of 9 spaces, 9 times
PLAYER_BOARD = [[" "] * 9 for x in range(9)]


def print_board(board):

    print("  A B C D E F G H I")
    print("  ----------------")
    row_number = 1
    for row in board:
        print(row_number, "|".join(row))
        row_number += 1

letters_to_numbers = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7,
    "I": 8,
}


numbers_to_letters = {
    0: "A",
    1: "B",
    2: "C",
    3: "D",
    4: "E",
    5: "F",
    6: "G",
    7: "H",
    8: "I",
}

user_score = 0

# def print_board(board):

#     print("  A B C D E F G H I")
#     print("  ----------------")
#     row_number = 1
#     for row in board:
#         print(row_number, "|".join(row))
#         row_number += 1


# Create ships
def create_ships(board):

    for ship in range(5):
        ship_row, ship_column = randint(0, 8), randint(0, 8)
        while board[ship_row][ship_column] == "*":
            ship_row, ship_column = randint(0, 8), randint(0, 8)
        board[ship_row][ship_column] = "*"


def get_ship_location():
    row = input("Enter the row of the ship: ").upper()
    while row not in "123456789":
        print('Not an appropriate choice, please select a valid row')
        row = input("Enter the row of the ship: ").upper()
    column = input("Enter the column of the ship: ").upper()
    while column not in "ABCDEFGHI":
        print('Not an appropriate choice, please select a valid column')
        column = input("Enter the column of the ship: ").upper()
    return int(row) - 1, letters_to_numbers[column]


# def validate_column(values):
    
#     try:
#         [int(value) for value in values]
#         if values not in continue_playing_options:
#             print("Please number between 1-9 '{values}'.")
#     except:
#         print("Please number between 1-9, please try again.\n")
#         return False
#     return True

# def validate_row(values):
    
#     try:
#         [int(value) for value in values]
#         if values not in continue_playing_options:
#             print("Please enter letter between A and I '{values}'.")
#     except:
#         print("Please enter letter between A and I, please try again.\n")
#         return False
#     return True




def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "*":
                count = 1
    return count


# Begin game and enter name


def start():

    # create_ships(HIDDEN_BOARD)
    # create_ships(PLAYER_BOARD)

    print("five ships have invaded our territorial waters")
    print("You need to shoot well to save our island")

    global username
    username = input("Sailor what is your name:\n")
    while username == "" or username == " ":
        print("Sailor please enter your name.")
        username = input("Sailor what is your name:\n")

def start_game():
    turns = 20
    global user_score


    while turns > 0:
        
        print_board(GUESS_BOARD)
        print_board(HIDDEN_BOARD)
        row, column = get_ship_location()
        if GUESS_BOARD[row][column] == "-" or GUESS_BOARD[row][column] == "X":
            print("Don't waste a shot you've already missed")
        elif HIDDEN_BOARD[row][column] == "*":
            print("Congratulations {username}, Direct hit, congratulations")
            GUESS_BOARD[row][column] = "X"
            turns -= 1
            user_score = 1

        else:
            print("Oh no, you missed")
            print("Better luck next time {username}")
            GUESS_BOARD[row][column] = "-"
            turns -= 1
        

        if turns == 10:
            print("You have used half your torpedoes")

        if turns == 1:
            print("Last shot, make it count")

        if count_hit_ships(GUESS_BOARD) == 5:
            print("{username} your country owes you a debt of grattitude")
            print("you have sunk all of the battleships, and saved our country from certain invasion")
            print("Game over")

        if count_hit_ships(PLAYER_BOARD) == 5:
            print("Sorry {username}, you've lost")

        # continue_playing = input("Do you want to continue playing? y/n\n")
        #     while continue_playing not in continue_playing_choice:
        #         validate_continue_playing(continue_playing)
        #         continue_playing = input(
        #             "Do you want to continue playing? y/n\n")
        #     if continue_playing == "y" or continue_playing == "yes":
        #         print("You have decided to continue playing the game.")
        #         continue
        #     elif continue_playing == "n" or continue_playing == "no":
        #         print("You have decided to finish playing, the game is now over")
        #     else:
        #         print("Sorry, please can you enter y/n")
        #         continue_playing = input("Do you want to continue playing? y/n \n")

start()
start_game()



# print("print board hidden board")
# print_board(HIDDEN_BOARD)
# print("print board guess board")
# print_board(GUESS_BOARD)
