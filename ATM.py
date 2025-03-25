class ATM:
    def __init__(self, balance=0):
        self.balance = balance
    
    def check_balance(self):
        print("*****************")
        print(f"Your Balance is ${self.balance:.2f}")
        print("*****************")
    
    def deposit(self):
        print("*****************")
        amount = float(input("Enter an amount to be Deposited: "))
        print("*****************")
        if amount < 0:
            print("*****************")
            print("That's not a valid amount")
            print("*****************")
        else:
            self.balance += amount
    
    def withdraw(self):
        print("*****************")
        amount = float(input("Enter amount to be Withdrawn: ))
        print("*****************")
        if amount > self.balance:
            print("*****************")
            print("Insufficient funds")
            print("*****************")
        elif amount < 0:
            print("*****************")
            print("Amount must be greater than 0")
            print("*****************")
        else:
            self.balance -= amount

def atm_interface():
    atm = ATM(0)
    
    while True:
        print("*****************")
        print("BANKING PROGRAM")
        print("*****************")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("*****************")
        
        choice = input("Enter your choice (1-4):")
        
        switch = {
            '1': atm.check_balance,
            '2': atm.deposit,
            '3': atm.withdraw,
            '4': lambda: print("THANK YOU! HAVE A NICE DAY!\n*****************")
        }

        if (action := switch.get(choice, lambda: print("*****************\nTHIS IS NOT A VALID CHOICE\n*****************")))() or choice == '4':
            break

if __name__ == "__main__":
    atm_interface()

