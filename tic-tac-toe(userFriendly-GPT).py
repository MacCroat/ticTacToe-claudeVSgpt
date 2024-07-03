def print_board(board):
    print("\n".join([" | ".join(row) for row in board]))
    print("\n")

def check_winner(board, player):
    # Check rows, columns and diagonals
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]]
    ]
    return [player, player, player] in win_conditions

def check_draw(board):
    return all(cell != " " for row in board for cell in row)

def get_valid_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value in [0, 1, 2]:
                return value
            else:
                print("Invalid input. Please enter 0, 1, or 2.")
        except ValueError:
            print("Invalid input. Please enter a number (0, 1, or 2).")

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Welcome to Tic Tac Toe!")
    print("Players take turns to place their marker (X or O) on the 3x3 grid.")
    print("The first player to get three in a row (horizontally, vertically, or diagonally) wins.")
    print("To place your marker, enter the row and column number (0, 1, or 2).")

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")

        row = get_valid_input("Enter the row (0, 1, or 2): ")
        col = get_valid_input("Enter the column (0, 1, or 2): ")

        if board[row][col] == " ":
            board[row][col] = current_player

            if check_winner(board, current_player):
                print_board(board)
                print(f"Congratulations! Player {current_player} wins!")
                break

            if check_draw(board):
                print_board(board)
                print("It's a draw!")
                break

            current_player = "O" if current_player == "X" else "X"
        else:
            print("This cell is already taken. Please choose another one.")

if __name__ == "__main__":
    main()
