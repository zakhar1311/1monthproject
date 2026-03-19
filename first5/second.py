import random
from colorama import Back, init, Style, Fore
q = 1
init(autoreset=True)
while True:
    print(Style.BRIGHT + "Гра вгадай число")

    print(Style.BRIGHT + "Вибери рівень складності:")
    print(Style.BRIGHT + "1.Легкий", Style.BRIGHT + "2.Нормальний", Style.BRIGHT + "3.Тяжкий")
    w = int(input(""))
    if w == 1:
        a = random.randint(1, 10)
        r = 7
        print(Style.BRIGHT + "Число від 1 до 10. Кількість спроб:", r)
        while True:
            try:
                b = int(input(Style.BRIGHT + 'Вгадай число:'))
            except ValueError:
                print("Ти ввів неправильний символ.")
                continue
            if a != b:
                q += 1
                r -= 1
                
            
                if a > b:
                    print(Style.BRIGHT + "Неправильно,число більше ніж", b)
                    print(Style.BRIGHT + "Лишилося спроб:", r)
                    if r == 0:
                        print(Style.BRIGHT + "Ти потратив всі спроби.😭")
                        break
                elif a < b:
                    print(Style.BRIGHT + "Неправильно, число менше ніж", b)
                    print(Style.BRIGHT + "Лишилося спроб:", r)

                    if r == 0:
                        print(Style.BRIGHT + "Ти потратив всі спроби.😭")
                        break
            elif a == b:
            
                print(Style.BRIGHT + "Молодець, число було:",a,"Кількість спроб:", q  )
                q =1 
                break
    elif w == 2:
        a = random.randint(1, 50)
        r = 6
        print(Style.BRIGHT + "Число від 1 до 50")
        while True:
            try:
                
                b = int(input(Style.BRIGHT + 'Вгадай число:'))
            except ValueError:
                print("Ти ввів неправильний символ")
                continue
            
            if a != b:
                q += 1
                r -= 1
                
                
                if a > b:
                    print(Style.BRIGHT + "Неправильно, число більше ніж", b)
                    print(Style.BRIGHT + "Лишилося спроб:", r)
                    if r == 0:
                        print(Style.BRIGHT + "Ти потратив всі спроби.😭")
                        break
                    
                elif a < b:
                    print(Style.BRIGHT + "Неправильно, число менше ніж", b)
                    print(Style.BRIGHT + "Лишилося спроб:", r)
                    if r == 0:
                        print(Style.BRIGHT + "Ти потратив всі спроби.😭")
                        break
            elif a == b:
            
                print(Style.BRIGHT + "Молодець, число було:",a,"Кількість спроб:", q  )
                q = 1
                break
            
    elif w == 3:
        a = random.randint(1, 100)
        r = 8
        print(Style.BRIGHT + "Число від 1 до 100")

        while True:
            try:
                b = int(input(Style.BRIGHT + 'Вгадай число:'))
            except ValueError:
                print("Ти ввів неправильний символ")
                continue
            if a != b:
                q += 1                
                
                r -= 1
                if a > b:
                    print(Style.BRIGHT + "Неправильно, число більше ніж", b)
                    print(Style.BRIGHT + "Лишилося спроб:", r)
                    if r == 0:
                        print(Style.BRIGHT + "Ти потратив всі спроби.😭")
                        break
                elif a < b:
                    print(Style.BRIGHT + "Неправильно, число менше ніж", b)
                    print(Style.BRIGHT + "Лишилося спроб:", r)
                    if r == 0:
                        print(Style.BRIGHT + "Ти потратив всі спроби.😭")
                        break
            elif a == b:
            
                print(Style.BRIGHT + "Молодець, число було:",a,"Кількість спроб:", q  )
            
                q = 1
                break
            
