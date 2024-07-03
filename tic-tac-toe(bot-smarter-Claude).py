import random


def print_board(board):
    print("\n")
    for i, row in enumerate(board):
        print(f" {' | '.join(cell if cell != ' ' else str(i * 3 + j + 1) for j, cell in enumerate(row))}")
        if i < 2:
            print("---+---+---")
    print("\n")


def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
                all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
            all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def is_full(board):
    return all(cell != " " for row in board for cell in row)


def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]


def bot_move(board, bot, player):
    # Check if bot can win
    for row, col in get_empty_cells(board):
        board[row][col] = bot
        if check_winner(board, bot):
            board[row][col] = " "
            return row, col
        board[row][col] = " "

    # Check if player can win and block
    for row, col in get_empty_cells(board):
        board[row][col] = player
        if check_winner(board, player):
            board[row][col] = " "
            return row, col
        board[row][col] = " "

    # Take center if available
    if board[1][1] == " ":
        return 1, 1

    # Take corners if available
    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    available_corners = [corner for corner in corners if board[corner[0]][corner[1]] == " "]
    if available_corners:
        return random.choice(available_corners)

    # Take any edge
    return random.choice(get_empty_cells(board))


def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    bot = "O"

    print("Welcome to Tic Tac Toe!")
    print("You are 'X'. Enter a number from 1-9 to make your move.")

    while True:
        print_board(board)

        if player == "X":  # Human player's turn
            while True:
                try:
                    move = int(input("Enter your move (1-9): "))
                    if 1 <= move <= 9:
                        row, col = divmod(move - 1, 3)
                        if board[row][col] == " ":
                            break
                        else:
                            print("That cell is already occupied. Try again.")
                    else:
                        print("Please enter a number between 1 and 9.")
                except ValueError:
                    print("Please enter a valid number.")
        else:  # Bot's turn
            print("Bot is making a move...")
            row, col = bot_move(board, bot, player)

        board[row][col] = player

        if check_winner(board, player):
            print_board(board)
            print(f"{'You win!' if player == 'X' else 'Bot wins!'}")
            break
        elif is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        player = bot if player == "X" else "X"

    play_again = input("Do you want to play again? (yes/no): ").lower().strip()
    if play_again == "yes" or play_again == "y":
        play_tic_tac_toe()
    else:
        print("Thanks for playing!")


if __name__ == "__main__":
    play_tic_tac_toe()