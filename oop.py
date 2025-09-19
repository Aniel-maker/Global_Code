class Account:
    def __init__(self, owner:str, balance = 0):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, amount: float):
        self.balance = amount

    def withdraw(self, amount: float):
        if amount >= self.balance:
            print("You are poor!!!!!!!!!")
        else:
            self.balance -= amount

    def get_balance(self):
        return self.balance 
    
account1 = Account("Philipa", 1000000)
account2 = Account("Dan", 50)