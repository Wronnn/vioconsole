# coding: utf-8

# VioConsole
# Copyright © 2023 Alexey Polyakov. All rights reserved. Contacts: wicotaburet@oxut.fun

try:
    import os, sys
    from colorama import init, Fore
except:
    print('Ошибка | Не удалось импортировать библиотеки!')

init()

def custom_color():
    print('\nКастомные цвета вывода текста\n1 - Зелёный\n2 - Красный\n3 - Жёлтый\n4 - Синий\n5 - Сбросить кастомный цвет')
    color_input = input('\nНапишите нужную цифру --> ')
    if color_input == '1': print(Fore.GREEN + '\nУспешно установлен цвет "Зелёный"\n')
    elif color_input == '2': print(Fore.RED + '\nУспешно установлен цвет "Красный"\n')
    elif color_input == '3': print(Fore.YELLOW + '\nУспешно установлен цвет "Жёлтый"\n')
    elif color_input == '4': print(Fore.BLUE + '\nУспешно установлен цвет "Синий"\n')
    elif color_input == '5': print(Fore.RESET + '\nУспешно сброшены все установленые цвета\n')
    else: print('\nВы не указали цифру либо же указали её не правильно\n')
