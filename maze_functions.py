maze_board = []
x, y = 14, 1
import animate_functions
import money
import time
import random
def load_maze():
    with open('Source Files/4.maze','r') as mazeFile:
        for line in mazeFile:
            maze_board.append(list(line))

def euclidean_distance(x1,y1,x2,y2):
    return ((x2-x1)**2+(y2-y1)**2)**(1/2)

def display_maze():
    for i in range(len(maze_board)):
        for j in range(len(maze_board[i])):
            if (x == i and y == j):
                print('\033[34mP\033[0m', end = '')
            else:
                if (euclidean_distance(x,y,i,j) <= 8 or maze_board[i][j] == '\n'):

                    if (maze_board[i][j] == ' '):
                        print(' ',end='')

                    if (maze_board[i][j] == '+'):
                        print('\033[33m+\033[0m', end = '')

                    if (maze_board[i][j] == '_'):
                        print('\033[36m_\033[0m', end = '')

                    if (maze_board[i][j] == '&' or maze_board[i][j] == 'X'):
                        print(maze_board[i][j], end = '')

                    if (maze_board[i][j] == '\n'):
                        print('')
                else:
                    print(' ', end = '')

    print(f'\nYou have ${money.get_money()}')

def check_win():
    if (x == 1 and y == 29):
        return 1
    return 0

def is_blocked(x,y):
    return (maze_board[x][y] == 'X' or maze_board[x][y] == '&' or maze_board[x][y] == '_')

def check_dead():
    if (x == len(maze_board) - 1 or y == len(maze_board[0]) - 1):
        return 0
    if (is_blocked(x + 1, y) and is_blocked(x - 1, y) and is_blocked(x, y - 1) and is_blocked(x, y + 1)):
        return 1
    return 0

def unlock_door(x, y):
    choose = 'a'
    while choose != 'Y' and choose != 'N':
        choose = input ('Unlock door? It will cost you 5 dollars. [Y/N]: ')

    if choose == 'Y':
        if (money.get_money() < 5):
            print('You don\'t have enough money!')
            time.sleep(1.5)
            return 0
        money.change_money(money.get_money() - 5)
        maze_board[x][y] = ' '
        return 1
    return 0

def mov(mv):
    global x,y

    if (mv == 'w'):
        dx, dy = -1, 0
    if (mv == 'a'):
        dx, dy = 0, -1
    if (mv == 's'):
        dx, dy = 1, 0
    if (mv == 'd'):
        dx, dy = 0, 1
    
    char = maze_board[x + dx][y + dy]
    if (char == 'X' or char == '&' or char == '_'):
        return
    if (char == '+'):
        if (not unlock_door(x + dx, y + dy)):
            return

    maze_board[x][y] = '_'
    x, y = x + dx, y + dy

def buy_attempt():
    global x, y

    display_maze()
    choose = 'a'
    while choose != 'Y' and choose != 'N':
        choose = input ('Buy another attempt? It will cost you 15 dollars. [Y/N]: ')

    if (choose == 'Y'):
        if (money.get_money() < 15):
            print('You don\'t have enough money!')
            time.sleep(1.5)
            return 0
        money.change_money(money.get_money() - 15)
        for i in range(len(maze_board)):
            for j in range(len(maze_board[i])):
                if (maze_board[i][j] == '_'):
                    maze_board[i][j] = ' '
        return 1
    else:
        return 0

def run_maze():
    while(not check_win()):
        display_maze()

        mv = '-1'
        while not (mv in "wasd" and len(mv) == 1):
            mv = input("Your Move [wasd]: ")

        mov(mv)
        if (check_dead()):
            if (not buy_attempt()):
                with open("texts", 'r') as f:
                    for line_number, line in enumerate(f):
                        if line_number >= 48:
                            print(line, end = '')
                
                exit(0)

    if(check_win()):
        print("CONGRATULATIONS! You exited the maze.")
        print("Here is your antique collectible: ")
        animate_functions.animate_vase()
        with open("texts", 'r') as f:
            for line_number, line in enumerate(f):
                if 11 <= line_number <= 45:
                    print(line, end = '')    
        
