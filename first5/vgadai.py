import random
def num(bot, people):
    
    if people > bot:
        return "Число менше "
    elif people < bot:
        return "Число більше "
        
    elif people == bot:
        return "Вгадав"
        
b = random.randint(1, 10)
while True:        
    a = int(input("Take up your number:"))
    h = num(b, a)
    print(h)
    if h == "Вгадав":
        break
