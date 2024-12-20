class Gun:              # outer class 
    def __init__(self):
        self.gun="AK 47"
        self.magzine="57 rounds"
        self.n=self.Names()         # creating inner class object
    def show(self):
        print("gun=",self.gun)
        print("rounds=",self.magzine)

    class Names:                    # second class under main class 
        def __init__(self):
            self.name="Army"
            self.work="firing Bullets"
        
        def display(self):
            print("name=",self.name)
            print("work=",self.work)

g=Gun()
g.show()
print()

g.n.display()           # calling second class main class object

#  or

print()
nn=Gun().Names()
nn.display()