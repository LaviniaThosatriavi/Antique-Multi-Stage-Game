import random
# guess word file for maps 1-3 puzzles

wordList = {1 : ["dim sum", "siu mai", "milk tea", "wonton", "pineapple bun"], 2 : ["disney land", "ocean park", "nan lian garden", "happy valley", "ngong ping", "big buddha", "repulse bay" ], 3 : ["wong tai sin", "kennedy town", "sheung wan", "sai ying pun", "tsuen wan", "admiralty", "mong kok", "diamond hill"]}

def display_hangman(attempts):
    hangman_condition = [
        '''
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |     / \\
            -
        ''',
        '''
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |     / 
            -
        ''',
        '''
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |      
            -
        ''',
        '''
            --------
            |      |
            |      O
            |     \\|
            |      |
            |     
            -
        ''',
        '''
            --------
            |      |
            |      O
            |      |
            |      |
            |     
            -
        ''',
        '''
            --------
            |      |
            |      O
            |    
            |      
            |     
            -
        ''',
        '''
            --------
            |      |
            |      
            |    
            |      
            |     
            -
        '''
    ]
    print(hangman_condition[6 - attempts])

def guessWord(choice):
    word_list = wordList[choice]
    the_word = random.choice(word_list)
    word_list.remove(the_word)

    guessed = []
    attempts = 6
    money = 0

    print("~~~~~ WELCOME TO HANGMAN GUESS THE WORD PUZZLE ~~~~~")
    display_hangman(attempts)
    for char in the_word:
        if char == ' ':
            print(' ',end = '')
        else:
            print('_', end = '')

    if choice == 1: print("\nWord category: HK Foods")
    elif choice == 2: print("\nWord category: HK Tourism Spots")
    elif choice == 3: print("\nWord category: HK MTR Stations")

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1:
            print("\033[38;2;255;165;0mInvalid input! Enter a single letter.\033[0m")
            continue

        if guess in guessed:
            print("\033[38;2;255;165;0mInvalid input! You guessed that letter.\033[0m")
            continue

        guessed.append(guess)

        if guess not in the_word:
            attempts -= 1
            display_hangman(attempts)
            print(f"\033[91mWrong guess! You have {attempts} attempts remaining.\033[0m")
            if attempts == 1:
                hint = random.choice(the_word)
                while hint in guessed or hint == ' ':
                    hint = random.choice(the_word)
                print(hint)
                print(f"\033[32mHint: The word contains the letter {hint} \033[0m")
        else:
            print("\033[32mCorrect guess!\033[0m")

        guess_progress = ""
        for letter in the_word:
            if letter in guessed:
                guess_progress += letter + " "
            elif letter == ' ':
                guess_progress += ' '
            else:
                guess_progress += "_"

        print(guess_progress)

        if "_" not in guess_progress:
            if attempts >= 3:
                money += 20
            else:
                money += 10
        
            print("Congratulations! You guessed the word correctly.")
            print("You earned $", money)
            break

    if attempts == 0:
        money += 5
        display_hangman(attempts)
        print(f"\033[91mOUT OF TRIES! The word was: {the_word} \033[0m")
        print("You earned $", money)
    
    return money
