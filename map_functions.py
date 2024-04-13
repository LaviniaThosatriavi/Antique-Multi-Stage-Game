import animate_functions

def load_map(choice):
    with open (f"{choice}.map", 'r') as mapFile:
        temp = mapFile.read().splitlines()
    map_board = []
    for line in temp:
        temp = [char for char in line]
        map_board.append(temp)

    return map_board

def display_map(map_board):
    for row in map_board: 
        for element in row:
            if element == 'P':
                print('\033[34mP\033[0m', end = '')
            elif element == '~':
                print('\033[32m~\033[0m', end = '')
            elif element == '&':
                print('\033[31m&\033[0m', end = '')
            elif element == 'O':
                print('\033[0;33mO\033[0m', end = '')
            else:
                print(element, end = '')
        print()

def find_player(map_board):
    for row in range(len(map_board)):
        for col in range(len(map_board[row])):
            if map_board[row][col] == 'P':
                return row, col

def valid_move(map_board, move):
    global player_pos, new_player_pos

    if move not in 'wasd': return False

    moves = [('w', -1, 0), ('a', 0, -1), ('s', 1, 0), ('d', 0, 1)]
    for direction in moves:
        if direction[0] == move:
            dx, dy = direction[1], direction[2]
    
    player_pos = find_player(map_board)
    new_player_pos = (player_pos[0] + dx, player_pos[1] + dy)
    if map_board[new_player_pos[0]][new_player_pos[1]] == '~':
        return True
    elif map_board[new_player_pos[0]][new_player_pos[1]] == 'O':
        animate_functions.animate_customer()
        print("YAY! You met your customer!")
        print("Solve the puzzle to successfully sell your dumpling!")
        return True
    elif map_board[new_player_pos[0]][new_player_pos[1]] == '&':
        animate_functions.animate_obstacle()
        print("OOPS! You crashed into an obstacle!")
        display_map(map_board)
        return False
    elif map_board[new_player_pos[0]][new_player_pos[1]] == 'X':
        animate_functions.animate_wall()
        print("OOPS! Your crashed into the wall!")
        display_map(map_board)
        return False

def update_map(map_board):
    global player_pos, new_player_pos
    if map_board[new_player_pos[0]][new_player_pos[1]] == 'O':
        customer = True
    else: 
        customer = False

    map_board[player_pos[0]][player_pos[1]] = '~'
    map_board[new_player_pos[0]][new_player_pos[1]] = 'P'  
    return map_board, customer
