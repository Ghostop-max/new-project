class Atm:
    pin = 1234

    def __init__(self):
        self.balance = 0

    def display_balance(self):
        print("------------------------------------------------------------------------------------")
        print("Your current balance is ₹", self.balance)

    def deposit(self):
        deposit = int(input("How much money would you like to deposit: ₹ "))
        self.balance += deposit
        print("------------------------------------------------------------------------------------")
        print("After depositing, your updated balance is: ₹", self.balance)

    def withdraw(self):
        withdraw = int(input("How much money would you like to withdraw: ₹ "))
        if withdraw > self.balance:
            print("------------------------------------------------------------------------------------")
            print("Insufficient funds. Withdrawal failed.")
        else:
            self.balance -= withdraw
            print("------------------------------------------------------------------------------------")
            print("After withdrawing, your updated balance is: ₹", self.balance)

    def main(self):
        chances = 3
        print('************************************************************************************')
        print("     ꕤꕤ Welcome to Admin Bank! ꕤꕤ     ")
        print("     --Please Enter your card--        \n")
        print('************************************************************************************')
        while chances != 0:
            pin = int(input("Please enter the Four-digit Pin: "))
            if pin != self.pin:
                chances -= 1
                print("------------------------------------------------------------------------------------")
                print(f"You have entered the wrong pin. Please try again (Only {chances} chances left)")
                print("------------------------------------------------------------------------------------")
            else:
                while True:
                    print("✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽")
                    print("What would you like to do?")
                    print("1. Display Balance")
                    print("2. Deposit Money")
                    print("3. Withdraw Money")
                    print("4. Exit")
                    print("✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽")
                    choice = int(input("Enter your choice :"))
                    if choice == 1:
                        self.display_balance()
                    elif choice == 2:
                        self.deposit()
                    elif choice == 3:
                        self.withdraw()
                    elif choice == 4:
                        print("Exiting the program. Thank you!")
                        return
                    else:
                        print("Invalid choice")


customer = Atm()
customer.main()
