def add(a, b):
    print("Result:", a+b)
def min(a, b):
    print("Result:", a-b)
def mno(a, b):
    print("Result:", a*b)
def dil(a, b):
    print("Result:", a/b)
while True:
    try:
        first = int(input('Enter ur first number:'))
        second = int(input("Enter ur second number:"))
        symbol = int(input('|1.+, 2.-, 3.*, 4.:|'))
        if symbol == 1:
            add(first, second)
        elif symbol == 2:
            min(first, second)
        elif symbol == 3:
            mno(first, second)
        elif symbol == 4:
            dil(first, second)
        else:
            print('U enter wrong number')
    except ValueError:
        print("U enter a letter")