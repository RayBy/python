import os
import psutil
import sys

name = input ("Введите имя: ")
print ("Привет, " + name)

work = input ("Хочешь поработать? (да/нет)")
if work == 'да':
    print ("Отлично!")
    print ("Я умею:")
    print("[1] - Вывести список файлов в текущей директории")
    print("[2] - Вывести информацию о системе")
    print("[3] - Вывести список активных процессов")
    do = int(input ("Укажите номер действия: "))
    if do == 1:
        print (os.listdir())
    elif do == 2:
        print("Текущая директория - " + os.getcwd())
        print("Название платформы - " + sys.platform)
        print("Кодировка - " + sys.getfilesystemencoding())
        print("Логин текущего пользователя - " + os.getlogin())
        print("Количество ядер CPU - " + str(psutil.cpu_count()))
    elif do == 3:
        print (psutil.pids())
    else:
        pass
elif work == "нет":
    print (name + ", ты лентяй, иди гуляй")
else:
    print (name + ", ну ты подумай, потом зови =)")