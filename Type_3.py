# Создайте программу для игры в ""Крестики-нолики"".

# Пример интерфейса:

#    |   | 0
# -----------
#    |   |
# -----------
#    | X |
# Ввод можно реализовать через введение двух чисел (номеров строки и столбца).

import random


def draw_board(board):
    print('X   0   1   2')
    print("Y -------------")
    for i in range(3):
        print(f"{i} |", board[i][0], "|", board[i][1], "|", board[i][2], "|")
        print("  -------------")


def get_player(player_0: str, player_1: str) -> str:
    '''
    Определение первого хода
    '''
    print('Сейчас мы разыграем право первого хода...')
    temp = random.randint(0, 1)
    if temp == 0:
        gamer = player_0
    else:
        gamer = player_1
    print(f'И первым у нас ходит {gamer}!')
    return gamer


def get_number_game(input_string: str) -> int:
    '''
    Проверка правильности индекса
    '''
    while True:
        try:
            num = int(input(input_string))
            if 0 <= num < 3:
                return num
            else:
                print('Неправильно. Давай еще раз.')
        except ValueError:
            print('Это не то ...')


def get_mark(input_string: str) -> int:
    '''
    Проверка правильности знака
    '''
    while True:
        try:
            mark = input(input_string)
            if mark in 'xoXO':
                mark_0 = mark.upper()
                if mark_0 == 'X':
                    mark_1 = 'O'
                else:
                    mark_1 = 'X'
                return mark_0, mark_1
            else:
                print('Неправильно. Давай еще раз.')
        except ValueError:
            print('Это не то ...')


def get_viner(game_board: list) -> bool:
    for i in range(3):
        if (game_board[i][0] == game_board[i][1] and game_board[i][0] == game_board[i][2]) and game_board[i][0] != ' ':
            return True
    for i in range(3):
        if (game_board[0][i] == game_board[1][i] and game_board[0][i] == game_board[2][i]) and game_board[0][i] != ' ':
            return True
    if (game_board[0][0] == game_board[1][1] and game_board[0][0] == game_board[2][2]) and game_board[1][1] != ' ':
        flag = True
    if (game_board[0][2] == game_board[1][1] and game_board[0][2] == game_board[2][0]) and game_board[1][1] != ' ':
        return True
    return False


def get_draw(game_board: list) -> bool:
    for i in range(3):
        for j in range(3):
            if game_board[i][j] == ' ':
                return False
    return True


def play_game(gamer: str, name_player_1: str, name_player_2: str, sign_0: str, sign_1: str, board: list) -> str:
    while True:
        if gamer == name_player_1:
            ind_2 = get_number_game('Введите координату "Х" клетки:\n')
            ind_1 = get_number_game('Введите координату "Y" клетки:\n')
            if board[ind_1][ind_2] == ' ':
                board[ind_1][ind_2] = sign_0
                draw_board(board)
                if get_viner(board):
                    print('У нас есть победитель!')
                    return gamer
                gamer = name_player_2
        else:
            ind_2 = random.randint(0, 2)
            ind_1 = random.randint(0, 2)
            if board[ind_1][ind_2] == ' ':
                board[ind_1][ind_2] = sign_1
                draw_board(board)
                if get_viner(board):
                    print('У нас есть победитель!')
                    return gamer
                gamer = name_player_1
        if get_draw(board):
            return 'У нас ничья.'


playing_field = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
print('Это игра "Крестики-нолики"\n Для того чтобы сделать ход вы вводите координаты клетки: X и Y')
name_0 = 'Игрок'
mark_0, mark_1 = get_mark('Выберите крестик - х или нолик - о:\n')
name_1 = 'Бот'
gamer_int = get_player(name_0, name_1)
draw_board(playing_field)
result = play_game(gamer_int, name_0, name_1, mark_0, mark_1, playing_field)
print(result)
