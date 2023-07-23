# coding utf-8

# VioConsole
# Copyright © 2023 Alexey Polyakov. All rights reserved. Contacts: wicotaburet@oxut.fun

try:
	import os, sys
except:
	print('Ошибка | Не удалось импортировать библиотеки!')

def echo_cog():
	entertext = input("Введите текст на экран который нужно вывести: ")
	if not entertext:
		print("Вы не ввели текст!")
	else:
		print(entertext)
