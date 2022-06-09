class Bank:
    def __init__(self, account_number, account_name):
        self.account_number = account_number
        self.account_name = account_name
        self.balance=0
        self.deposits=[]
        self.withdrawals=[]

        

    def deposit (self, amount):
        self.balance+= amount
        return f"you have deposited this amount{amount} and this is your balance {self.balance}"


    def deposit (self, amount):
        if amount <=0:
            return f"Deposit amount should be more than zero"

        self.balance += amount
        self.deposits.append(amount) 
        print(self.deposits)
        return f"You have deposited {amount}. Your new balance is {self.balance}"

    def withdraw (self, amount):
        if amount>self.balance:
            return f"Your balance is {self.balance}. You cannot withdraw the {amount}"
        elif amount<0:
            return f"Amount must be greater than zero"
        else:
            self.balance-=amount
            self.withdrawals.append(amount)
            return f"You have withdrawn {amount}. Your balance is {self.balance}", self.withdrawals

    def deposits_statements():
        print(*self.deposits,sep="/n")

    def withdrawals_statements():
        print(*self.withdrawals,sep="/n")
        
        
        
        