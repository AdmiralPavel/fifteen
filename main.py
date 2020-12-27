import random

import keyboard

solved_field = [['1 ', '2 ', '3 ', '4 '], ['5 ', '6 ', '7 ', '8 '], ['9 ', '10', '11', '12'], ['13', '14', '15', '0 ']]

field = [['1 ', '2 ', '3 ', '4 '], ['5 ', '6 ', '7 ', '8 '], ['9 ', '10', '11', '12'], ['13', '14', '15', '0 ']]


def print_field(field):
    print('\n' * 30)
    for row in field:
        print(' '.join(row))


def move(field, cmd, flag):
    cmd = cmd.upper()
    for line in field:
        if '0 ' in line:
            row = field.index(line)
            column = line.index('0 ')
    if not (cmd == 'W' or cmd == 'A' or cmd == 'S' or cmd == 'D'):
        print('Некорректный ввод! Попробуйте ещё раз.')
    elif cmd == 'W':
        if row != 3:
            field[row][column], field[row + 1][column] = field[row + 1][column], field[row][column]
    elif cmd == 'S':
        if row != 0:
            field[row][column], field[row - 1][column] = field[row - 1][column], field[row][column]
    elif cmd == 'A':
        if column != 3:
            field[row][column], field[row][column + 1] = field[row][column + 1], field[row][column]
    elif cmd == 'D':
        if column != 0:
            field[row][column], field[row][column - 1] = field[row][column - 1], field[row][column]
    if flag:
        print_field(field)


def shuffle(field):
    for i in range(50):
        direct = random.choice(['W', 'A', 'S', 'D'])
        move(field, direct, False)


shuffle(field)
print_field(field)
keyboard.add_hotkey('up', lambda: move(field, 'W', True))
keyboard.add_hotkey('down', lambda: move(field, 'S', True))
keyboard.add_hotkey('left', lambda: move(field, 'A', True))
keyboard.add_hotkey('right', lambda: move(field, 'D', True))

keyboard.wait()
