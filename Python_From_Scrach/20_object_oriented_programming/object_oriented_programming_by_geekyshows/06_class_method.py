# Class Method With Parameter

class Mobile:
    fp="yes"
    @classmethod            # decorator
    def ShowModel(cls,r):     # class Method
        cls.RAM=r
        print("finger print=",cls.fp,"Ram=",cls.RAM)

realme=Mobile()
Mobile().ShowModel("4 GB")    # calling class method 


# class Mobile(object):
#     fp="yes"
    
#     @classmethod
#     def show(cls,r):
#         cls.ram=r
#         cls.fp="no"
#         print("ram=",cls.ram,",fingerprint=",cls.fp)
    
# realme=Mobile
# realme.show("4gb")
