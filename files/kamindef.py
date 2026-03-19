import random
import time
g = 0
e = 0
draw = 0
win = 0
lose = 0
print("Гра камінь ножниці папір")
#1 kamin 2 noznuci 3 papir
try:
    def gameplay(): #num 1 or  2 or 3 a = 3
        global g, e, win, lose, draw
        
        npc = random.randint(1, 3)
        people = int(input(("1.Камінь     2.Ножниці    3.Папір\n Ваш вибір:")))
        print(3)
        time.sleep(0.3)
        print(2)
        time.sleep(0.3)
        print(1)
        time.sleep(0.3)
        

        if npc == people:
            print("Нічия. Бот вибрав", 
            "Камінь" if npc == 1 else
            "Ножниці" if npc == 2 else
            "Папір")
            draw += 1
            with open('kamin.txt', 'a') as file:
                file.write("Draw\n")
        elif(people == 1 and npc == 2) or \
            (people == 2 and npc == 3) or \
            (people == 3 and npc == 1):
            g += 1
            print("Виграш. Бот вибрав", 
            "Камінь" if npc == 1 else
            "Ножниці" if npc == 2 else
            "Папір"  )
            win += 1
            with open('kamin.txt', 'a') as file:
                file.write("Win\n")
        
        elif(people == 1 and npc == 3) or \
            (people == 2 and npc == 1) or \
            (people == 3 and npc == 2):
            e += 1
            print("Програш. Бот вибрав", 
            "Камінь" if npc == 1 else
            "Ножниці" if npc == 2 else
            "Папір" )
            with open('kamin.txt', 'a') as file:
                file.write("Losee\n")
            lose += 1
        else:
            print("Wrong number😑")
        

    while True:
        a = int(input("1.Грати    2.Подивитися стату\nВаш вибір:\n"))
        if a == 1:
            gameplay()
        elif a == 2:
            with open('kamin.txt', 'r') as f:
                print(f.read())
except ValueError:
    pass
            