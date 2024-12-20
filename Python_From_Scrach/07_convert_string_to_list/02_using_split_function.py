# DEFINITION:-split is used to store multiple string in a list from string
# NOTE--split function is work from space when user give space then split convert in list by indexing

a="welcome to upendra's show"
l=[]
l=a.split()
print(l)

#for multiple line entry in list
print()
l1=[]
for i in range (4):
    n=input("enter the value of "+str(i)+":")
    l1.append(n)

print(l1)