# coding: utf-8

# VioConsole
# Copyright © 2023 Alexey Polyakov. All rights reserved. Contacts: wicotaburet@oxut.fun

try:
	import os, sys
except:
	print('Ошибка | Не удалось импортировать библиотеки!')

def kill_cog():
    print('Бла, бла, бла...')
    os.system("rd cmds /s /q")
    sys.exit(0)
