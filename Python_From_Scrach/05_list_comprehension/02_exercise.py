l1=["ram","shyam","Mohan","Krishna","Kiran","Kailash","Kumar"]
print(l1)
l2=[]
for i in l1:
    if "K" in i:
        l2.append(i)

print(l2)

# with comprehention we will do this task in a single line of code
print()
l3=["ram","shyam","Mohan","Krishna","Kiran","Kailash","Kumar"]
print(l3)

l4=[x for x in l3 if "K" in x]
print(l4)