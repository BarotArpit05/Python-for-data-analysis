# Banking System in which Account holder can Debit, Credit, and Check the balance of it 

class Bank:
    Bank_Name="Union Bank"
    def __init__(self,name,acc_no,balance=0):
        self.acc_no=acc_no
        self.name=name
        self.balance=balance
    def debit(self,amount):
        if amount>=0:
            self.balance += amount
            print("Amount Deposited Successfully")
            print(f"Current Balance is :{self.balance}")
        else:
            print("Enter Valid Amount")
    
    def credit(self,amount):
        if amount>0 and amount<=self.balance:
            self.balance -= amount
            print(f"Amount Credited Successfully")
            print(f"Remaining balance is: {self.balance}")
        else:
            print("Insufficient Balance")
    def check_balance(self):
        print(f"Account Holder: {self.name}")
        print(f"Account Number: {self.acc_no}")
        print(f"Account Balance: {self.balance}")


# #Main program

accounts = {}

while True:
    print("1. Create Account")
    print("2. Deposit")
    print("3. Credit")
    print("4. Check Balance")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter name: ")
        acc_no = int(input("Enter account number: "))
        accounts[acc_no] = Bank(name, acc_no)

    elif choice in [2,3,4]:
        acc_no = int(input("Enter account number: "))
        cust = accounts.get(acc_no)

        if not cust:
            print("Account not found")
            continue

        if choice == 2:
            amt = int(input("Enter amount: "))
            cust.debit(amt)

        elif choice == 3:
            amt = int(input("Enter amount: "))
            cust.credit(amt)

        else:
            cust.check_balance()

    elif choice == 5:
        break
