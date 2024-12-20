class GrandFather:
    def showG(self):
        print('grandFather class instance method ')

class Father(GrandFather):
    def showF(self):
        print("Father class instance Method ")

class Son(Father):
    def showS(self):
        print("Son class instance method ")

S=Son()
S.showG()
S.showF()
S.showS()

