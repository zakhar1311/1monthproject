import pwinput
file = "passwords.txt"

print("Hi to passwords manager!")
def main_password(sign):
    with open("main.txt", "r") as f:
        
        if not f:
            sign
            with open("main.txt", "w") as file:
                file.write(sign)
                print("Signed sucefully!")
        elif f:
