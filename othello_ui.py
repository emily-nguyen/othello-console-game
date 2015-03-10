# Project 4: Othello Console User Interface

def main():
    print('Enter an even integer b/t 4 and 16 inclusive')
    row = get_int('ROW')
    col = get_int('COL')
    print('Enter [W]hite or [B]lack')
    start = get_letter('STARTING PLAYER')
    top_left = get_letter('TOP LEFT CORNER')

def is_even(n:int)->bool:
    '''Returns true if n is even, false otherwise'''
    return (n%2 == 0)

def is_range(n:int)->bool:
    '''Returns true if n is in range 4 <= n <= 16, false otherwise'''
    return (4 <= n <= 16)

def is_letter(c:str)->bool:
    '''Returns true if c is W or B, false otherwise'''
    return (c == 'W' or c == 'B')

def get_int(s:str)->int:
    '''Gets the number of rows or columns from the user b/t 4 and 16 inclusive'''
    while True:
        try:
            value = int(input('{}: '.format(s)))
            if is_range(value) and is_even(value):
                break
            raise Exception
        except ValueError:
            print('ValueError: Enter an integer')
        except:
            print('Invalid {}. Please try again.'.format(s))
            print()

def get_letter(s:str)->str:
    '''Gets the letter of top left corner or start player'''
    while True:
        try:
            letter = input('{}: '.format(s)).strip().upper()
            if is_letter(letter):
                break
            raise exception
        except:
            print('Invalid {}. Please try again.'.format(s))
            print()

if __name__ == '__main__':
    main()
