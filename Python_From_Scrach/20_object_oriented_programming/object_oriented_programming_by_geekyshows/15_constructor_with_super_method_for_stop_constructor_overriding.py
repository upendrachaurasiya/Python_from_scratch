# If we want to access both constructor in inheritance than we have to use super()Method

class Father:               # parent class constructor
    def __init__(self,m):
        self.money=m
        print("Father class constructor:",self.money)
    
    def showF(self):
        print("Father class instance Method",self.money)

class Son(Father):          # son class constructor 
    def __init__(self,r):
        self.moneys=r
        print("Son class Constructor",self.moneys)
        super().__init__(1000)      # calling parents class constructor

    def showS(self):
        print("Son class Instance Method",self.moneys)


s=Son(2000)
s.showS()
s.showF()
