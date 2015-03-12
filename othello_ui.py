# Project 4: Othello Console User Interface

import othello_game_logic

def main():
    print('Enter an even integer b/t 4 and 16 inclusive')
    row = get_int('ROW')
    col = get_int('COL')
    top_left = get_letter('TOP LEFT CORNER')
    turn = get_letter('STARTING PLAYER')
    print('Enter [W]hite or [B]lack')
    print('Enter [Y]es or [N]o')
    most = get_most('MOST TILES')

    game_state = othello_game_logic.OthelloGame(row, col, turn, top_left, most)
    
    while game_state.get_winner() == None:
        print()
        print_score(game_state)
        print()
        board = game_state.get_board()
        print_board(row, col, board)
        print_turn(game_state)
        print()
        print('Make a move')
        print('Enter an even integer b/t 4 and 16 inclusive')
        while True:
            try:
                move_row = get_int('ROW')
                move_col = get_int('COL')
                game_state.make_move(move_row, move_col)
                break
            except:
                print('InvalidOthelloMoveError: Please try again')

    board = game_state.get_board()
    print_board(row, col, board)
    print('Game Over')
    print_score(game_state)
    print_winner(game_state)
    
def is_color(c:str)->bool:
    '''Returns true if c is W or B, false otherwise'''
    return (c == 'W' or c == 'B')

def is_letter(c:str)->bool:
    '''Returns true if c is Y or N, false otherwise'''
    return (c == 'Y' or c == 'N')

def get_int(s:str)->int:
    '''Gets the number of rows or columns from the user b/t 4 and 16 inclusive'''
    while True:
        try:
            value = int(input('{}: '.format(s)))
            return value
        except:
            print('Invalid {}. Please try again.'.format(s))
            print()

def get_letter(s:str)->str:
    '''Gets the letter of top left corner or start player'''
    while True:
        try:
            letter = input('{}: '.format(s)).strip().upper()
            if is_color(letter):
                return letter
            raise Exception
        except:
            print('Invalid {}. Please try again.'.format(s))
            print()

def get_most(s:str)->bool:
    '''Gets the win type of the game: most tiles or less tiles wins'''
    while True:
        try:
            most = input('{}: '.format(s)).strip().upper()
            if is_letter(most):
                if most == 'Y':
                    return True
                return False
            raise Exception
        except:
            print('Invalid {}. Please try again.'.format(s))
            print()

def print_score(game_state:othello_game_logic.OthelloGame)->None:
    '''Prints the current score (count) of black and white discs'''
    black = game_state.disc_count('B')
    white = game_state.disc_count('W')
    print('SCORE:\nBlack: {}\tWhite: {}'.format(black, white))

def print_board(row:int, col:int, board:[[str]])->None:
    '''Prints the othello game board'''
    print('  ', end='')
    
    for n in range(col):
        if n < 9:
            print(' ', end='')
            print(n+1, end='  ')
        else:
            print('', end=' ')
            print(n+1, end=' ')
    print()

    for r in range(row):
        if r < 9:
            print(r+1, end='  ')
        else:
            print(r+1, end=' ')
        for c in range(col):
            if board[r][c] == '':
                print('.', end='   ')
            else:
                print(board[r][c], end='   ')
        print()
    print()

def print_turn(game_state:othello_game_logic.OthelloGame)->None:
    '''Prints the current player's turn'''
    turn = game_state.get_turn()
    print("Player {}'s turn".format(turn))

def print_winner(game_state:othello_game_logic.OthelloGame)->None:
    '''Prints the winner based on most or less discs as indicated at start of game'''
    winner = game_state.get_winner()
    if winner == 'Tie':
        print("It's a tie.")
    print('{} is the winner!'.format(winner))

if __name__ == '__main__':
    main()