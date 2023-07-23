# coding: utf-8

# VioConsole
# Copyright © 2023 Alexey Polyakov. All rights reserved. Contacts: wicotaburet@oxut.fun

try:
	import os, sys
except:
	print('Ошибка | Не удалось импортировать библиотеки!')

def help():
	print("""
Помощь по VioConsole:
help - Вызвать это меню справки
info - Узнать информацию о данной версии VioConsole
mkdir - Создать новую папку
rmdir - Удалить уже существующую папку
redir - Прочитать уже существующую папку
echo - Вывести нужный текст на экран
create_error - Создать ошибку
	""")
