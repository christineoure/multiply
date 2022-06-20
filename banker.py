from datetime import datetime
class Bank:
    def __init__(self, account_number, account_name):
        self.account_number = account_number
        self.account_name = account_name
        self.balance=0
        self.deposits=[]
        self.withdrawals=[]
        self.transaction=[]
        self.time=datetime.now().strftime('%x')
        self.total=[]
        self.loan_balance = 0
        self.loan_repayment = 0
        self.transfers = 0
       


        

    def deposit (self, amount):
        self.balance+= amount
        return f"you have deposited this amount{amount} and this is your balance {self.balance}"


    def deposit (self, amount):
        if amount <=0:
            return f"Deposit amount should be more than zero"

        self.balance += amount
        self.deposits.append({"date":self.time, "amount":amount, "narration":"Deposits"})
         
        return f"You have deposited {amount}. Your new balance is {self.balance}",self.deposits


    def withdraw (self, amount):
        if amount>self.balance:
            return f"Your balance is {self.balance}. You cannot withdraw the {amount}"
        elif amount<0:
            return f"Amount must be greater than zero"
        else:
            self.transaciton_cost = 100
            self.balance-=amount + self.transaciton_cost
            self.withdrawals.append({"date":self.time, "amount":amount, "narration":"withrawals"})


            return f"You have withdrawn {amount}. Your balance is {self.balance}", self.withdrawals

    def deposits_statements(self):
        for x in self.deposits:
             print (x)

    def withdrawals_statements(self):
        for x in self.withdrawals:
            print (x)
    
    def current_balance(self):
        balance=self.balance
        return f"Your current balance is {balance}" 
     
    def full_statements(self):
        total =self.deposits + self.withdrawals
        for i in total:
            print(i)
            
    def borrow(self, amount):
        sum = 0
        for i in self.total:
            sum+=i["amount"]
        
        if len(self.deposits) <10:
            print("Deposits must be greater than 10")
        elif amount<100:
            print("the amount should be greater than 100")
        elif amount <= (sum//3):
            print(f"you are eligible for the loan and your balance is {amount}")

        elif self.balance == 0:
            print(f"You can't borrow. Your account balance is 0.")

        elif self.loan_balance > 0:
            print(f"You cannot borrow {amount} need to clear your previous loan first")
        else:
             self.loan_balance =(0.03*amount)+ amount
             return f" you have borrowed {amount} with an interest of {0.03*amount} and your balance is {self.loan_balance}"

    def loan_repayments(self, amount):
        loan_repayment = amount - self.loan_balance
        if amount < self.loan_balance:
            return f"You have paid {amount} and your outstanding balance is {loan_repayment}"
        
        elif amount == self.loan_balance:
            return "Congratlations! You have cleared your loan"
        
        else:
            amount > self.loan_balance
            return f"Congratlations! You have cleared your loan and our new balance is {loan_repayment}"


    def transfer(self,amount,Account2):
        if amount<=0:
            return "You cannot make a transfer"
        elif amount>=self.balance:
            return "You have insufficient balance. Please top up"
        else:
            self.balance-=amount
            Account2.balance += amount
            return f"You have transfered {amount} to {Account2} account with the name of {Account2.account_name}. Your new balance is {self.balance}"

