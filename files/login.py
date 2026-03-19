accounts = {}
while True:
    main = int(input("1.Register\n2.Login\n3.See accounts\n"))
    if main == 1:
        user = input("Enter ur login:\n")
        
        password = input("Enter ur password:\n")
        

        accounts[user] = password
        print("Account sucefully added!")
    elif main == 2:
        luser = input("Enter ur login:\n")
        

        lpassword = input("Enter ur password:\n")
        
        if luser in accounts.keys():
            if lpassword == accounts.get(luser):
                print("Sucefully logined!")
            else:
                print("Wrong password!")
        else:
            print(f"Login {luser} was no found!")
    elif main == 3:
        if accounts:
            for user, password in accounts.items():
                print(f"{user} : {password}")
        else:
            print("There is no one account")
