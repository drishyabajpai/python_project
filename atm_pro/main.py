
import json
import os
from datetime import datetime

FILE = "accounts.json"

class ATMError(Exception):
    pass

class InvalidPinError(ATMError):
    pass

class InsufficientBalanceError(ATMError):
    pass

class InvalidAmountError(ATMError):
    pass

class AccountExistsError(ATMError):
    pass

def load():
    if os.path.exists(FILE):
        with open(FILE,"r") as f:
            return json.load(f)
    return {}

def save():
    with open(FILE,"w") as f:
        json.dump(accounts,f,indent=4)

accounts = load()

def create():
    user=input("Username: ").strip()
    if user in accounts:
        raise AccountExistsError("Username already exists.")
    pin=input("4-digit PIN: ")
    if len(pin)!=4 or not pin.isdigit():
        raise InvalidPinError("PIN must be exactly 4 digits.")
    accounts[user]={
        "pin":pin,
        "balance":0,
        "history":[],
        "failed":0
    }
    save()
    print("Account created.")

def login():
    user=input("Username: ").strip()
    if user not in accounts:
        print("User not found.")
        return
    if accounts[user]["failed"]>=3:
        print("Account locked.")
        return
    pin=input("PIN: ")
    if pin!=accounts[user]["pin"]:
        accounts[user]["failed"]+=1
        save()
        print(f"Wrong PIN. Attempts: {accounts[user]['failed']}/3")
        return
    accounts[user]["failed"]=0
    save()
    session(user)

def add_history(user,msg):
    ts=datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    accounts[user]["history"].append(f"{ts} | {msg}")

def deposit(user):
    amt=float(input("Amount: "))
    if amt<=0:
        raise InvalidAmountError("Amount must be positive.")
    accounts[user]["balance"]+=amt
    add_history(user,f"Deposit ₹{amt:.2f}")
    save()
    print("Deposit successful.")

def withdraw(user):
    amt=float(input("Amount: "))
    if amt<=0:
        raise InvalidAmountError("Amount must be positive.")
    if amt>25000:
        raise InvalidAmountError("Daily single transaction limit ₹25000.")
    if amt>accounts[user]["balance"]:
        raise InsufficientBalanceError("Insufficient balance.")
    accounts[user]["balance"]-=amt
    add_history(user,f"Withdraw ₹{amt:.2f}")
    save()
    print("Withdrawal successful.")

def change_pin(user):
    old=input("Old PIN: ")
    if old!=accounts[user]["pin"]:
        raise InvalidPinError("Incorrect old PIN.")
    new=input("New 4-digit PIN: ")
    if len(new)!=4 or not new.isdigit():
        raise InvalidPinError("Invalid new PIN.")
    accounts[user]["pin"]=new
    save()
    print("PIN changed.")

def history(user):
    print("\n--- Transaction History ---")
    if not accounts[user]["history"]:
        print("No transactions.")
    else:
        for item in accounts[user]["history"]:
            print(item)

def session(user):
    while True:
        print(f"\nWelcome {user}")
        print("1.Check Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Change PIN")
        print("5.Transaction History")
        print("6.Logout")
        ch=input("Choice: ")
        try:
            if ch=="1":
                print(f"Balance: ₹{accounts[user]['balance']:.2f}")
            elif ch=="2":
                deposit(user)
            elif ch=="3":
                withdraw(user)
            elif ch=="4":
                change_pin(user)
            elif ch=="5":
                history(user)
            elif ch=="6":
                break
            else:
                print("Invalid choice.")
        except ATMError as e:
            print("Error:",e)

while True:
    print("\n=== PYTHON ATM ===")
    print("1.Create Account")
    print("2.Login")
    print("3.Exit")
    c=input("Choice: ")
    try:
        if c=="1":
            create()
        elif c=="2":
            login()
        elif c=="3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
    except ATMError as e:
        print("Error:",e)
