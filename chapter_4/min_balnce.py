"""model an account type where the account holder has to maintain a pre-determined minimum balance. """

class Bank_Account:
    def __init__(self):
        self.bal=0
    def deposit(self,amount):
        self.bal += amount
        print 'balance after deposit %d:'% amount,
        return self.bal
    def withdraw(self,amount):
        self.bal -= amount
        print 'balance remaining after withdraw %d:'% amount,
        return self.bal

class MinimumBalAccount(Bank_Account):
    def __init__(self,min_balance=500):
	Bank_Account.__init__(self)
	self.min_balance=min_balance
    def withdraw(self,amount):
	if self.bal-amount < self.min_balance:
	    print 'sorry,, may be next time'
	else:
	    Bank_Account.withdraw(self,amount)

a=MinimumBalAccount(Bank_Account)
b=Bank_Account()
print a.deposit(1000)
print a.withdraw(700)
