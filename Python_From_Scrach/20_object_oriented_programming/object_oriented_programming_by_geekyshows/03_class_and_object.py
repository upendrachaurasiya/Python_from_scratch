class Mobile:
    def __init__(self,m):
        self.model=m
    
    def show(self,p):
        self.price=p
        print("model:",self.model,",price:",self.price)

M=Mobile("realme C2")
M.show(10000)   # model: realme C2 ,price: 10000

M.prices=100
M.show(M.prices) # model: realme C2 ,price: 100

