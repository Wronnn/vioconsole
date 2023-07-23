# coding: utf-8

# VioConsole
# Copyright © 2023 Alexey Polyakov. All rights reserved. Contacts: wicotaburet@oxut.fun

try:
	import os, sys
except:
	print('Ошибка | Не удалось импортировать библиотеки!')

def read_dir():
    try:
        name_folder = input('\nВведите название директории --> ')
        if not name_folder:
            print('\nВы не указали название директории!\n')
        else:
            logs = os.listdir(path=f".\\{name_folder}")
            print(f"\n{logs}\n")
    except:
        print('\nДиректории не существует!\n')
