# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота. Достаточно сделать так,
# чтобы бот не брал конфет больше положенного или больше чем имеется в куче.
# b) Подумайте как наделить бота ""интеллектом"".
# Напоминаю, если перед пользователем будет лежать 29 конфет, то он, однозначно, проиграет.
# Достаточно довести игру до такой ситуации.
import random


def get_player(player_0: str, player_1: str) -> str:
    '''
    определение первого хода
    '''
    print('Сейчас мы разыграем право первого хода...')
    temp = random.randint(0, 1)
    if temp == 0:
        gamer = player_0
    else:
        gamer = player_1
    print(f'И первым у нас берет конфеты {gamer}!')
    return gamer


def get_number(input_string: str) -> int:
    '''
    Получение количества конфет
    '''
    num_test = 0
    while num_test == 0:
        num = int(input(input_string))
        if 0 < num < 29:
            num_test = num
            return num
        else:
            print('Неправильно. Давай еще раз.')


def last_move(input_string: str, number: int) -> int:
    '''
    Получение количества конфет
    для последнего хода
    '''
    num_test = 0
    while num_test == 0:
        num = int(input(input_string))
        if 0 < num <= number:
            return num
        else:
            print('Неправильно. Давай еще раз.')


def playng(candy: int, player: str, player_1: str, player_2: str) -> str:
    winner = ''
    while candy > 0:
        # '''
        # подсказка для первого игрока
        # '''
        # if player == player_1:
        #     if candy > 57:
        #         print('берите 28 конфет')
        #     elif candy < 29:
        #         print(f'берите {candy} конфет')
        #     else:
        #         print(f'берите {candy - 29} конфет')

        '''
        игровой процесс
        '''
        if candy > 28:
            if player == player_1:
                print(f'У нас {candy} конфет.')
                move = get_number(
                    f'{player} сколько вы берете кофет? Вы можете взять от 1 до 28: ')
                candy -= move
                player = player_2
                winner = player_1
            else:
                print(f'У нас {candy} конфет.')
                if candy > 57:
                    if ((candy-29) % 28) == 0:
                        move = 1   
                    else:
                        move = (candy-29) % 28
                else:

                    move = candy - 29
                print(f'=> Я беру {move} конфет')
                candy -= move
                player = player_1
                winner = player_2
        else:
            if player == player_1:
                print(f'У нас {candy} конфет.')
                move = last_move(
                    f'{player} сколько вы берете кофет? Вы можете взять от 1 до {candy}: ', candy)
                candy -= move
                player = player_2
                winner = player_1
            else:
                print(f'У нас {candy} конфет.')
                move = candy
                print(f'=> Я беру {move} конфет')
                candy -= move
                player = player_1
                winner = player_2
    return winner


name_0 = 'Игрок_1'
name_1 = 'Бот'
gamer = get_player(name_0, name_1)
sweet = 100
winner = playng(sweet, gamer, name_0, name_1)

print(f'победил - > {winner} !!!')
