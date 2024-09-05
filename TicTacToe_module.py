import random

def display_board(board):
    print( '   |   |   ')
    print(f' {board[1]} | {board[2]} | {board[3]} ')
    print( '   |   |   ')
    print( '-----------')
    print( '   |   |   ')
    print(f' {board[4]} | {board[5]} | {board[6]} ')
    print( '   |   |   ')
    print( '-----------')
    print( '   |   |   ')
    print(f' {board[7]} | {board[8]} | {board[9]} ')
    print( '   |   |   ')

def place_marker(board, marker, position):
    board[position] = marker
    return board

def player_input():
    marker = ''
    while not marker in ['X','O']:
        marker = input("Player 1 chose 'X' or 'O': ").upper()
    return marker

def win_check(board, mark):
    winCombinations = ([1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7])
    
    for combination in winCombinations:
        for n in combination:
            win = True
            if board[n] != mark:
                win = False
                break
        if win:
            break
    return win            

def choose_first():
    first = random.randint(1,2)
    if first == 1:
        print('Player 1 starts.')
    else:
        print('Player 2 starts.')
    return first

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    full = True
    for position in board:
        if position == ' ':
            full = False
            break
    return full

def player_choice(board):
    choice = ''
    while not choice.isdigit():
        choice = input('Make your turn (1-9): ')
        if not choice.isdigit():
            print('Not a number! Try again.')
        elif not int(choice) in range(1,10):
            print('Position out of range! Try again.')
            choice = ''
        elif not space_check(board, int(choice)):
            print('Position is occupied! Try again.')
            choice = ''
    return int(choice)

def replay():
    choice = ''
    while not choice in ['Y','N']:
        choice = input('Do you want to play again? (Y/N): ').upper()
    return choice == 'Y'

def start_game():
    choice = ''
    while not choice in ['Y','N']:
        choice = input('Are you ready to start the game? (Y/N): ').upper()
    return choice == 'Y'