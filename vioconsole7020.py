# coding: utf-8

# VioConsole
# Copyright © 2023 Alexey Polyakov. All rights reserved. Contacts: wicotaburet@oxut.fun

import os, sys
os.system('title VioConsole 7020')
try:
	from colorama import init, Fore
	from cmds.create_error import create_error
	from cmds.echo import echo_cog
	from cmds.exit import exit_cog
	from cmds.help import help
	from cmds.info import info
	from cmds.mkdir import mkdir_cog
	from cmds.redir import read_dir
	from cmds.rmdir import rmdir_cog
	from cmds.clone import clone
	from cmds.kill import kill_cog
	from cmds.themes import custom_color
except:
	try:
		from recovery import main_notfoundcmds
		main_notfoundcmds()
	except:
		print("VioConsole | Не удалось запустить Recovery! Переустановите VioConsole.")
		while True:
			input()

init()

def main():
	entercmd = input("Введите команду: ")
	if entercmd == "help":
		help()
	elif entercmd == "info":
		info()
	elif entercmd == "exit":
		exit_cog()
	elif entercmd == "echo":
		echo_cog()
	elif entercmd == "mkdir":
		mkdir_cog()
	elif entercmd == "rmdir":
		rmdir_cog()
	elif entercmd == "redir":
		read_dir()
	elif entercmd == "create_error":
		create_error()
	elif entercmd == "clone":
		clone()
	elif entercmd == "kill":
		kill_cog()
	elif entercmd == "colors":
		custom_color()
print("VioConsole [версия 7020]")
print("Copyright © 2023 Alexey Polyakov. All rights reserved.")
print("Вы впервые запустили VioConsole и не знаете команд? Напишите help для чтобы узнать все команды и что они делают!")
print()
while True:
	main()
