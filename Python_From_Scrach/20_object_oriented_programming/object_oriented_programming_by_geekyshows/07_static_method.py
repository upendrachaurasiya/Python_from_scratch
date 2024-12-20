class Mobile:
    @staticmethod
    def ShowModel():
        model="realme X"
        print("mobile Model:",model)

realme=Mobile()
Mobile.ShowModel()



class RedmiMobile:
    fp="yes"
    @staticmethod
    def show(n,m,p):
        name=n
        model=m
        price=p
        
        print("name=",name,",model=",model,",price=",price,",fingerprint=",RedmiMobile.fp)


redmi=RedmiMobile()
RedmiMobile.show("redmi","5g",10000)
        