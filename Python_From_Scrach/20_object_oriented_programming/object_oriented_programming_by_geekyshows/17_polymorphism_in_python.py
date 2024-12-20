# 1- Duck typing 

class Duck:
    def walk(self):
        print("Thapak Thapak Thapak")

class Horse:
    def walk(self):
        print("Tabdak Tabdak Tabdak")

def myfunction(obj):
    obj.walk()


d=Duck()
myfunction(d)

h=Horse()
myfunction(h)



