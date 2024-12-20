class Mobile:
    def __init__(self,n,p):
        self.name=n
        self.price=p

    def show(self):
        print("model=",self.name)
        print("price=",self.price)

class User:
    @staticmethod
    def display(s):
        print("model=",s.name)
        print("price=",s.price)
        s.show()

realme=Mobile("reamlme", 20000)
realme.show()
print()

User.display(realme)        # Accessing Mobile Class members 
