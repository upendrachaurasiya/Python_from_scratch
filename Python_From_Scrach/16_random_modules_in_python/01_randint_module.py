import random
num=random.randint(1,10)# randint() function will return randomally number between 1 to 10
print(num)

num1=random.randrange(1,10) # randrange() function also return randomally number between 1 to 9 not 10

print(num1)

l=[5,55,555,5555]
c=random.choice(l) # choice() function is use for return randomally number of list,touple
print(c)