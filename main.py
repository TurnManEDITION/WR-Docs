import os

answer = str(input("What do you want to do?(W/R): "))
os.system("cls")
if answer.lower() == "w" or answer.lower() == "write":
    while True:
        print("Mode 'write'")
        surname = input("Enter surname:         ")
        if len(surname) > 20 or len(surname) == 0:
            os.system("cls")
        else:
            break
    while True:
        name = input("Enter name:            ")
        if len(name) > 15 or len(name) == 0:
            os.system("cls")
            print("Mode 'write'")
            print(f"Enter surname:         {surname}")
        else:
            break
    while True:
        patronymic = input("Enter patronymic:      ")
        if len(patronymic) > 25 or len(patronymic) == 0:
            os.system("cls")
            print("Mode 'write'")
            print(f"Enter surname:         {surname}")
            print(f"Enter name:            {name}")
        else:
            break
    while True:
        try:
            age = int(input("Enter age:             "))
            if len(str(age)) > 3:
                os.system("cls")
                print("Mode 'write'")
                print(f"Enter surname:         {surname}")
                print(f"Enter name:            {name}")
                print(f"Enter patronymic:      {patronymic}")
            else:
                break
        except ValueError:
            os.system("cls")
            print("Mode 'write'")
            print(f"Enter surname:         {surname}")
            print(f"Enter name:            {name}")
            print(f"Enter patronymic:      {patronymic}")
    while True:
        try:
            id1 = input("Enter passport series: ")
            if id1 == "no" or id1 == "No":
                id = "NO"
                break
            elif int(len(str(id1))) == 4:
                id = ""
                break
            else:
                os.system("cls")
                print("Mode 'write'")
                print(f"Enter surname:         {surname}")
                print(f"Enter name:            {name}")
                print(f"Enter patronymic:      {patronymic}")
                print(f"Enter age:             {age}")
        except ValueError:
            os.system("cls")
            print("Mode 'write'")
            print(f"Enter surname:         {surname}")
            print(f"Enter name:            {name}")
            print(f"Enter patronymic:      {patronymic}")
            print(f"Enter age:             {age}")
    while id == "":
        try:
            id2 = int(input("Enter passport number: "))
            if len(str(id2)) == 6:
                id = str(id1) + "-" + str(id2)
                break
            else:
                os.system("cls")
                print("Mode 'write'")
                print(f"Enter surname:         {surname}")
                print(f"Enter name:            {name}")
                print(f"Enter patronymic:      {patronymic}")
                print(f"Enter age:             {age}")
                print(f"Enter passport series: {id1}")
        except ValueError:
            os.system("cls")
            print("Mode 'write'")
            print(f"Enter surname:         {surname}")
            print(f"Enter name:            {name}")
            print(f"Enter patronymic:      {patronymic}")
            print(f"Enter age:             {age}")
            print(f"Enter passport series: {id1}")

    data = (f"Surname    : {surname}\n"
            f"Name       : {name}\n"
            f"Patronymic : {patronymic}\n"
            f"Age        : {age}\n"
            f"ID         : {id}")

    retry = ''
    i = 1
    o = 0
    while True:
        if len(data) >= i:
            a = data[o]
            retry = retry + str(ord(a)) + ' '
            i += 1
            o += 1
        else:
            del i, o
            break

    data = retry[:-1]

    data = data.split()
    count = len(data)
    i = 0
    datas = ""
    while i != count:
        datas += hex(int(data[i])) + "-"
        i += 1
    datas = datas[:-1]
    if os.path.isdir("People"):
        pass
    else:
        os.mkdir("People")
    if os.path.isdir(f"People"):
        with open(f"People/{surname}{name}{age}.dat", "w", encoding="utf-8") as file:
            file.write(datas)
        with open(f"People/{surname}{name}{age}.dat", "r") as file:
            data = file.read()
        os.system("cls")
        print(data)
    else:
        os.mkdir(f"People")
        with open(f"People/{surname}{name}{age}.dat", "w", encoding="utf-8") as file:
            file.write(datas)
        with open(f"People/{surname}{name}{age}.dat", "r") as file:
            data = file.read()
        os.system("cls")
        print(data)


elif answer.lower() == "r" or answer.lower() == "read":
    while True:
        print("Mode 'read'")
        surname = input("Enter surname:         ")
        if len(surname) > 20 or len(surname) == 0:
            os.system("cls")
        else:
            break
    while True:
        name = input("Enter name:            ")
        if len(name) > 15 or len(name) == 0:
            os.system("cls")
            print("Mode 'read'")
            print(f"Enter surname:         {surname}")
        else:
            break
    while True:
        try:
            age = int(input("Enter age:             "))
            if len(str(age)) > 3:
                os.system("cls")
                print("Mode 'read'")
                print(f"Enter surname:         {surname}")
                print(f"Enter name:            {name}")
            else:
                break
        except ValueError:
            os.system("cls")
            print("Mode 'read'")
            print(f"Enter surname:         {surname}")
            print(f"Enter name:            {name}")
    try:
        with open(f"People/{surname}{name}{age}.dat", "r") as file:
            data = file.read()
    except FileNotFoundError:
        print("Error: '394'")
        os.system("pause")
        exit()
    data = data.replace("-", " ").split()
    count = len(data)
    i = 0
    datas = ""
    while i != count:
        datas += str(int(data[i], 16)) + " "
        i += 1
    datas = datas.split()
    i = 0
    data = ""
    while i != count:
        data += str(chr(int(datas[i])))
        i += 1
    os.system("cls")
    print(data[:-1])
else:
    print("Error: '394'")
os.system("pause")