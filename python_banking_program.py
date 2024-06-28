def show_balance():
    print("***********************************************************************************************************")
    print(f"Your balance is Ksh.{balance:.2f}")
    print("***********************************************************************************************************")


def deposit():
    print("***********************************************************************************************************")
    amount = float(input("Enter amount you wish to deposit: "))
    print("***********************************************************************************************************")
    
    if amount <= 0:
        print("Amount should be more than Ksh. 0")
        return 0
    else:
        print(f"You have deposited Ksh. {amount}")
        return amount
    
    
    

def withdraw():
    print("***********************************************************************************************************")
    amount = float(input("Enter amount you wish to withdraw: "))
    print("***********************************************************************************************************")
    
    if amount <= 0:
        print("Please enter a number more than zero")
        return 0
    elif amount > balance:
        print("The amount you wish to withdraw is more than your avaialble balance.")
        return 0
    else:
        print(f"You have withdrawn Ksh. {amount}")
        return amount


balance = 0
is_running = True

while is_running:
    print("1.Show balance")
    print("2.Deposit amount")
    print("3.Withdraw amount")
    print("4.Exit program")
    
    print("***********************************************************************************************************")
    choice = input(f"Enter your choice(1-4): ")
    print("***********************************************************************************************************")
    
    if choice == "1":
        show_balance()
    elif choice == "2":
        balance += deposit()
    elif choice == "3":
        balance -= withdraw()
    elif choice == "4":
        is_running = False
    else:
        print("Please enter a valid choice.")   
        
    print("Thank you have a nice day!!") 
