# coding: utf-8

# VioConsole
# Copyright © 2023 Alexey Polyakov. All rights reserved. Contacts: wicotaburet@oxut.fun

try:
	import os, sys
except:
	print('Ошибка | Не удалось импортировать библиотеки!')

def rmdir_cog():
	enterfolder = input("Введите название папки, которую нужно удалить: ")
	if not enterfolder:
		print("Вы не ввели название папки!")
	else:
		try:
			os.rmdir(f".\\{enterfolder}")
		except:
			print(f"Не удалось удалить папку! Проверьте, не заполнен ли диск и не защищён ли он от записи, также не заполнена ли папка...")
		else:
			print(f"Успешно удалена папка: {enterfolder}")
