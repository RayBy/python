import os

name = input ("Введите имя: ")
print ("Привет, " + name)

work = input ("Хочешь поработать? (да/нет)")
if work == 'да':
    print ("Отлично!")
    print ("Я умею:")
    print("[1] - Вывести список файлов в текущей директории")
    print("[2] - Вывести информацию о системе")
    do = int(input ("Укажите номер действия: "))
    if do == 1:
        print (os.listdir())
    elif do == 2:
        pass
    else:
        pass
elif work == "нет":
    print (name + ", ты лентяй, иди гуляй")
else:
    print (name + ", ну ты подумай, потом зови =)")