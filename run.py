from random import randint
from pprint import pprint

# Legend
# "*" for placing ship
# " " for available space
# "X" for hit battleship
# "-" for missed shot

# Code taken from Knowledge Mavens video,
# LENGTH_OF_SHIPS = [3,6,3,4,5]

HIDDEN_BOARD = [[" "] * 9 for x in range(9)]

GUESS_BOARD = [[" "] * 9 for x in range(9)]


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


def print_board(board):

    print("  A B C D E F G H I")
    print("  ----------------")
    row_number = 1
    for row in board:
        print(row_number, "|".join(row))
        row_number = 1


# Create ships
def create_ships(board):

    for ship in range(5):
        ship_row, ship_column = randint(0, 8), randint(0, 8)
        while board[ship_row][ship_column] == "*":
            ship_row, ship_column = randint(0, 8), randint(0, 8)
        board[ship_row][ship_column] = "*"


def get_ship_location():
    row = input("Please enter a ship row 1-9\n")
    while row not in "123456789" or len(row) > 1 or row == "":
        validate_row(row)
        print("Please enter a valid row")
        row = input("Please enter a ship row 1-9\n")
    column = input("Please enter a ship column A-I\n").upper()
    while column not in "ABCDEFGHI" or len(column) > 1 or column == "":
        validate_column(column)
        print("Please enter a valid column")
        column = input("Please enter a ship column A-I\n").upper()
    return int(row) - 1, letters_to_numbers[column]


# check
# def validate_column(values):
#     try:
#         if values not in letters_to_numbers:
#             print("Please choose a valid column")
    # except:
    #     print("Please choose a valid column\n")
    # return False
    # return True


# def validate_row(values):
#     try:
#         if values not in letters_to_numbers:
#             print("Please choose a valid row")
    # except:
    #     print("Please choose a valid row\n")
    # return False
    # return True


def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count = 1
    return count


# Begin game and enter name


def start_game():

    create_ships(HIDDEN_BOARD)
    create_ships(GUESS_BOARD)

    print("five ships have invaded our territorial waters")
    print("You need to shoot well to save our island")
    global username
    username = input("Sailor what is your name:\n")
    while username == "" or username == " ":
        print("Sailor please enter your name.")
        username = input("Sailor what is your name:\n")


turns = 20
global user_score


while turns > 0:
    print("{username}'s Board")
    print(USER_BOARD)
    print("Computer's Board")
    print_board(GUESS_BOARD)
    row, column = get_ship_location()
    if GUESS_BOARD[row][column] == "-" or GUESS_BOARD[row][column] == "X":
        print("Don't waste a shot you've already missed")
    elif HIDDEN_BOARD[row][column] == "*":
        print("Congratulations {username}, Direct hit, congratulations")
        GUESS_BOARD[row][column] = "X"
        turns -= 1
        computer_guess(USER_BOARD)
        user_score = 1

    else:
        print("Oh no, you missed")
        print("Better luck next time {username}")
        GUESS_BOARD[row][column] = "-"
        turns -= 1
        computer_guess(USER_BOARD)

    if turns == 10:
        print("You have used half your torpedoes")

    if turns == 19:
        print("Last shot, make it count")

    if count_hit_ships(GUESS_BOARD) == 5:
        print("{username} your country owes you a debt of grattitude")
        print(
            "you have sunk all of the battleships, and saved our country from certain invasion"
        )
        print("Game over")

    if count_hit_ships(USER_BOARD) == 5:
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




print("print board hidden board")
print_board(HIDDEN_BOARD)
print("print board guess board")
print_board(GUESS_BOARD)
