class Teacher:
    no_of_teachers=23
    
    def show(self):
        print("teacher class instance method")

class Servant:
    no_of_servant=5
    def disp(self):
        print("Servent class instance method ")

class Priciple(Teacher,Servant):
    def showdata(self):
        print("principle class instance method")


p=Priciple()
p.show()
p.disp()
p.showdata()

print()
t=Teacher()
print(t.no_of_teachers)