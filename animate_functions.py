import time

# py file to animate the animations

def animate_obstacle():
    with open ("Source Files/animations", 'r') as sourceFile:
        for line_number, line in enumerate(sourceFile, start = 1):
            if line_number <= 11:
                for element in line:
                    if element == '_':
                        print("\033[32m_\033[0m", end = '')
                    elif element == '<':
                        print("\033[31m<\033[0m", end = '')
                    elif element == '!':
                        print("\033[31m!\033[0m", end = '')
                    else:
                        print(f"\033[34m{element}\033[0m", end = '')
            else:
                break
            time.sleep(0.4)

def animate_wall():
    with open ("Source Files/animations", 'r') as sourceFile:
        for line_number, line in enumerate(sourceFile, start = 1):
            if line_number < 13:
                continue
            if 13 <= line_number <= 23:
                for element in line:
                    if element == '_':
                        print("\033[32m_\033[0m", end = '')
                    elif element == '[':
                        print("\033[31m[\033[0m", end = '')
                    elif element == ']':
                        print("\033[31m]\033[0m", end = '')
                    else:
                        print(f"\033[34m{element}\033[0m", end = '')
                time.sleep(0.4)

            elif line_number > 23:
                break

def animate_customer():
    with open ("Source Files/animations", 'r') as sourceFile:
        for line_number, line in enumerate(sourceFile, start = 1):
            if line_number < 25:
                continue
            elif 25 <= line_number <= 27:
                for element in line:
                    if element == '_':
                        print("\033[32m_\033[0m", end = '')
                    elif element == 'X':
                        print("\U0001F95F", end = '')
                    else:
                        print(f"\033[34m{element}\033[0m", end = '')
            elif line_number > 27:
                break

def animate_dumplings():
    with open ("Source Files/animations", 'r') as sourceFile:
        for line_number, line in enumerate(sourceFile, start = 1):
            if line_number < 29:
                continue
            if 29 <= line_number <= 35:
                for element in line:
                    if element == '_':
                        print("\033[32m_\033[0m", end = '')
                    elif element == 'X':
                        print("\U0001F95F", end = '')
                    else:
                        print(f"\033[34m{element}\033[0m", end = '')
                time.sleep(0.4)

            elif line_number > 35:
                break

def animate_money():
    with open("Source Files/animations", 'r') as sourceFile:
        for line_number, line in enumerate(sourceFile, start = 1):
            if line_number < 37:
                continue
            if 37 <= line_number <= 58:
                for element in line:
                    if element == '_':
                        print(element, end = '')
                    else:
                        print(f"\033[32m{element}\033[0m", end = '')
            elif line_number > 58:
                break

def animate_vase():
    with open("Source Files/animations", 'r') as sourceFile:
        for line_number, line in enumerate(sourceFile, start = 1):
            if line_number < 58:
                continue
            else:
                for element in line:
                    if element == '_':
                        print(element, end = '')
                    else:
                        print(f"\033[38;2;205;149;12m{element}\033[0m", end = '')
                time.sleep(0.2)
