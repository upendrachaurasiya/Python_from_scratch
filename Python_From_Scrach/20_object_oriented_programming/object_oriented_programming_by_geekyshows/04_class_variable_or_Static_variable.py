class Mobile:
    fp="yes"                # class variable
    def __init__(self):
        self.model="Realme X"
    def Show_model(self):
        print(self.model)

    @classmethod        # Class Method
    def is_fp(cls):
        print("finger print=",cls.fp )         # Accessing class variable inside class method

realme=Mobile()
realme.Show_model()
Mobile.is_fp()

        

class Mobile:
    fp = "yes"
    def __init__(self):
        self.model = "Oppo A15s"
    def show(self):
        print(self.model)
        print("finger print =",self.fp)
        
        
        
m = Mobile()
m.show()
    
    