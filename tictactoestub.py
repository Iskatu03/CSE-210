

def main():
    ''' Holds the main game loop logic
        Selects a player
        Builds the board
        Loops through Players until a winner is found or game is over
        Displays results to user
        Thanks them for playing
        return: None
    '''
    # assign/get the first player
    player = next_player("")
    board = create_board()
    
    while not (is_winner(board) or is_draw(board)):
        display_board(board)
        make_move(player,board)
        player = next_player(player)
    display_board(board)
    print("Good game. Thanks for playing!")

    # create a board

    # loop if there isn't a winner or if the game isn't a draw

        # display the board

        # allow the player to make a move

        # pick the next player

    # display the final board

    # show message for winner and thanks for playing
    pass

def create_board():
    ''' Creates a list that holds the spots on the board
        It initializes the positions with the numbers for the person to pick
        return: the board as a list
    '''
    board_values = []
    for i in range(1,10):
        board_values.append(i)
    return board_values

def display_board(board):
    ''' Displays the current board
        return: None
    '''
    print()
    print(f'{board[0]}|{board[1]}|{board[2]}')
    print(f'-+-+-')
    print(f'{board[3]}|{board[4]}|{board[5]}')
    print(f'-+-+-')
    print(f'{board[6]}|{board[7]}|{board[8]}')
    return

def is_draw(board):
    ''' return: True if board is a draw, False if board is still playable '''
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False

    pass

def is_winner(board):
    ''' return: True if someone won, False if there is no winner '''
    return(board[0] == board[1] == board[2] or 
           board[3] == board[4] == board[5] or
           board[6] == board[7] == board[8] or
           board[0] == board[3] == board[6] or
           board[1] == board[4] == board[7] or
           board[2] == board[5] == board[8] or
           board[0] == board[4] == board[8] or
           board[2] == board[4] == board[6])     # use this to check every possible winning combination
    

def make_move(player, board):
    ''' Prompts player to select a square to play
        Assigns the player to that board location if it is a legal move
        return: None
    '''
    try:
        square = int(input(f'{player}\'s turn choose a square (1-9): '))

        if square > 9 or square < 1 or board[square-1] == "o" or board[square-1] == "x":
            raise ValueError()
        board[square - 1] = player
    except ValueError:
        print("Illegal Move")
        make_move(player, board)
        return


        

def next_player(current):
    ''' return: x if current is o, otherwise x '''
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"
    

# run main if this has been called from the command line
if __name__ == "__main__":
    main()
