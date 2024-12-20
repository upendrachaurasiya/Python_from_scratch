class Father:
    def __init__(self):
        self.money=1000
       
    
    def showFather(self):
        print("Father class instance method")

    
class Son(Father):
    def showSon(self):
        print("Son class instance Method","money=",self.money)

S=Son()
S.showFather()
S.showSon()