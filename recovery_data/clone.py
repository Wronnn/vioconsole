# coding: utf-8

# VioConsole
# Copyright © 2023 Alexey Polyakov. All rights reserved. Contacts: wicotaburet@oxut.fun

try:
	import os, sys, random
except:
	print('Ошибка | Не удалось импортировать библиотеки!')

def clone():
	print("Внимание: Данная команда не клонирует последнюю версию VioConsole")
	name = input("Введите название вашей копии VioConsole: ")
	version = input("Введите версию вашей копии VioConsole: ")
	if not name:
		return print("Вы не указали имя!")
	if not version:
		return print("Вы не указали версию!")
	loginuser = os.getlogin()
	techsupport = input("Введите ссылку тех. поддержки: ")
	if not techsupport:
		techsupport = "Тех. поддержка недоступна"
	clone_sources = f'''
# coding: utf-8

# {name}
# Создано с любовью Alexey Polyak

try:
	import os, sys
except:
	print('{name} | Не удалось импортировать библиотеки!')
	input('Нажмите Enter, чтобы выйти')

os.system(f'title {name}')

def echo():
	entertext = input("Введите текст на экран который нужно вывести: ")
	if not entertext:
		print("Вы не ввели текст!")
	else:
		print(entertext)

def rmdir():
	enterfolder = input("Введите название папки, которую нужно удалить: ")
	if not enterfolder:
		print("Вы не ввели название папки!")
	else:
		try:
			os.rmdir(enterfolder)
		except:
			print(f"Не удалось удалить папку! Проверьте, не заполнен ли диск и не защищён ли он от записи, также не заполнена ли папка...")
		else:
			print(f"Успешно удалена папка")

def exit_program():
	sys.exit(0)

def info():
	print(f"{name} (VioConsole Clone) [version {version}]")
	print("Создано с любовью Alexey Polyak")
	print("Данная версия VioConsole была создана при помощи команды clone")
	print("Данная версия VioConsole не является оригиналом!")

def help():
	print(f"""
Помощь по {name}:
help - Вызвать это меню справки
info - Узнать информацию о данной версии {name}
rmdir - Удалить уже существующую папку
echo - Вывести нужный текст на экран
exit - Выход из {name}
	""")

def main():
	entercmd = input("Введите команду: ")
	if entercmd == "help":
		help()
	elif entercmd == "info":
		info()
	elif entercmd == "exit":
		exit_program()
	elif entercmd == "echo":
		echo()
	elif entercmd == "mkdir":
		print(f"[{name}] Данная версия {name} не поддерживает эту функцию.")
	elif entercmd == "rmdir":
		rmdir()
	elif entercmd == "redir":
		print(f"[{name}] Данная версия {name} не поддерживает эту функцию.")
	elif entercmd == "create_error":
		print(f"[{name}] Данная версия {name} не поддерживает эту функцию.")
	elif entercmd == "/cloneuser":
		print(f"[{name}] Данная версия {name} {version} была склонирована из под учётной записи {loginuser}")
print(f"{name} [version {version}]")
print("Создано с любовью Alexey Polyak")
print()
while True:
	main()
'''
	print(f"ВНИМАНИЕ! Если в папке с VioConsole есть точно такой же файл '{name}.py' то он будет заменён без возможности восстановления!")
	input("Нажмите Enter, чтобы продолжить")
	with open(f".\\{name}.py", "w+", encoding="utf-8") as project:
		project.write(clone_sources)
		project.close()
		print("Клонирование VioConsole завершено! Файл сохранён в папке с VioConsole")
