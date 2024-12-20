l=[]
while True:
    a=int(input('''
        1   push
        2   pop
        3   peek
        4   display
        5   exit       =>'''))
    if a==1:
        b=input("Enter element :")
        l.append(b)
        print(l)
    
    elif a==2:
        if len(l)==0:
            print("Empty list")
        else:
            n=l.pop()
            print(n)
    
    elif a==3:
        if len(l)==0:
            print("Empty list")
        else:
            print(l[-1])
    
    elif a==4:
        print(l)
    
    elif a==5:
        break