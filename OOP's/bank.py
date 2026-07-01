class Bank:
    bankname = "SBI"
    ifsc = "SBIN0000123"
#Constructor
    def __init__(self, name, bal, mail):
        self.name=name
        self.bal=bal
        self.mail=mail
#Account Details
    def show_details(self):
        print("Bank Name :",Bank.bankname)
        print("IFSC Code  :",Bank.ifsc)
        print("Name :",self.name)
        print("Balance     :",self.bal)
        print("Email   :",self.mail)
# Check Balance
    def check_bal(self):
        print("\nAvailable Balance :", self.bal)
# Deposit Amount
    def deposit(self):
        amount = int(input("\nEnter Deposit Amount: "))
        self.bal += amount
        print( amount,"Deposited Successfully.")
        print("Updated Balance :", self.bal)
    def withdraw(self):
        amount=int(input("enter withdraw amount:"))
        if amount>self.bal:
            self.bal-=amount
            print("withdraw amount:",amount)
        else:
            print("insuff fund")
user1 = Bank("Ram", 10000, "ram@example.com")
user1.show_details()
user1.check_bal()
user1.deposit()
user1.withdraw()
user1.check_bal()
class Bank:
    bankname = "SBI"
    ifsc = "SBIN0000123"
#Constructor
    def __init__(self, name, bal, mail):
        self.name=name
        self.bal=bal
        self.mail=mail
#Account Details
    def show_details(self):
        print("Bank Name :",Bank.bankname)
        print("IFSC Code  :",Bank.ifsc)
        print("Name :",self.name)
        print("Balance     :",self.bal)
        print("Email   :",self.mail)
# Check Balance
    def check_bal(self):
        print("\nAvailable Balance :", self.bal)
# Deposit Amount
    def deposit(self):
        amount = int(input("\nEnter Deposit Amount: "))
        self.bal += amount
        print( amount,"Deposited Successfully.")
        print("Updated Balance :", self.bal)
    def withdraw(self):
        amount=int(input("enter withdraw amount:"))
        if amount>self.bal:
            self.bal-=amount
            print("withdraw amount:",amount)
        else:
            print("insuff fund")
user1 = Bank("Ram", 10000, "ram@example.com")
user1.show_details()
user1.check_bal()
user1.deposit()
user1.withdraw()
user1.check_bal()
print("================================")
user2=Bank("Sita",200000, "sita@example.com")

user2.show_details()
user2.check_bal()
user2.deposit()
user2.withdraw()
user2.check_bal()
print("================================")
if user1.bal>user2.bal:
    print("user1 has more blance")
else:
    print("user2 has more blance")
user1.show_details()
user2.show_details()


