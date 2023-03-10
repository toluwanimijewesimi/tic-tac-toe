# Tic Tac Toe game in python.

board = [' ' for x in range(10)]

def insert_letter(letter, position):
    """Place a letter on a position on the board."""
    board[position] = letter

def space_is_free(position):
    """Check if a space on the board is free."""
    return board[position] == ' '

def print_board(board):
    """Prints the board."""
    print(f'  {board[1]}  |  {board[2]}  |  {board[3]}  ')
    print(f'  {board[4]}  |  {board[5]}  |  {board[6]}  ')
    print(f'  {board[7]}  |  {board[8]}  |  {board[9]}  ')

def is_winner(bo, le):
    """Checks if there is a winner."""
    return (bo[1] == le and bo[2] == le and bo[3] == le) or\
    (bo[4] == le and bo[5] == le and bo[6] == le) or\
    (bo[7] == le and bo[8] == le and bo[9] == le) or\
    (bo[1] == le and bo[4] == le and bo[7] == le) or\
    (bo[2] == le and bo[5] == le and bo[8] == le) or\
    (bo[3] == le and bo[6] == le and bo[9] == le) or\
    (bo[1] == le and bo[5] == le and bo[9] == le) or\
    (bo[3] == le and bo[5] == le and bo[7] == le)

def player_move():
    """Allows the player to make a move."""
    run = True
    while run:
        move = input("\nSelect a position to place an 'X' (1-9): ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if space_is_free(move):
                    run = False
                    insert_letter('X', move)
                else:
                    print('This position is occupied, select a different one.')
            else:
                print('Please type a number within the range.')
        except:
            print('Please enter a number.')

def computer_move():
    """Allows the computer to make a move."""
    possible_moves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    # Checks if there is a move the computer can make to win,
    # if so it makes the move. 
    # Checks if there is a move the player can make to win,
    # if so it blocks the move.
    for let in ['O', 'X']:
        for i in possible_moves:
            board_copy = board[:]
            board_copy[i] = let  
            if is_winner(board_copy, let):
                move = i
                return move 

    # Checks if there are any open corners, if so,
    # the computer makes a move in a random one.
    corners_open = []
    for i in possible_moves:
        if i in [1, 3, 7, 9]:
            corners_open.append(i)

    if len(corners_open) > 0:
        move = select_random(corners_open)
        return move

    # Checks if the center is open, if so,
    # the computer makes a move in the center.
    if 5 in possible_moves:
        move = 5
        return move

    # Checks if the edges are open, if so,
    # the computer makes a move in a random one.
    edges_open = []
    for i in possible_moves:
        if i in [2, 4, 6, 8]:
            edges_open.append(i)

    if len(edges_open) > 0:
        move = select_random(edges_open)
    
    return move 


def select_random(li):
    """
    Selects a random item from a list for when the computer is making a move.
    """
    import random 
    ln = len(li)
    random = random.randrange(0, ln)
    return li[random]

def is_board_full(board):
    """Checks if the board is full to know if the game is a tie."""
    if board.count(' ') > 1:
        return False
    else:
        return True

def main():
    """Executes the game."""
    print('Welcome to Tic Tac Toe!\n')
    print_board(board)

    while not(is_board_full(board)):
        if not(is_winner(board, 'O')):
            player_move()
            print_board(board)
        else:
            print('\nYou Lost.')
            break

        if not(is_winner(board, 'X')):
            move = computer_move()
            insert_letter('O', move)
            print(f"\nThe computer placed an 'O' in position {move}.")
            print_board(board)
        else:
            print('\nYou Won!')
            break

    if is_board_full(board):
        print('\nTie Game!')

while True:
    answer = input('Do you want to play? (yes/no) ')
    if answer.lower() == 'yes':
        board = [' ' for x in range(10)]
        print('-----------------------------------')
        main()
    else:
        break