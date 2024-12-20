# 4-  Method overriding 
# Note----Method overriding always use in Inheritance concept


class Father:
    
    def show(self,a,b):
        print("addition=",a+b)



class Son(Father):
    
    def show(self,a,b):
        print("multiplication=",a*b)
        super().show(11,11)        # this line for print father class show method 

S=Son()
S.show(100, 10)



