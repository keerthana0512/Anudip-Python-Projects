board = [ "-","-","-",
          "-","-","-",
          "-","-","-"]
def playboard():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])

def take_turn(player):
    print(player + "'s turn")
    position = input("Enter a number between 1 to 9 : ")
    while position not in ["1", "2","3","4","5","6","7","8","9"]:
        position = input("Invalid position. Choose between 0 to 9.")
    position = int(position)-1
    while board[position]!= "-":
        print("Position filled choose another position between 0 to 9.")
    board[position] = player
    playboard()
    
def check_game():
    if (board[0] == board[1] == board[2]!="-" or
        board[3] == board[4] == board[5]!="-" or
        board[6] == board[7] == board[8]!="-" or
        board[0] == board[3] == board[6]!="-" or
        board[1] == board[4] == board[7]!="-" or
        board[2] == board[5] == board[8]!="-" or
        board[0] == board[4] == board[8]!="-" or
        board[2] == board[4] == board[6]!="-"):
        return "win"
    elif "-" not in board:
        return "tie"
    else:
        return "play"
def game():
    playboard()
    current_player = "X"
    game_over = False
    while not game_over:
        take_turn(current_player)
        game_result = check_game()
        if game_result == "win":
            print(current_player + " wins!!!")
            game_over = True
        elif game_result == "tie":
            print("It's tie")
            game_over = True
        else:
            current_player = "O" if current_player == "X" else "X"
game()