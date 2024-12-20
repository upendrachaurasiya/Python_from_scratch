# Multiple Inheritance 

class A:
    def displayA(self):
        print("A class method")

class B:
    def displayB(self):
        print("B class method")

class C(A,B):
    def display(self):
        print("C class method")
cc=C()
cc.display()
cc.displayA()
cc.displayB()
