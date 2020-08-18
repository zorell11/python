import random

BOARD = [['', '', ''],
        ['', '', ''],
        ['', '', '']]
PLAYER_X = 'x'
PLAYER_O = 'o'

def print_rules():
    print('''
===========================
Welcome to Tic Tac Toe
GAME RULES:
Each player can place one mark (or stone) per turn on the 3x3 grid
The WINNER is who succeeds in placing three of their marks in a
* horizontal,
* vertical or
* diagonal row

Let's start the game
    ''')

def print_board(board):
    print( 6 * '-')
    for i in board:
        print('{:1}|{:1}|{:1}'.format(*i))
        print( 6 * '-')

def player_move(board, player):
    print(39 * '=')
    while True:
        try:
            move = int(input('Player ' + player + ' | Please enter your move number: '))
            print(39 * '=')
            row, column = divmod(move-1, 3)
            if board[row][column] == '':
                board[row][column] = player
                return row, column
            else:
                print('{} is already taken'.format(move))
        except ValueError:
            print('Enter only numbers.')
        except IndexError:
            print('Enter number from 1 to 9')

def check_row(BOARD, row, player):
    for i in BOARD[row]:
        if i != player:
            return False
    return True

def check_coulumn(BOARD, column, player):
    for i in range(len(BOARD)):
        if BOARD[i][column] != player:
            return False
    return True

def check_diag1(BOARD,player):
    for i in range(0, 9, 4):
        x, y = divmod(i, len(BOARD))
        if BOARD[x][y] != player:
            return False
    return True

def check_diag2(BOARD,player):
    for j in range(2, 7, 2):
        x, y = divmod(j, len(BOARD))
        if BOARD[x][y] != player:
            return False
    return True

def check_draw(BOARD):
    for i in BOARD:
        if '' in i:
            return False
    print('DRAW, no one win.')
    exit()

def check_win(BOARD, row, column, player):
    if check_row(BOARD, row, player) or check_coulumn(BOARD, column, player) or check_diag1(BOARD, player) or check_diag2(BOARD, player):
        print('Congratulations, the player ' + player + ' WON!')
        exit()

def main():

    print_rules()
    while True:
        print_board(BOARD)
        row, column = player_move(BOARD, PLAYER_X)
        check_win(BOARD, row, column, PLAYER_X)
        check_draw(BOARD)
        print_board(BOARD)
        row, column = player_move(BOARD, PLAYER_O)
        check_win(BOARD, row, column, PLAYER_O)

main()
