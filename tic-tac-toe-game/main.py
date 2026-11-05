import random
board_state = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

possible_players = ["p", "c"]
options = ["x", "o"]

WINNING_COMBO = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

def display_board(state):
    print(f"     {state[0]}     |      {state[1]}     |      {state[2]}    ")
    print("-------------------------------------")
    print(f"     {state[3]}     |      {state[4]}     |      {state[5]}    ")
    print("-------------------------------------")
    print(f"     {state[6]}     |      {state[7]}     |      {state[8]}    ")

def player_option(player_type):
    if player_type == "p":
        while True:
            player_choice = input("Make a choice ['x' or 'o']: ").lower()
            if player_choice in options:
                return player_choice
            print(f"{player_type} invalid choice, please choose between ['x', 'o']")


    elif player_type == "c":
        computer_choice = random.choice(options)
        return computer_choice

def game_moves(choice, player):
    if player == "p":
        while True:
            player_placement = input("Pick a valid spot on the board (1 - 9): ")
            if player_placement.isdigit() or board_state[int(player_placement) - 1] == " " and 1 <= int(player_placement) <= 9:
                board_state[int(player_placement) - 1] = choice
                return

            print(f"{player_placement} spot is occupied or invalid")

    elif player == "c":
        while True:
            computer_placement = random.randint(0, len(board_state) - 1)
            if board_state[computer_placement] == " ":
                board_state[computer_placement] = choice
                return

def game_results(board, choice):
    for combo in WINNING_COMBO:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == choice:
            return True

    return False

def validate_player(player_label):
    while True:
        player_type = input(f"{player_label}[press 'p' for human or 'c' for computer]: ").lower()
        if player_type in possible_players:
            return player_type
        print("Invalid choice, please choose between ['p', 'c']")

def game():
    player_1 = validate_player("player_1")
    player_2 = validate_player("player_2")

    player1_choice = player_option(player_1)
    player2_choice = "x" if player1_choice == "o" else "o"

    current_player = player_1
    current_choice = player1_choice
    player_label = "Player 1"

    while " " in board_state:
        print("\n" * 3)
        display_board(board_state)

        game_moves(current_choice, current_player)

        if game_results(board_state, current_choice) == True:
            display_board(board_state)
            print(f"{player_label} with choice '{current_choice}' wins!")
            break

        if current_player == player_1:
            current_player = player_2
            current_choice = player2_choice
            player_label = "Player 2"
        else:
            current_player = player_1
            current_choice = player1_choice
            player_label = "Player 1"

    else:
        display_board(board_state)
        print("The board is full! It's a draw game!")


while True:
    game()

    play_game = input("Do you want to play again? [y/n]: ").lower()

    if play_game == "y":
        continue
    break