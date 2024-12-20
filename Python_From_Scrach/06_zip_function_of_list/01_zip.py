# DEFINITION- zip is used to more than one list elements print using for loop

# zip is used when no. of elements are same of both list (if 1st list elements are 5 
#                                                        then second lists elments should be 5 )

l=[1,2,3,4,5]
l1=[11,22,33,44,55]

for a,b in zip(l,l1):
    print(a,b)

# without zip function use

print()
for i in range(len(l)):
    print(l[i],l1[i])