phonebook = {}
print("Welcome to phone book!")
while True:
    vibor = int(input("1.Add a phone number\n2.See phone book\n3.Delete number\n4.Exit\n"))
    if vibor == 1:
        name = input("Contact name:")
        num = input("Contact number:")
        phonebook[name] = num 
        print(f"Contact {name} was added!")
    elif vibor == 2:
        if phonebook:
            for name, num in phonebook.items():
                print(f"{name}:{num}")
        else:
            print("Theres nothing in ur phone book")
    elif vibor == 3:

        pop = input("Which contact u want do delete:")
        if pop in phonebook:
            phonebook.pop(pop)
            print(f"Contact {pop} was deleted!")
        else:
            print(f"Contact {pop} was not found!")
    elif vibor == 4:
        print("Bye!") 
        break
        

