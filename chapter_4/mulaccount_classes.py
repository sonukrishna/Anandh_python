""" modeling multiple accounts using classes """


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

a=Bank_Account()
b=Bank_Account()
print 'account details of a:'
print a.deposit(100)
print a.deposit(150)
print a.withdraw(200)
print 'account details of b:'
print b.deposit(1000)
print b.withdraw(750)
