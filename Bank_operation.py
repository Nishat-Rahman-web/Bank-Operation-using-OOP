#Bank Operation using OOP
class Bank:
    bankname = "Mutual Trust Bank"
    branch = "Kaliganj,Gazipur"
#create account
    def __init__(self, username, pin, address):
        self.username = username
        self.pin = pin
        self.address = address
        self.balance = 0.0 #set account balannce to 0.0
        print(f'Hello {self.username} Congratulations! your account created successfully.')
    
#deposit
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f'{amount} diposited successfully. Your account balance is {self.balance}')
#withdraw
    def withdraw(self, amount):
        if amount < self.balance:
            self.balance = self.balance - amount
            print(f'{amount} withdraws successfully.')
        else:
            print("Insufficient Fund")
#ministatement
    def ministatement(self):
        print(f'Your account balance is {self.balance}')    

print(f'Welcome to {Bank.bankname}, {Bank.branch}')
print("********Account Creation********")
#collect user data for account creation
username = input("Enter your user name : ")   
pin = input("Enter your pin : ")
address = input("Enter your address : ")

B = Bank(username, pin, address) #object creation based on user provided data

while True:
    print("Please select any option : ")
    print("1. Deposite : ")
    print("2. Withdraw : ")
    print("3. Ministatement : ")
    print("4. Stop : ")
    option = int(input(""))

    if option == 1:
        amount = float(input("Enter deposited amount :"))
        B.deposit(amount)
    if option == 2:
        amount = float(input("Enter withdraw amount :"))
        B.withdraw(amount)
    if option == 3:
        B.ministatement()
    if option == 4:
        print("Thanks for using Mutual Trust Bank...")
        break