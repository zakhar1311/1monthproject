# 1спитати в користувача пароль 
# 2занести пароль в базу
# 3спитати пароль
# 4якщо пароль вірний то відкрити, інакше брейк
# 5меню
# 6додати пароль
# 7подивитися паролі
# 8видалити пароль
# 9вийти

import pwinput
with open('masterparol.txt', 'r') as f:
    text = f.read().strip()
    if not text:
        mainparol = pwinput.pwinput("Enter ur master password:\n")
        with open('masterparol.txt', 'a') as f:
            f.write(mainparol)
            print("Sucefully registry!")
            
    elif text:
        
            
        enterparol = pwinput.pwinput("Login: enter ur master password:\n")
        if enterparol == text:
            print("Sucefully registry!")
            while True:
                print("Menu:")
                menu = int(input(" 1.Add a password\n 2.See passwords\n 3.Delete a password\n 4.Exit\n"))
                if menu == 1:
                    site = input("Site name:")
                    password = input("Password:")
                    with open("parols.txt", "a") as file:
                        
                        

                        file.write(f"{site} --> {password}\n")
                        print("Password was added!")
                   
                elif menu == 2:
                    fa = False
                    with open("parols.txt", "r") as file:
                        reads = file.read()
                        print(reads)
                elif menu == 3:
                    deleted = input("What site u want to delete?:\n")
                    with open("parols.txt", 'r') as file:
                        lines = file.readlines()
                    with open("parols.txt", 'w') as file:    
                        for line in lines:
                            if not line.startswith(deleted + " -->"):
                                file.write(line)
                                fa = True
                        with open("parols.txt", "r") as file:
                            a = file.read()

                        if fa:
                            print(f"Site {deleted} was deleted")
                        else:
                            print(f"Site {deleted} has not found")


                elif menu == 4:

                    print("Bye!")
                    break



        else:
            print("Wrong password!")
        

        