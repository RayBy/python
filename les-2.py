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
        print("[4] - Провести операции с файлами")
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
            print("# Провести операции с файлами #")
            print("[1] - Вывести список файлов текущей директории")
            print("[2] - Создать копию выбранного файла")
            print("[3] - Удалить копии файлов в директории указанной пользователем")
            file = int(input("Укажите номер действия: "))
            if file == 1:
                print("# Список файлов в текущей директории #")
                print(os.listdir())
            elif file == 2:
                file_name = input ("Введите имя файла: ")
                if os.path.isfile(file_name):
                    copy_file = file_name + '.copy'
                    shutil.copy(file_name, copy_file)
            elif file == 3:
                dir_name = input("Укажите имя директории: ")
                file_list = os.listdir(dir_name)
                i=0
                while i < len(file_list):
                    copy_file_name = os.path.join(dir_name, file_list[i])
                    if copy_file_name.endswith('.copy'):
                        os.remove(copy_file_name)
                    i = i+1
                else:
                    print("Недопустимое действие")
        else:
            pass
    elif work == "нет":
        print("Жаль, ну если передумаешь заходи. Пока " + name)
    else:
        pass