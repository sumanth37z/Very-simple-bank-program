#VERY SIMPLE BANKING PROGRAM


def show_balance(balance):
    print("-------------------------------")
    print(f"Your balance is ₹{balance:.2f}")
    print("-------------------------------")

def deposit():
    print("-------------------------------")
    amount = float(input("How much would you like to deposit: "))
    print("-------------------------------")
    if amount < 0 :
        print("Invalid amount")
        return 0
    else:
        return amount

def withdraw(balance):
    print("-------------------------------")
    amount = float(input("How much would you like to withdraw: "))
    print("-------------------------------")

    if amount > balance:
        print("-------------------------------")
        print("Insufficient Funds :0")
        print("-------------------------------")
        return 0
    elif amount < 0:
        print("-------------------------------")
        print("Amount must be greater than 0")
        print("-------------------------------")
        return 0
    else:
        return amount



def main():
    balance = 0
    is_running = True
    while is_running:
        print("----------------------------")
        print("         Ken Bank           ")
        print("----------------------------")
        print("1. Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("----------------------------")

        choice = input("What can we do for you (Please select an option from above): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("Please select from the options provided ^-^")

    print("Thanks for using our services ;) ")


if __name__ == '__main__':
    main()
