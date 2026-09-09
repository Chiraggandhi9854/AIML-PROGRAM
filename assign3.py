board = [" " for _ in range(9)]

def display():
    print("\n")
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])

def check_winner(player):
    wins = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    return any(all(board[i] == player for i in line) for line in wins)

player = "X"

for turn in range(9):
    display()
    position = int(input(f"Player {player}, enter position (1-9): ")) - 1

    if position < 0 or position > 8 or board[position] != " ":
        print("Invalid move!")
        continue

    board[position] = player

    if check_winner(player):
        display()
        print(f"Player {player} wins!")
        break

    player = "O" if player == "X" else "X"
else:
    display()
    print("It's a draw!")