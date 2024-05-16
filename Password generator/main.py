import random
password = []
passw =""

alpha="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
num=[x for x in range(0,10)]
special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '_', '-', '+', '=', '|', '\\', '~', '`', ':', ';', '"', "'", '<', '>', '/', '?', ',', '.']

print("Welcome to the random password generator")
length = int(input("How many letters would you like in your password? (Minimum 7 characters long): "))
if length<7:
    print("Length of password set to 7".center(100),"\n")
    length=7

symbols = int(input("How many symbols would you like? "))
if symbols > length:
    print(f"\nYou cann't have {symbols} symbols in a password of length {length} !!!".center(100),"\n")

else:
    numbers = int(input("How many numbers would you like? "))
    if numbers + symbols > length:
        print(f"\nYou cann't have {numbers} numbers and {symbols} symbols in a password of length {length} !!!".center(100),"\n")
        
    else:
        for i in range(symbols):
            password.append(random.choice(special_characters))

        for i in range(numbers):
            password.append(random.choice(num))

        for i in range(length-symbols-numbers):
            password.append(random.choice(alpha))
            
        for i in range(random.choice(num)):
            random.shuffle(password)

        password = [str(x) for x in password]
        passw = "".join(password)

        print(f"Here is your password:\n{passw}")
        
        with open("passwords.txt","a") as file:

            file.write(f"{passw}\n")
    
        print("check passwords.txt file")
