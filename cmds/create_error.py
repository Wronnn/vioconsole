# coding: utf-8

# VioConsole
# Copyright © 2023 Alexey Polyakov. All rights reserved. Contacts: wicotaburet@oxut.fun

try:
	import os, sys
except:
	print('Ошибка | Не удалось импортировать библиотеки!')

def compile_error(text_error, title_error):
    try: os.mkdir('Temp', mode=0o777, dir_fd=None)
    except OSError: pass
    vbs_text = f"""
    x=msgbox("{text_error}", 4+16, "{title_error}")
    """
    bat_text = """
    @echo off
    Temp\\_create_error_.vbs
    """
    bat_two_text = """
    @echo off
    cd...
    del Temp /s /q
    """
    with open('Temp\\_start_vbs_.bat', 'w+', encoding='utf-8') as bat:
        bat.write(bat_text)
    with open('Temp\\_remove_error_.bat', 'w+', encoding='utf-8') as bat_two:
        bat_two.write(bat_two_text)
    with open('Temp\\_create_error_.vbs', 'w+', encoding='utf-16') as vbs:
        vbs.write(vbs_text)

def create_error():
    input_text = input('Введите текст ошибки --> ')
    input_title = input('Введите заголовок ошибки --> ')
    if not input_text:
        print('Вы не указали текст ошибки!')
        return
    if not input_title:
        print('Вы не указали заголовок ошибки!')
        return
    print('Создание ошибки. . .')
    compile_error(text_error=input_text, title_error=input_title)
    os.system('"Temp\\_start_vbs_.bat"')
    os.system('"Temp\\_remove_error_.bat"')
