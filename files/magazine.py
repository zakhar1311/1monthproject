products = ["bread", "milk", "cheese"]


prices = [25, 60, 110]
print("u in a magazine")
budgete = 250
bread = 0
milk = 0
cheese = 0
print("ur budgete is 250$")
while True:
    s = int(input(f"what do u want to buy:\n1.{products[0]} --> {prices[0]}\n2.{products[1]} --> {prices[1]}\n3.{products[2]} --> {prices[2]}\n4.Go to cash register\n5.See your freezer"))
    if s == 1:
        if budgete >= prices[0]:

            print(f"u put {products[0]} into bucket")
            budgete -= prices[0]
            bread += 1
            print(f" u have {budgete}$ left")
           
        else:
             print("not enough dollars")
    elif s == 2:
        if budgete >= prices[1]:
            print(f"u put {products[1]} into bucket")
            budgete -= prices[1]
            milk += 1
            print(f" u have {budgete}$ left")
        else:
            print("not enough dollars")
    elif s == 3:
        if budgete >= prices[2]:
            print(f"u put {products[2]} into bucket")
            budgete -= prices[2]
            cheese += 1
            print(f" u have {budgete}$ left")
        else:
            print("nou enough dollars") 
    elif s == 4:
        if bread == 0:
            print("u dont buy any bread\n")
        elif bread == 1:
            print("u buy 1 loaf of bread\n")
        else:
            print(f"u buy {bread} loaves of bread\n")


        if milk == 0:
            print("u dont buy any milk\n")
        elif milk == 1:
            print("u buy 1 bottle of milk\n")
        else:
            print(f"u buy {milk} bottles of milk\n")



        if cheese == 0:
            print("u dont buy any cheese\n")
        elif cheese == 1:
            print("u buy 100g of cheese\n")
        else:
            print(f"u buy {cheese}00g of cheese\n")



        print(f"u have {budgete}$ left")
        break
