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


# Function to check if a player has won
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

    for condition in win_conditions:
        if board_selection[condition[0]] == board_selection[condition[1]] == board_selection[condition[2]] == marker:
            return True
    return False


# Function to check if the board is full (for tie condition)
def check_full_board(board_selection):
    return all(spot in ['X', 'O'] for spot in board_selection)


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


# Helper functions for the hard bot logic
def find_winning_move(board_selection, marker):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]

    # Check for a winning move
    for condition in win_conditions:
        if board_selection[condition[0]] == board_selection[condition[1]] == marker and board_selection[
            condition[2]] not in ['X', 'O']:
            return condition[2]
        if board_selection[condition[0]] == board_selection[condition[2]] == marker and board_selection[
            condition[1]] not in ['X', 'O']:
            return condition[1]
        if board_selection[condition[1]] == board_selection[condition[2]] == marker and board_selection[
            condition[0]] not in ['X', 'O']:
            return condition[0]
    return None


def find_blocking_move(board_selection, player_marker, bot_marker):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]

    # Priority 1: Can the bot win?
    winning_move = find_winning_move(board_selection, bot_marker)
    if winning_move is not None:
        return winning_move

    # Priority 2: Block the player from winning
    blocking_move = find_winning_move(board_selection, player_marker)
    if blocking_move is not None:
        return blocking_move

    # Priority 3: Set up 2 in a row for future offense
    # Try to find a spot that sets up the bot to potentially win in a future turn
    for condition in win_conditions:
        # If one of the bot's markers is in the line and the others are empty, try to set up for 2 in a row
        if board_selection[condition[0]] == bot_marker and board_selection[condition[1]] not in ['X', 'O'] and \
                board_selection[condition[2]] not in ['X', 'O']:
            return condition[1] if board_selection[condition[1]] != bot_marker else condition[2]
        if board_selection[condition[1]] == bot_marker and board_selection[condition[0]] not in ['X', 'O'] and \
                board_selection[condition[2]] not in ['X', 'O']:
            return condition[0] if board_selection[condition[0]] != bot_marker else condition[2]
        if board_selection[condition[2]] == bot_marker and board_selection[condition[0]] not in ['X', 'O'] and \
                board_selection[condition[1]] not in ['X', 'O']:
            return condition[1] if board_selection[condition[1]] != bot_marker else condition[0]

    return None


# Function for Player 2's (computer) turn
def player2_turn(board_selection, difficulty):
    bot_marker = 'X'
    player_marker = 'O'

    if difficulty == 'hard':
        # Step 1: Always pick the center (5) if available and it's the bot's first move
        if board_selection[4] == '5':
            board_selection[4] = bot_marker
            print(f"\nThe computer placed its X on spot 5 (center).\n")
            return

        # Step 2: Prioritize winning or blocking moves, else make a strategic setup move
        best_move = find_blocking_move(board_selection, player_marker, bot_marker)
        if best_move is not None:
            board_selection[best_move] = bot_marker
            print(f"\nThe computer placed its X on spot {best_move + 1}.\n")
            return

    # If no strategic or blocking move is found, make a random move
    while True:
        computer_choice = random.randint(1, 9)
        index_spot_chosen = computer_choice - 1  # Convert computer's choice to board index
        if board_selection[index_spot_chosen] not in ['X', 'O']:
            board_selection[index_spot_chosen] = bot_marker
            print(f"\nThe computer placed its X on spot {computer_choice}\n")
            break  # Break after a valid move


# Main game loop
while True:
    if current_player == "Player1":
        player1_turn(board_selection)
        print_board(board_selection)
        if check_index_for_winner(board_selection, 'O'):
            print("\nPLAYER 1 WINS!")
            break  # exits loop after a win
        elif check_full_board(board_selection):
            print("\nIt's a tie!")
            break  # exits loop after a tie
        current_player = "Player2"  # switches to player2
    else:
        # current_player == "Player2":
        player2_turn(board_selection, difficulty)
        print_board(board_selection)
        if check_index_for_winner(board_selection, 'X'):
            print("\nPLAYER 2 WINS!")
            break  # exits loop after a win
        elif check_full_board(board_selection):
            print("\nIt's a tie!")
            break  # exits loop after a tie
        current_player = "Player1"  # switches back to player1
