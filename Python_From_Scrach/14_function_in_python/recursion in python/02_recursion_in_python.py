num=int(input("enter last term:"))
f0=0
f1=1
print(f0,f1,end=" ")
for i in range(2,num+1):
    f2=f0+f1
    print(f2,end=" ")
    f0=f1
    f1=f2
