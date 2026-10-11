class ATM():
    def __init__(self,name,pin,balance):
        self.name=name
        self.__pin=pin
        self._balance=balance
    def check_balance(self):
        print("here's your current balance:",self._balance)
    def verify_pin(self,pin):
        return pin==self.__pin
    def deposit(self,amount):
        self.amount=amount
        if amount>0:
            self._balance+=amount
            print("amount deposited successfully",self._balance)
    def withdrawl(self,amount):
        if amount<=self._balance:
            self._balance-=amount
            print("withdrawl successfull",self._balance)

a=ATM("mikey",2003,7000)
print("welcome to ATM")
pin=int(input("enter your ATM pin:"))
if a.verify_pin(pin):
    while True:
        print("\n ATM menu")
        print("1.check balance")
        print("2.cash deposit")
        print("3.amount withdrawl")
        print("4.exit")

        choice=int(input("enter your choice(1-4):"))
        
        if choice == 1:
            a.check_balance()
        elif choice == 2:
            amount = int(input("Enter amount to deposit: "))
            a.deposit(amount)
        elif choice == 3:
            amount = int(input("Enter amount to withdrawl: "))
            a.withdrawl(amount)
        elif choice == 4:
            print("Thank you for using our ATM")
            break
        else:
            print("Invalid choice")
else:
    print("Incorrect pin, please try again")
                
