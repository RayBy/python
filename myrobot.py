import os
import psutil
import sys
import shutil

def duplicate(file_name):
    if os.path.isfile(file_name):
        copy_file = file_name + '.copy'
        shutil.copy(file_name, copy_file)
        if os.path.exists(file_name):
            print("Дубликат файла", file_name, "был успешно создан")
            return True
        else:
            print("Возникли проблемы с созданием дубликата файла", file_name)
            return False

def del_duplicate(dir_name):
    d = 0
    file_list = os.listdir(dir_name)
    for f in file_list:
        copy_file_name = os.path.join(dir_name, f)
        if copy_file_name.endswith('.copy'):
            os.remove(copy_file_name)
            if not os.path.exists(copy_file_name):
                d = d + 1
                print("Файл ", copy_file_name, " был успешно удален")
                print("Было удалено", d, "файлов")
    return d

def sys_info():
    print("# Информация о системе #")
    print("Текущая директория - ", os.getcwd())
    print("Название платформы - ", sys.platform)
    print("Кодировка - ", sys.getfilesystemencoding())
    print("Логин текущего пользователя - ", os.getlogin())
    print("Количество ядер CPU - ", str(psutil.cpu_count()))

def main():
    print ("# Вы запустили робота-помощника #")
    name = input("Введите Ваше имя: ")
    print("Добрый день, ", name, ". Чем я могу тебе помочь?.")

    work = ''
    while work != 'выход':
        work = input("Хочешь поработать? (да/нет/выход)")
        if work == 'да':
            print("Отлично!")
            print("Что будем делать?:")
            print("[1] - Вывести список файлов в текущей директории")
            print("[2] - Вывести информацию о системе")
            print("[3] - Вывести список активных процессов")
            print("[4] - Провести операции с файлами")
            do = int(input("Укажите номер действия: "))
            if do == 1:
                print("# Список файлов в текущей директории #")
                print(os.listdir())
            elif do == 2:
                sys_info()
            elif do == 3:
                print("# Список активных процессов #")
                print(psutil.pids())
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
                    print("# Создание дубликата файла #")
                    file_name = input("Введите имя файла: ")
                    duplicate(file_name)
                elif file == 3:
                    print("# Удаление дубликатов файлов из выбранной директории #")
                    dir_name = input("Укажите имя директории: ")
                    del_duplicate(dir_name)
                else:
                    print("Недопустимое действие")
            else:
                pass
        elif work == "нет":
            print("Жаль, ну если передумаешь заходи. Пока " + name)
        else:
            pass

if __name__ == "__main__":
    main()