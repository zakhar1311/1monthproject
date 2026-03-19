products = ["bread", "milk", "cheese"]
prices = [25, 60, 110]
budgete = 250
bread = 0
milk = 0
cheese = 0

def buy(x):
    global budgete, bread, milk, cheese
    if budgete >= prices[x]:

        print(f"u put {products[x]} into bucket")
        budgete -= prices[x]
        if x == 1:
            bread += 1
        elif x == 2:
            milk += 1
        elif x == 3:
            cheese += 1
        print(f" u have {budgete}$ left")
    else:
            print("not enough dollars")


def s4(fnum, typef, typef2, food):
    if fnum == 0:
        print(f"u dont buy any {food}\n")
    elif fnum == 1:
        print(f"u buy 1 {typef} of {food}\n")
    else:
         print(f"u buy {fnum} {typef2} of {food}\n")


print("u in a magazine")
print("ur budgete is 250$")
while True:
    s = int(input(f"what do u want to buy:\n1.{products[0]} --> {prices[0]}\n2.{products[1]} --> {prices[1]}\n3.{products[2]} --> {prices[2]}\n4.Go to cash register\n"))
    if s == 1:
        buy(0)
    elif s == 2:
        buy(1)
    elif s == 3:
        buy(2)
    elif s == 4:

        s4(bread, "loaf", "loaves", "bread" )
        s4(milk, "bottle", "bottles", "milk")
        s4(cheese, "00g", "00g", "cheese")
        print(f"u have {budgete}$ left")
        break
              