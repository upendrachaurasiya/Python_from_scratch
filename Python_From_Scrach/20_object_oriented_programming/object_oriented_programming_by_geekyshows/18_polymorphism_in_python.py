#  2- strong typing     syntax=  hasattr(object,attribute)#  1- Duck typing 

class Duck:
    def walk(self):
        print("Thapak Thapak Thapak")

class Horse:
    def walk(self):
        print("Tabdak Tabdak Tabdak")

class Cat:
    def talk(self):
        print("meaw meaw meaw")



def myfunction(obj):
    if hasattr(obj,"walk"):
        obj.walk()
    if hasattr(obj, "talk"):
        obj.talk()


d=Duck()
myfunction(d)

h=Horse()
myfunction(h)

c=Cat()
myfunction(c)