# 5- Operator Overloading

class A:
    def __init__(self,x):
        self.x=x
    def __add__(self,other):
        return self.x + other.y

class B:
    def __init__(self,y):
        self.y=y

a=A(12)
b=B(12)
print(a+b)      # A.__add__(a,b)

# 10+20                 int.__add__(self,other)
# 'upendra'+'kumar'     str.__add__(self,other)