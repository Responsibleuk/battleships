from pprint import pprint

# Game board - 10 x 10

COMPUTER = [[" "] * 10 for x in range(10)]
PLAYER = [[" "] * 10 for i in range(10)]

def print_board(board):
    print("  A B C D E F G H I J")
    print("  +-+-+-+-+-+-+-+-+-+")
    
letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    'I': 8,
    'J': 9
}

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


