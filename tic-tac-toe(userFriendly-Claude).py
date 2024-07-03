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


def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Welcome to Tic Tac Toe!")
    print("Players take turns entering a number from 1-9 to make their move.")

    while True:
        print_board(board)
        while True:
            try:
                move = int(input(f"Player {current_player}, enter your move (1-9): "))
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

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins! Congratulations!")
            break
        elif is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

    play_again = input("Do you want to play again? (yes/no): ").lower().strip()
    if play_again == "yes" or play_again == "y":
        play_tic_tac_toe()
    else:
        print("Thanks for playing!")


if __name__ == "__main__":
    play_tic_tac_toe()