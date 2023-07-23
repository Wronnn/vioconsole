# coding: utf-8

# VioConsole
# Copyright © 2023 Alexey Polyakov. All rights reserved. Contacts: wicotaburet@oxut.fun

try:
	import os, sys
except:
	print('Ошибка | Не удалось импортировать библиотеки!')

infotext = """
VioConsole - многофункциональная консоль на ЯП Python.
Оффициальный дискорд сервер VioConsole: Soon...
Разработчики:
Alexey Polyak (aka. Wico) кодер, основатель VioConsole
А также спасибо человеку под именем SideKick (aka. Xiodazer) за большинство идей для VioConsole.
"""

def info():
    print(infotext)
