import guess_word
import map_functions
import maze_functions
import animate_functions
import money
import time

# variable to store the maps which have been solved
solved = []

with open("Source Files/texts", 'r') as f:
    for line_number, line in enumerate(f):
        if line_number <= 10:
            print(line, end = '')
print("-----------------------> \033[1mGuidelines\033[0m <-----------------------\n\033[34m~   Enter 1-3 to venture into Antique's puzzle map games   ~\n~   3 for a challenging map..... 1 for a chill game.....   ~\033[0m")

# validating user choice for puzzle maps

choice = 'x'
while not(choice in "123" and choice.isdigit() and len(choice) == 1):
    choice = input("Choice: ")

# function to play maps 1-3
def map_game():
    global choice

    choice = int(choice)

    if choice == 1:
        customers = 1
    elif choice == 2: 
        customers = 3
    elif choice == 3: 
        customers = 5
    
    map_board = map_functions.load_map(choice)
    map_functions.display_map(map_board)
    
    while customers > 0:
        move = 'x'

        while move not in "wasdq" and len(move) == 1 or move == ' ' or len(move) != 1:
            move = input("Enter your move [wasdq]: ")

        if move == 'q': 
            maze_game()
            break

        while not map_functions.valid_move(map_board, move):
            move = input("Enter your move [wasdq]: ")
        
        map_board, customer = map_functions.update_map(map_board)
        
        if customer == True:
            money.change_money(money.get_money() + guess_word.guessWord(choice))
            customers -= 1

            animate_functions.animate_dumplings()
            print("DUMPLING SUCCESSFULLY SOLD!")
            time.sleep(0.4)
            animate_functions.animate_money()
            print("Collected money: ", money.get_money())
            time.sleep(1.5)
            map_functions.display_map(map_board)
        else:
            map_functions.display_map(map_board)
        
        if customers == 0:
            solved.append(choice)
            
            if len(solved) < 3:
                print("Congratulations, you solved this map!\n~ Enter 4 to directly enter the maze final round.....! ~\n~ Or, enter another map to collect more money........! ~")
                left = []
                for i in range(1, 4):
                    if i not in solved:
                        left.append(i)
    
                print("Your remaining map choices: ", left)
                
                choice = 'x'
                while not(choice in ''.join(map(str, left)) or choice == '4'):
                    choice = input("Choice: ")
                if choice == '4':
                    maze_game()
                else:
                    map_game()
            else:
                maze_game()

# function to play maze game
def maze_game():
    maze_functions.load_maze()
    maze_functions.run_maze()
                
map_game()
