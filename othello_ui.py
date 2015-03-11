# Project 4: Othello Console User Interface

import othello_game_logic

def main():
    print('Enter an even integer b/t 4 and 16 inclusive')
    row = get_int('ROW')
    col = get_int('COL')
    print('Enter [W]hite or [B]lack')
    top_left = get_letter('TOP LEFT CORNER')
    turn = get_letter('STARTING PLAYER')
    print('Enter [Y]es or [N]o')
    most = get_most('MOST TILES')

    game_state = othello_game_logic.OthelloGame(row, col, top_left, turn, most)
    board = game_state.get_board()
    print_board(row, col, board)


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

if __name__ == '__main__':
    main()
