# constructor overriding in Inheritance 

class Father:
    def __init__(self):
        self.money=1000
        print("Father class constructor:")
    
    def showF(self):
        print("Father class instance Method",self.money)

class Son(Father):
    def __init__(self):
        self.money=2000
        print("Son class Constructor")

    def showS(self):
        print("Son class Instance Method",self.money)


s=Son()
print(s.money)
print()

s.showF()
s.showS()
print()

f=Father()
f.showF()
