from random import randint

# Game board - 10 x 10

def create_board(board)
    for i in range(10):
        board.append ([" x "]*10)
    return board

# Starting game
print ("Are you ready to defend our waters?")
print ("4 ships need to be sunk")
print ("You have 50 torpedoes, choose your shots carefully")
print_board(board)


# Create ships
def create_ships(board):
    ship_number = 0
    

# Create position
def random_number(board):
    return randint(0, len(board)-1)

def get_ship_position():
    ship_number = 0
    while ship_number < 5:
        ship_row = random_number(board)
        ship_column = random_number(board)
        

# Take first shot
print ("Take your first shot")

# Hit or miss
def count_hit_ships(board):


# Win or loose


