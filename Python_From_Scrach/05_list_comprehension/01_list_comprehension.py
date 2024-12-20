'''DEFINITION=List comprehension is a sort way to insert elemets in list by using single line code
        
        SYNTAX=  newlist_NAME = [expression for item in iterable if condition == True]'''


print()
l=[]

for i in range(1,11):
    l.append(i)

print(l)

#    By using list comprehension

print()
n=[m for m in range(1,11)]
print(n)


l1=[h for h in range(1,101) if h%2==0]  # this line will return even number between 1 to 100
print(l1)


a="hello"
s=[n for n in a]
print(s)

l=[i for i  in range(1,111) if i%5==0]
print(l)
