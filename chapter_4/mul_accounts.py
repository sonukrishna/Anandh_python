""" if we want to model multiple accounts,what we do??? """


def make_account():
    return {'balance':0}
def deposit(account,amount):
    account['balance'] += amount
    print 'balance after deposit %d:'% amount,
    return account['balance']
def withdraw(account,amount):
    account['balance'] -= amount
    print 'balance remaining after withdraw %d:'% amount,
    return account['balance']


a=make_account()
b=make_account()
c=make_account()
print 'account details of a:',
print deposit(a,100)
print deposit(a,250)
print 'account details of c:',
print deposit(c,5000)
print withdraw(c,2000)
print 'account details of b:',
print deposit(b,200)
print deposit(b,300)
