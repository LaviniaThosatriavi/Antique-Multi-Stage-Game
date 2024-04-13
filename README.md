# Antique-Multi-Stage-Game

The game consists of multiple maps where the player collects money and completes various objectives. Here's an overview of the gameplay:

## Maps 1-3

Maps 1 to 3 have increasing difficulty and size. The player's objective is to reach the customers (indicated by 'O') and solve a guess-the-word puzzle to sell dumplings. The maps are represented by different characters:

- 'X': walls
- 'O': customer
- 'P': player
- '&': obstacle
- '~': free spaces

Each map has a word list category, as follows:

- Map 1: HK Foods
- Map 2: HK Tourism Spots
- Map 3: HK MTR Stations

The player has three attempts to guess the word. If they guess correctly within three attempts, they receive $20; otherwise, they receive $10. If they cannot guess the word, they still receive $5.

During maps 1 to 3, the player can enter moves [wasdq] to navigate the map:

- w: up
- s: down
- a: left
- d: right
- q: quit (immediately enter maze in map 4)

The game provides animations to visualize the gameplay, such as a stickman hitting an obstacle/wall or selling dumplings to a customer.

## Map 4: Maze

After collecting money in maps 1 to 3, the player can enter a maze in the final round. The maze is partially displayed at a time, and the player cannot retrace their path. The maze contains doors represented by '+', which require $5 to unlock. When the player reaches a dead end, they can buy a new attempt for $15 and retrace their path. If the player runs out of money and cannot escape the maze, they lose. If they manage to exit the maze, they win and receive the antique vase.

Note: The game validates all inputs, uses colored outputs, and ASCII art drawings for visual elements.
