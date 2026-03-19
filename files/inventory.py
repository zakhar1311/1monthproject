import time
import random
timee = 5
axe = False
inventory = {
    "wood" : 10,
    "rock" : 5,
    "coal" : 1,
    "torch" : 0,
    "pickaxe" : 0




}
uses = 0
def farm(chas, ore, x):
    global uses, axe
    b = 0.5
    if uses >= 1:
        b = 0.25
    if axe:
        b = b / 2
    for a in range(chas):
        print(chas)
        chas -= 1
        time.sleep(b)
    inventory[ore] += x
    print(f"U farmed {x} {ore}")
    if uses >= 1:
        uses -= 1
    
    


def use_items(ask):
    global uses, axe
    ask
    if ask == 1:
        if inventory["torch"] >= 1:
            inventory["torch"] -= 1
            uses = 3
            print("Torch used! Now farming faster for 3 times!")
    elif ask == 2:
        if inventory["pickaxe"] >= 1:
            axe = True
            print("Pickaxe used! Now farming faster!")
        
                
       

            

def see_inventory():
    
    for key, items in inventory.items():
        print(key, ":", items)

def craft_items(ask):
    global torch, pickaxe, wood, coal, rock, inventory
    ask  #1.fakel   2.kurka
    if ask == 1:
        if inventory["wood"] >= 2 and inventory["coal"] >= 1:
            inventory["torch"] += 1
            inventory["wood"] -= 2
            inventory["coal"] -= 1
            print("Torch added to ur inventory")
        else:
            print("Not enought materials!")
    elif ask == 2:
        if inventory["wood"] >= 2 and inventory["rock"] >= 3:
            inventory["rock"] -= 3
            inventory["wood"] -= 2
            inventory["pickaxe"] += 1
            print("Pickaxe added to ur inventory")
        else:
            print("Not enought materials")
    

while True:
    choice = int(input("1.Farming\n2.Use thing\n3.See inventory\n4.Craft items\n"))

    if choice == 1:
        farmc = int(input("What do u want to farm:\nwood\nrock\ncoal\n"))
        woods = random.randint(2, 5)
        rocks = random.randint(1, 3)
        coals = random.randint(1, 2)
        if farmc == 1:
            farm(7, "wood", woods)
        elif farmc == 2:
            farm(10,"rock", rocks)
        elif farmc == 3:
            farm(15, "coal", coals)
        else:
            print("U enter wrong symbol, please enter 1, 2 or 3")
    elif choice == 2:
        use_items(int(input("1.Torch     2.Pickaxe\n")))
    elif choice == 3:
        see_inventory()
    elif choice == 4:
        craft_items(int(input("1.Torch     2.Pickaxe\n")))
            
