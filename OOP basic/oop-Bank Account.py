class Account:
    def __init__(self, name, amount=0):
        self.name = name
        self.amount = amount
    def __str__(self):
        return f"Account owner: {self.name}\nAccount balance: ${self.amount}"
 
    def deposit(self, a):
        self.amount += a
        return "Deposit Accepted"
    def withdraw(self, b):
        if self.amount < b:
            return "Funds Unavailable!"
        else:
            self.amount = self.amount - b
            return "Withdrawal Accepted"
            

acct1 = Account('Jose', 100)

#Example
print(acct1)
print(acct1.name)
print(acct1.deposit(50))
print(acct1.amount)
print(acct1.withdraw(500))
print(acct1.withdraw(50))
print(acct1.amount)