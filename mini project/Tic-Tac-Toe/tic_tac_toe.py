# tic_tac_toe game

board = [' '] * 9


def draw_board():
    print("--------------")
    print("|", board[0], "|", board[1], "|", board[2], "|")
    print("--------------")
    print("|", board[3], "|", board[4], "|", board[5], "|")
    print("--------------")
    print("|", board[6], "|", board[7], "|", board[8], "|")
    print("--------------")


def check_winner():
    # Check rows for winner
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] != ' ':
            return True

    # Check columns for winner
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] != ' ':
            return True

    # Check diagonals for winner
    if board[0] == board[4] == board[8] != ' ':
        return True
    if board[2] == board[4] == board[6] != ' ':
        return True

    return False


current_player = 'X'

while True:
    draw_board()
    print("It's", current_player, "'s turn.")
    move = input("Enter your move (0-8): ")

    move = int(move)

    if 0 <= move <= 8 and board[move] == ' ':
        board[move] = current_player
        if check_winner():
            draw_board()
            print("Congratulations! You win!")
            break
        elif ' ' not in board:
            draw_board()
            print("It's a tie!")
            break
        else:
            current_player = 'O' if current_player == 'X' else 'X'
    else:
        print("Invalid move. Try again.")
