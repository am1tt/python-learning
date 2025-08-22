


class BankAccount: 
    def __init__(self,owner,balance): 
        self.owner = owner
        self.__balance = balance
    
    def show_balance(self): 
        print(f"balance : {self.__balance}")


acc = BankAccount("am1tt",2000)


print(acc.owner) ## this is public 

acc.show_balance() ## still prints due to python is not trully private unlike java and c++ 

print(acc.__balance) ## this is private but will cause an error 
