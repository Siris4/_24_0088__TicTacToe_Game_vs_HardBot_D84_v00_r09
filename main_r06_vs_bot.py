import random

print("Welcome to Siris's Tic Tac Toe\n")


bot_difficulty_level = input("Please choose your difficulty level (1 = easy, 2 = medium, 3 = hard): ").lower()
while bot_difficulty_level not in ['1', '2', '3']:
    print("Invalid choice. Please choose 1 for easy, 2 for medium, or 3 for hard.")
    bot_difficulty_level = input("Please choose your difficulty level (1 = easy, 2 = medium, 3 = hard): ").lower()

if bot_difficulty_level == '1':
    difficulty = 'easy'
elif bot_difficulty_level == '2':
    difficulty = 'medium'
else:
    difficulty = 'hard'
print(f"You have selected {difficulty} difficulty.")

print("Player 1 is O. Player 2 is X.\n")

# Initial board setup
board_selection = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

# Function to print the board
def print_board(board_selection):
    print(f" {board_selection[0]} | {board_selection[1]} | {board_selection[2]}")
    print("-----------")
    print(f" {board_selection[3]} | {board_selection[4]} | {board_selection[5]}")
    print("-----------")
    print(f" {board_selection[6]} | {board_selection[7]} | {board_selection[8]}")

print_board(board_selection)

def check_index_for_winner(board_selection, marker):
    win_conditions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    # looping through each win condition to check:
    for condition in win_conditions:
        # if all 3 positions for a win condition are the same as the player's marker, consider it a win.
        if board_selection[condition[0]] == board_selection[condition[1]] == board_selection[condition[2]] == marker:
            return True
    return False

# Coin flip to decide who goes first
print("\nA coin is flipped.")
coin_result = random.randint(0, 1)
if coin_result == 0:
    current_player = "Player1"
    print(f"\nThe coin landed on heads! Player 1 goes first.")
else:
    current_player = "Player2"
    print(f"\nThe coin landed on tails! Player 2 goes first.")

# Function for Player 1's (human) turn
def player1_turn(board_selection):
    while True:
        player1_choice = input("\nPlease choose which number you want to place your O (between 1-9): \n")
        if player1_choice.isdigit() and int(player1_choice) in range(1, 10):
            index_spot_chosen = int(player1_choice) - 1  # Convert chosen number to board index
            if board_selection[index_spot_chosen] not in ['X', 'O']:
                board_selection[index_spot_chosen] = 'O'
                break  # Break out of the loop after a valid move
            else:
                print("That spot is already taken. Please select a different spot.")
        else:
            print("You must choose a number between 1-9.")

# Function for Player 2's (computer) turn
def player2_turn(board_selection):
    while True:
        computer_choice = random.randint(1, 9)
        index_spot_chosen = computer_choice - 1  # Convert computer's choice to board index
        if board_selection[index_spot_chosen] not in ['X', 'O']:
            board_selection[index_spot_chosen] = 'X'
            print(f"\nThe computer placed its X on spot {computer_choice}\n")
            break  # Break after a valid move

# main game loop:
while True:
    if current_player == "Player1":
        player1_turn(board_selection)
        print_board(board_selection)
        if check_index_for_winner(board_selection, 'O'):
            print("\nPLAYER 1 WINS!")
            break # exits loop after a win
        current_player = "Player2"  # switches to player2
    else:
        # current_player == "Player2":
        player2_turn(board_selection)
        print_board(board_selection)
        if check_index_for_winner(board_selection, 'X'):
            print("\nPLAYER 2 WINS!")
            break # exits loop after a win
        current_player = "Player1" # switches back to player1




