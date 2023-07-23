# coding utf-8

# VioConsole
# Copyright © 2023 Alexey Polyakov. All rights reserved. Contacts: wicotaburet@oxut.fun

try:
	import os, sys
except:
	print('Ошибка | Не удалось импортировать библиотеки!')

def mkdir_cog():
	entername = input("Введите название папки: ")
	if not entername:
		try:
			os.mkdir(".\\New folder")
		except:
			print("Не удалось создать папку! Проверьте, не заполнен ли диск и не защищён ли он от записи...")
		else:
			print("Успешно создана новая папка: New folder")
	else:
		try:
			os.mkdir(f"{entername}")
		except:
			print("Не удалось создать папку! Проверьте, не заполнен ли диск и не защищён ли он от записи...")
		else:
			print(f"Успешно создана новая папка: {entername}")
