BOARD = [['', '', ''],
        ['', '', ''],
        ['', '', '']]
PLAYER_X = 'X'
PLAYER_O = 'O'

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

# print the BOARD
def print_board(board):
    whole_board = []
    for i in board:
        line = '{:1}|{:1}|{:1}'.format(*i)
        whole_board.append(line)
    for i in range(1, len(board)+1, 2):
        whole_board.insert(i, '-'*len(line))
    whole_board  = '\n'.join(whole_board)
    print(whole_board)

# read and check players move
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

# check rows
def check_row(BOARD, row, player):
    for i in BOARD[row]:
        if i != player:
            return False
    return True

# check columns
def check_coulumn(BOARD, column, player):
    for i in range(len(BOARD)):
        if BOARD[i][column] != player:
            return False
    return True

# transform nested list to one list
def flatten(board):
    lst = []
    for i in board:
        lst += i
    return lst

# check diagonals
def check_diag(BOARD, player):
    flat_board = flatten(BOARD)
    size = len(BOARD)
    #check diag from left to down
    if set(flat_board[0:size**2:size+1]) == set(player):
        return True
    #check diag from right to down
    if set(flat_board[size-1:size**2-1:size-1]) == set(player):
        return True

# check if the game is tie and print it
def check_draw(BOARD):
    for i in BOARD:
        if '' in i:
            return False
    print('DRAW, no one win.')
    exit()

# check if move was a win move and print it out
def check_win(BOARD, row, column, player):
    if check_row(BOARD, row, player) or check_coulumn(BOARD, column, player) or check_diag(BOARD, player):# or check_diag2(BOARD, player):
        print_board(BOARD)
        print(39 * '=')
        print('Congratulations, the player ' + player + ' WON!')
        exit()

# change player
def chenge_player(player):
    return PLAYER_O if player == PLAYER_X else PLAYER_X

#main
def main():

    print_rules()
    PLAYER = PLAYER_X
    while True:
        print_board(BOARD)
        row, column = player_move(BOARD, PLAYER)
        check_win(BOARD, row, column, PLAYER)
        check_draw(BOARD)
        PLAYER = chenge_player(PLAYER)

main()
