# Multilevel Inheritence 

class GrandFather:
    def DisplayGF(self):
        print("GrandFather class Method")

class Father(GrandFather):
    def DisplayF(self):
        print("Father class Method")

class Son(Father):
    def DisplayS(self):
        print("Son calss method")



ss=Son()
ss.DisplayS()
ss.DisplayF()
ss.DisplayGF()