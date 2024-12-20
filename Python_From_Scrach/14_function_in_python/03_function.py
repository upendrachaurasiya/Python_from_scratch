# function with no argument and with return

def eveodd():
    a=int(input("enter a number:"))
    return a

x=eveodd()
if x%2==0:
    print(x,"is even")
else:
    print(x,"is odd")
    