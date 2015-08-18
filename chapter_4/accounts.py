"""making a single account """

bal=0
def deposit(amount):
    global bal
    bal += amount
    return bal
def withdraw(amount):
    global bal
    bal -= amount
    return bal
print deposit(5000)
print deposit(1000)
print withdraw(1000)
