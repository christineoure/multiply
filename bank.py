class Bank:
    def __init__(self, account_number, account_name, account_type, pin, balance):
        self.account_number = account_number
        self.account_name = account_name
        self.account_type = account_type
        self.pin = pin
        self.balance = balance

    def deposit (self, amount):
        currentbalance = amount + self.balance
        return currentbalance
        
    def withdraw (self, amount):
        currentbalance1 = amount - self.balance
        return currentbalance1
        