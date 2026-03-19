#1спитати користувача його дію
#2.в випадку якщо занести, то занести його дію в файл 
#3. в випадку якщо подивитися, файл прочитати
#4. в випадку якщо видалити, видалити останній текст.
print("Hi to todolist")
main = int(input("1.Open program     2.Exit\n"))
if main == 1:
    while True:
        print("Take ur option:")
        
        ask = int(input("1.Open list\n2.Add a task\n3.Exit\n"))
        if ask == 1: 
            with open('list.txt', 'r') as f:
                tasks = f.read()
               
            if tasks.strip():
                print(f"Ur tasks: \n {tasks}")
            else:
                print("U dont add any tasks")

          
        elif ask == 2:
            task = str(input("What do u want to add?\n"))
            status = input("Status: 1.✅    2.❌\n")
            if status == "1":
                status = "Done"
                
            elif status == "2":
                status = "Not completed"
                
            a = {task : status}


            with open("list.txt", 'a') as f:
                f.write(a)
            print(f"Task |{task}| was added")

        elif ask == 3:
            break
        else:
            print("U input wrong number")
else:
    print("Bye!")