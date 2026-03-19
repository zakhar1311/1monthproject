d = 1
c = 1
while True:
    a = int(input("1.Регістрація      2.Заєструватися\n"))
        
    if a == 1:
        b = str(input("Введіть логін:\n"))
        s = str(input("Введіть пароль:\n"))
        with open('logins.txt', 'a') as file:
            
            file.write(b + "\n")
        with open('passwords.txt', 'a') as file:
            file.write(s + "\n")
        print("Успішно заєстровано!")

    elif a == 2:
        login = input("Введіть логін:")
        password = input("Введіть пароль:")
        with open('logins.txt', 'r') as file:
            logins = file.read()
            
        with open('passwords.txt', 'r') as file:
            passwords = file.read()
        if login + '\n' in logins:
            index = logins.index(login)
            if password + "\n" == password(index, "\n"):
                print("Успішно ввійдено!")
            else:
                print("Неправильний пароль!")
        else:
            print("Логін не знайдено")


