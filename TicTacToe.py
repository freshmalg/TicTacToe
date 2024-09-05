from IPython.display import clear_output
import TicTacToe_module



while True:
    #setup the game
    clear_output()
    print('Welcome to Tic Tac Toe!')
    
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    gameOver = False
    position = 0
    P1 = TicTacToe_module.player_input()
    P2 = ''
    if P1 == 'X':
        P2 = 'O'
    else:
        P2 = 'X'
        
    turn = TicTacToe_module.choose_first()
    
    game_on = TicTacToe_module.start_game()

    while game_on:
        clear_output()
        TicTacToe_module.display_board(board)
        print(f"Player {turn}'s turn.")     
        
        # Player1's turn.
        if turn == 1:
            position = TicTacToe_module.player_choice(board)
            board = TicTacToe_module.place_marker(board, P1, position)
            if TicTacToe_module.win_check(board, P1):
                clear_output()
                TicTacToe_module.display_board(board)
                print('Player 1 wins!')
                break
            else: 
                turn = 2
        # Player2's turn.
        elif turn == 2: 
            position = TicTacToe_module.player_choice(board)
            board = TicTacToe_module.place_marker(board, P2, position)
            if TicTacToe_module.win_check(board, P2):
                clear_output()
                TicTacToe_module.display_board(board)
                print('Player 2 wins!')
                break
            else:
                turn = 1
                

        # Draw
        if TicTacToe_module.full_board_check(board):
            clear_output()
            TicTacToe_module.display_board(board)
            print('Game is drawn!')
            break

    #end game
    if not game_on:
        break
    if not TicTacToe_module.replay():
        break                        