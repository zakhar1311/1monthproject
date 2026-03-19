import random
import time
print("Гра камінь ножниці папір!")
print("Гра до 3 перемог")
w = 0 # pepl peremogs
q = 0 #bot peremogs
try:
    while True:

        a = 3
        npc = random.randint(1, 3)
        print('Ваш вибір:')
        print("1.Камінь    2.Ножниці    3.Папір")
        plr = int(input(""))
        #1 kamin 2 noznuci 3 papir
        while a > 0:
            print(a)
            time.sleep(0.3)
            a -= 1
            if a == 0:
                break
        if npc == 1:
            if plr == 1:
                print("Нічия. Бот вибрав камінь.")
                
            elif plr == 2:
                print("Програш. Бот вибрав камінь.")
                w += 1 
            elif plr == 3:
                print("Ви виграли. Бот вибрав камінь.")
                q += 1
            else:
                print("Ви ввели непраильний символ.")
        elif npc == 2:
            if plr == 1:
                print("Ви виграли. Бот вибрав ножниці.")
                q += 1
            elif plr == 2:
                print("Нічия. Бот вибрав ножниці.")
            elif plr == 3:
                print("Програш. Бот вибрав ножниці.")
                w += 1
            else:
                print("Ви ввели непраильний символ.")
        elif npc == 3:
            if plr == 1:
                print("Програш. Бот вибрав папір.")
                w += 1
            elif plr == 2:
                print("Ви виграли. Бот вибрав папір.")
                q += 1
            elif plr == 3:
                print("Нічия. Бот вибрав папір")
            else:
                print("Ви ввели непраильний символ.")
        if q == 3:
            print("Ви виграли бота!")
            break
        elif w == 3:
            print("Ви програли😭")
            break
        else:
            continue
except ValueError:
    pass        