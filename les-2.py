import os
import psutil
import sys
import shutil

name = input ("Введите Ваше имя: ")
print ("Привет, " + name + ". Я твой интерактивный помощник.")

work = ''
while work != 'выход':
    work = input ("Хочешь поработать? (да/нет/выход)")
    if work == 'да':
        print ("Отлично!")
        print ("Что будем делать?:")
        print("[1] - Вывести список файлов в текущей директории")
        print("[2] - Вывести информацию о системе")
        print("[3] - Вывести список активных процессов")
        print("[4] - Создать копии файлов из текущей директории")
        do = int(input ("Укажите номер действия: "))
        if do == 1:
            print ("# Список файлов в текущей директории #")
            print (os.listdir())
        elif do == 2:
            print ("# Информация о системе #")
            print("Текущая директория - " + os.getcwd())
            print("Название платформы - " + sys.platform)
            print("Кодировка - " + sys.getfilesystemencoding())
            print("Логин текущего пользователя - " + os.getlogin())
            print("Количество ядер CPU - " + str(psutil.cpu_count()))
        elif do == 3:
            print ("# Список активных процессов #")
            print (psutil.pids())
        elif do == 4:
            file_list = os.listdir()
            i = 0
            while i < len(file_list):
                newfile = file_list[i] + '.dd'
                shutil.copy(file_list[i], newfile)
                i = i+1
        else:
            pass
    elif work == "нет":
        print ("Жаль, ну если передумаешь заходи. Пока " + name)
    else:
        pass