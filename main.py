import os

board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


def display_board(board):
    # Displays the board
    for row in board:
        print("|".join(row))
        print("-" * 5)


def get_player_input():
    # Getting player move and checking to make sure it is valid
    while True:
        try:
            row = int(input("Enter the row (0, 1, or 2): "))
            col = int(input("Enter the column (0, 1, or 2): "))
            if 0 <= row <= 2 and 0 <= col <= 2:
                return row, col
            else:
                print("Invalid input. Row and column must be between 0 and 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def update_board(board, row, col, player):
    # Updating the board with players move
    if board[row][col] == ' ':
        board[row][col] = player
        os.system("cls")
    else:
        print("That spot is already taken. Try again.")


def check_win(board):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return True
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return True
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True
    return False


def check_draw(board):
    # Check if the board is full without a winner
    for row in board:
        if ' ' in row:
            return False
    return True


def switch_player(player):
    # Switches between players
    return 'X' if player == 'O' else 'O'


while True:
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        display_board(board)
        print("Player", current_player)
        player_input = get_player_input()
        update_board(board, player_input[0], player_input[1], current_player)
        if check_win(board):
            display_board(board)
            print("Player", current_player, "wins!")
            break
        if check_draw(board):
            display_board(board)
            print("It's a draw!")
            break
        current_player = switch_player(current_player)

    play_again = input("Play again? (yes/no): ").lower()
    if play_again != 'yes':
        break
