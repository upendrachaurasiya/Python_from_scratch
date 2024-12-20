l=[]
while True:
    a=int(input('''
        1   Push Elements
        2   Pop First Element
        3   Front Element
        4   Last Element
        5   Display Stack
        6   Exit        :-->>'''))
    
    if a==1:
        n=input("Enter value of queue :->")
        l.append(n)
    elif a==2:
        if len(l)==0:
            print("Empty queue")
        else:
            del l[0]
            print(l)
    elif a==3:
        if len(l)==0:
            print("Empty queue")
        else:
            print("First Queue value",l[0])
    elif a==4:
        if len(l)==0:
            print("Empty queue")
        else:
            print("Last Queue element ",l[-1])
    elif a==5:
        print(l)
    elif a==6:
        break
    else:
        print("Invalid Operation....")