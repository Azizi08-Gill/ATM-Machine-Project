import sys
import os
import time

balance = 0.0

def checkbalance(balance):
    print("Your balance is " + str(balance))    

def deposite(balance):
    amount = float(input("Enter the amount you want to deposit: "))
    print("You amount has been deposited to your account successfully!🤗")
    return balance + amount

def withdraw(balance):
    withdraw_money = float(input("Enter the amount you want to withdraw: "))
    if withdraw_money>balance:
        print("You do not have enough money😥")
        return
    else:    
        rest = balance - withdraw_money
        print("You have withdrawn money from your account.")
        print("The remaining balance is = " + str(rest))
    return rest

while True:
    print ("********<MENU>********")
    print("1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
    print("-----------------------")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        os.system("cls" if os.name == "nt" else "clear")
        checkbalance(balance)
    elif choice == 2:
        os.system("cls" if os.name == "nt" else "clear")
        balance = deposite(balance)
    elif choice == 3:
        os.system("cls" if os.name == "nt" else "clear")
        balance = withdraw(balance)
    elif choice == 4:
        print("Exiting the realm of time after")
        for i in range(5,0,-1):
            print(i)
            time.sleep(1)
        print("See you later, may your day be sprinkled with laughter and love")
        sys.exit(0)    
    else:
        print("Invalid choice")
        print("Try any of the options above! :)")
