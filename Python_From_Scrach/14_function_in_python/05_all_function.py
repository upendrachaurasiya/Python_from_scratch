# simple function
def eveodd():
    a=int(input("Enter a number :"))
    if a%2==0:
        print(a,"is even")
    else:
        print(a,"is odd")

eveodd()

# function with argument and no return

def eveodd(a):
    if a%2==0:
        print(a,"is even")
    else:
        print(a,"is odd")

b=int(input("Enter a number :"))
eveodd(b)

#function with no argument and with return

def eveodd():
    a=int(input("Enter a number:"))
    return a
x=eveodd()
if x%2==0:
    print(x,"is even")
else:
    print(x,"is odd")


# functio with argument and with return
def eveodd(a):
    return a
b=int(input("Enter a number :"))
x=eveodd(b)
if x%2==0:
    print(x,' is even')
else:
    print(x,'is odd')