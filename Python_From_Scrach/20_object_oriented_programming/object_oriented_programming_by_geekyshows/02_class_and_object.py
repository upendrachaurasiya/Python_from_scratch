class Mobile:
    def __init__(self):
        self.model="realme X"
    def show(self):
        print("model:",self.model)

realme=Mobile()         # output=
realme.show()                      # realme X
realme.model="Realme C2"           
realme.show()                      # Realme C2
print()
redme=Mobile()                     
redme.show()                       # realme X
