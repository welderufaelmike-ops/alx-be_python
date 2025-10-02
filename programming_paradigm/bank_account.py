
class BankAccount:
    def __init__(self,initial_balance=0.0):
        self.account_balance=float(initial_balance)
    
    def deposit(self,amount):
        if amount >0:
            self.account_balance+=amount
            return True
        return False
    def withdraw(self, amount):
        if 0< amount <= self.account_balance:
            return True
        return False
    
    def get_balance(self):
        return self.__account_balance

    def display_balance(self):
        print(f"the current balance: ${self.account_balance=:.2f}")