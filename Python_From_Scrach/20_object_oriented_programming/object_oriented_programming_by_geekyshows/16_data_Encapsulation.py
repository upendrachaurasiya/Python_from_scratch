'''definition---We can not access the variable or methods directly by using data Encapsulation 
                    Syntax---__var_name_or_Method_name()'''

class Demo:
    __name="Upendra"  # we cannot access this varible using object but we can use this variable in under 
                        #   consturctor or method
    def __init__(self):
        print(self.__name)      # calling private variable under constructor

    def __show(self):
        print("You can not access me using object because i am private variable")

    def disp(self):
        print(self.__name)
        self.__show()

d=Demo()
# print(d.__name)  this line throw error because __name is private variable
d.disp()