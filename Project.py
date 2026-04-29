#Final Project 

def print_board(board):
    #creating the board for tic tace toe
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    for row in board: #checking for every row to see if there is a winning side 
        if row[0] == player and row[1] == player and row[2] == player:
            return True

    for columun in range(3): #checking for every columun to see if there is a winning side
        if (board[0][columun] == player and
            board[1][columun] == player and
            board[2][columun] == player):
            return True

    if (board[0][0] == player and board[1][1] == player and board[2][2] == player):
        return True #chekcing the diagonals to see if it a winning side

    if (board[0][2] == player and board[1][1] == player and board[2][0] == player):
        return True

    return False


def is_draw(board):
    for row in board:
        for cell in row:  #checks through each row and coloum to see if there is any empty space and if there none it return true indicating draw 
            if cell == " ":
                return False
    return True


def start_game():
    board = [[" " for _ in range(3)] for _ in range(3)] #craetes an empty board
    current_player = "X"
    final = False

    while not final:
        print_board(board)
        print("Player", current_player, "turn")

        valid_move = False  #checks to see if the move played is vaild

        while not valid_move:
            row_input = input("Enter row (0-2): ")    #asking for which row and colomun the player wants to position their move 
            columun_input = input("Enter column (0-2): ")

            if row_input.isdigit() and columun_input.isdigit():  #using the isdidgit method to check to see if the 
                row = int(row_input)
                columun = int(columun_input)  #converting it to a integer 

                if 0 <= row <= 2 and 0 <= columun <= 2: #checking to see if the move is vaild
                    if board[row][columun] == " ":
                        valid_move = True
                    else:
                        print("That spot is taken.")
                else:
                    print("Coordinates out of range.")
            else:
                print("Please enter numbers only.")

        board[row][columun] = current_player

        if check_winner(board, current_player):  #checking to see if the player won 
            print_board(board)
            print("Player", current_player, "wins!")
            final = True

        elif is_draw(board):  #checking to see if there is a draw  
            print_board(board)
            print("It's a draw!")
            final = True

        else:
            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"


start_game()

def tic_tac_toe():
    play_again = "yes"                              

    #giving the chance to play again        

    while play_again.lower() == "yes":                     
        start_game()                                       
        play_again = input("Play again? (yes/no): ")      

    print("Thanks for playing!")  #final output 