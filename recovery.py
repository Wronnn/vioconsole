# coding: utf-8

# VioConsole
# Copyright © 2023 Alexey Polyakov. All rights reserved. Contacts: wicotaburet@oxut.fun

import sys, random, os

def main_notfoundcmds():
    print("Кажется, что-то сломалось...")
    print("VioConsole не смогла загрузится правильно, обычно перезапуск помогает в данной ситуации.\nЕсли же после перезапуска вы видите это окно то необходимо восстановить VioConsole")
    print("Выберите действие цифрой ниже\n1) Запустить восстановление\n2) Выбрать другие варианты восстановления")
    selection = input("Напишите нужную цифру и нажмите Enter: ")
    if selection == "1":
        try:
            os.mkdir(".\\cmds")
        except:
            print("Предупреждение | Не удалось создать папку! Восстановление может завершится не правильно.")
        os.system("copy %CD%\\recovery_data\\*.* .\\.\\cmds")
    elif selection == "2":
        while True:
            main()
            input("Готово! Нажмите Enter, чтобы продолжить.\nЧтобы изменения вступили в силу необходима перезагрузка")
    
    print("Устранение неполадок завершено!")
    print("Чтобы изменения вступили в силу необходима перезагрузка.")
    while True:
        
        input()

def main():
    os.system("cls")
    print("Добро пожаловать в VioConsole Recovery 1.1!\nДанное меню поможет вам устранить все неполадки с VioConsole.\n\nВыберите действие с помощью цифры\n1) Удалить папку cmds (Только для опытных пользователей)\n2) Восстановить папку cmds (В случае сбоев VioConsole)\n")
    selection2 = input("Выберите нужную цифру: ")
    if selection2 == "1":
        try:
            os.system("rd cmds /s /q")
            os.system("cls")
        except:
            print("Ошибка | Похоже произошла маленькая ошибка...")
    elif selection2 == "2":
        try:
            os.mkdir(".\\cmds")
        except:
            os.system("cls")
            print("Предупреждение | Не удалось создать папку! Восстановление может завершится не правильно.")
        os.system("copy %CD%\\recovery_data\\*.* .\\.\\cmds")
