class ATM:
    def __init__(self, balance=0):
        self.balance = balance
    
    def check_balance(self):
        print("*****************")
        print(f"YOUR BALANCE IS ${self.balance:.2f}")
        print("*****************")
    
    def deposit(self):
        print("*****************")
        amount = float(input("ENTER AN AMOUNT TO BE DEPOSITED:"))
        print("*****************")
        if amount < 0:
            print("*****************")
            print("THAT'S NOT A VALID AMOUNT")
            print("*****************")
        else:
            self.balance += amount
    
    def withdraw(self):
        print("*****************")
        amount = float(input("ENTER AMOUNT TO BE WITHDRAWN:"))
        print("*****************")
        if amount > self.balance:
            print("*****************")
            print("INSUFFICIENT FUNDS")
            print("*****************")
        elif amount < 0:
            print("*****************")
            print("AMOUNT MUST BE GREATER THAN 0")
            print("*****************")
        else:
            self.balance -= amount

def atm_interface():
    atm = ATM(0)
    switch = {
        '1': atm.check_balance,
        '2': atm.deposit,
        '3': atm.withdraw,
        '4': lambda: print("THANK YOU! HAVE A NICE DAY!\n*****************")
    }
    
    while True:
        print("*****************")
        print("BANKING PROGRAM")
        print("*****************")
        print("1. Show Balance")
        print("*****************")
        print("2. Deposit")
        print("*****************")
        print("3. Withdraw")
        print("*****************")
        print("4. Exit")
        print("*****************")
        
        choice = input("ENTER YOUR CHOICE (1-4):")
        action = switch.get(choice, lambda: print("*****************\nTHIS IS NOT A VALID CHOICE\n*****************"))
        if choice == '4':
            action()
            break
        else:
            action()

if __name__ == "__main__":
    atm_interface()

