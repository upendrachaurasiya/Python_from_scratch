l=[10,20,30,40,50]
print(l[0::])  # Return whole list same to same 


for i in range(len(l)):    # return list elements line by line 
    print(l[i])

print()

for i in l:
    print(i)   # return list elements line by line 

print(l[-1::-1])   # return reverse of list {[50, 40, 30, 20, 10]}

t=len(l)
for i in range(t-1,-1,-1):#  this line also return reverse of list line by line 
    print(l[i])