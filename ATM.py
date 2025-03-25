def show_balance(balance):
    print("************")
    print(f"Your balance is ${balance:.2f}")
    print("************")
def deposit():
    print("************")
    amount=float(input("ENTER AN AMOUNT TO BE DEPOSITED:"))
    print("*****************")
    if amount <0:
        print("*****************")
        print("THAT'S NOT A VALID AMOUNT")
        print("*****************")
        return 0
    else:
        return amount
def withdraw(balance):
    print("*****************")
    amount=float(input("ENTER AMOUNT TO BE WITHDRAWN:"))
    print("*****************")
    if amount > balance:
        print("*****************")
        print("INSUFFICENT FUNDS")
        print("*****************")
        return 0
    elif amount < 0:
        print("*****************")
        print("AMOUNT MUST BE GREATER THAN 0")
        print("*****************")
        return 0
    else:
        return amount

def main():
    balance=0
    is_running=True
    
    while is_running:
        print("*****************")
        print("BANKING PROGRAM")
        print("*****************")
        print("1.SHOW BALANCE")
        print("*****************")
        print("2.DEPOSIT")
        print("*****************")
        print("3.WITHDRAW")
        print("*****************")
        print("4.EXIT")
        print("*****************")
            
        choice=input("ENTER YOUR CHOICE (1-4):")
        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running=False
        else:
            print("*****************")
            print("THIS IS NOT A VALID CHOICE")
            print("*****************")
    print("*****************")
    print("THANK YOU! HAVE A NICE DAY!")
    print("*****************")

if __name__ =='__main__':
    main()
