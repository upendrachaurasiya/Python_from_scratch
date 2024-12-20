#   Single Inheritance 

class A:
    def displayA(self):
        print("Class A method")

class B(A):
    def displayB(self):
        print("Class B method")

bb=B()
bb.displayA()
bb.displayB()