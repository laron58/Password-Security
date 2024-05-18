import string
import time

global safe 
safe = False
global cooldown
cooldown = False
global cracked
cracked = False
global timer
timer = 0

while safe is False:
    pwd = input("Please enter a password:\n")
    file = open("passList.txt", "r")
    pwdList = file.read()
    if pwd in pwdList:
        print("Password too common!")
    elif any(c in pwd for c in string.ascii_lowercase) is False:
        print("Password must have a lowercase letter!")
    elif any(c in pwd for c in string.ascii_uppercase) is False:
        print("Password must have an uppercase letter!")
    elif any(c in pwd for c in string.digits) is False:
        print("Password must have a number!")
    elif len(pwd) < 12:
        print("Password must be at least 12 characters long!")
    elif any(c in pwd for c in string.punctuation) is False:
        print("Password must have a special character!")
    else: 
        print("Congratulations! You have created a strong password!")
        safe = True
    
while cracked is False:
    for i in range (5):
        if cooldown is True:
            timer += 5
            print(f"On cooldown for {timer} seconds...")
            time.sleep(timer)
            cooldown = False
        if pwd == input("\nCrack your password:\n"):
            print("Password cracked successfully.")
            cracked = True
            break
        elif i == 4:
            print("Too many attempts! Cooldown initiating...")
            cooldown = True
