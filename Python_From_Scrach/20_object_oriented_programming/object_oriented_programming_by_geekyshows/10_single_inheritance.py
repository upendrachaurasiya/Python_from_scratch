class Father:
    def __init__(self):
       print("Father class Constructor")
    def shows(self):
        print("father class instance Method")

class Son(Father):
    
    def disp(self):
        print("child class instance method")
       



S=Son()
S.disp()
S.shows()