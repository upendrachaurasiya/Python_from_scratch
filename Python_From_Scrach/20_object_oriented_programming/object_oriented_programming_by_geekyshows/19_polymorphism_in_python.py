# 3- method overloading
class MyClass:
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a*b
        else:
            s="provide atleast two numbers "
        return s

m=MyClass()
print(m.sum(12,12,12))
print(m.sum(15,10))
print(m.sum(12))


