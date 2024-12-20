class demo:
    def getdata(self):
        self.a=int(input("enter a number that you want to know square:"))
        
    
    def putdata(self):
        print(f"squrare={self.a*self.a}")

    def add_data(self,x,y):
        print(x+y)

d=demo()
d.getdata()
d.putdata()
d.add_data(10, 10)