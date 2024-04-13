# Antique Multi-Stage Game

This is a text-based maze game where players navigate through maps, solve word puzzles, and collect money to escape the maze and retrieve an antique vase. The game features different maps, increasing difficulty levels, and interactive gameplay elements.

## Installation

To run the game, make sure you have Python installed on your system. The game is compatible with Python 3.

1. Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/LaviniaThosatriavi/Antique-Multi-Stage-Game.git
```

2. Navigate to the game's directory:

```bash
cd Antique-Multi-Stage-Game
```

## Gameplay Instructions

To start the game, follow these steps:

1. Open a terminal or command prompt.

2. Navigate to the game's directory.

3. Run the game using the following command:

```bash
python main.py
```

The game will start, and you will be presented with the first map.

## Map Gameplay

The game consists of multiple maps, each with its own objectives and challenges. Here's a breakdown of the gameplay mechanics:

### Maps 1-3

Maps 1 to 3 are the initial stages of the game. Each map presents a maze-like environment where the player's goal is to reach the customers and solve word puzzles to complete the sale. The maps become progressively more challenging, with larger sizes and more customers to interact with.

- The player is represented by the character 'P'.
- Customers are represented by the character 'O'.
- Walls are represented by the character 'X'.
- Obstacles are represented by the character '&'.
- Free spaces are represented by the character '~'.

During maps 1 to 3, you can move the player character using the following controls:

- 'w': Move up
- 's': Move down
- 'a': Move left
- 'd': Move right
- 'q': Quit and immediately enter the maze in map 4

To successfully sell the dumplings, you must solve a guess-the-word puzzle within three attempts. If you guess correctly within three attempts, you will receive $20. Otherwise, you will receive $10. If you cannot guess the word, you will still receive $5.

### Map 4: The Maze

fter collecting money in maps 1 to 3, the player can enter a maze in the final round. The maze is partially displayed at a time, and the player cannot retrace their path. The maze contains doors represented by '+', which require $5 to unlock. When the player reaches a dead end, they can buy a new attempt for $15 and retrace their path. If the player runs out of money and cannot escape the maze, they lose. If they manage to exit the maze, they win and receive the antique vase.

Note: The game validates all inputs, uses colored outputs, and ASCII art drawings for visual elements.
