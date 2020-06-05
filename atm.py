# Simple ATM system program
# class for customer information
class CustomerInfo:
    def __init__(self, cname,cid,balance):
        self.cname = cname
        self.cid = cid
        self.balance = balance

# class for transactions of customer
class Transaction(CustomerInfo):

    def __init__(self,cname,cid,balance):
        super().__init__(cname,cid,balance)

    def displaycustinof(self):
        print("Customer Name:- {} \n Customer Current balance:- {}".format(self.cname, self.balance))

    def depobal(self,damount):
        print("Total balance after deposit:- {}".format(damount + self.balance))
        self.balance=self.balance+damount

    def withbal(self,wamount):
        print("Total balance after withdraw:- {}".format(self.balance-wamount))
        self.balance = self.balance - wamount

def pincheck(pin):
    if pin==1234:
        print("Wait,We are proceeding..!")
    else:
        print("Sorry you have entered wrong pin,Try again..!")

# default balance
balance=50000
print("Welcome to ATM")
pin = int(input("Please enter your pin:"))
pincheck(pin)
t = Transaction("abhishek", pin, balance)
# To run the loop infinite times
while(True):
    print(" 1. Current Balance \n 2. Deposit Money \n 3. Withdraw Money \n 4. Exit.")
    no=int(input("Enter your choice number\n"))
    if no==1:
        t.displaycustinof()
    elif no==2:
        damount=int(input("Enter the deposite amount:"))
        t.depobal(damount)
    elif no==3:
        withbal=int(input("Enter the withdraw amount"))
        if withbal<balance:
            t.withbal(withbal)
        else:
            print("Sorry,You don't have sufficient amount to withdraw.")
    else:
        exit()