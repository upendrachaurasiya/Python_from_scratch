# write a program to find factorial of any number using recursion

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)

num=int(input("enter number that you want to know factorial:"))
f=fact(num)
print(f)