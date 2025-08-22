

class BankAccount: 
    def __init__(self,owner,balance): 
        self.owner = owner
        self.__balance = balance

    def show_balance(self): 
        print(f"balance : {self.__balance}")

class Cal(BankAccount):

    def __init__(self,owner,balance,isActive): 
        super().__init__(owner,balance) 

        self.isActive = isActive

    def account_status(self):
        print(f"owner name : {self.owner}")
        print(f"account balance : {self.show_balance()}")
        print(f"account status : {self.isActive}")

    


acc = Cal("am1tt",2100,"yes")

acc.show_balance()

acc.account_status()

## Implemented getter here , for show_balance()

