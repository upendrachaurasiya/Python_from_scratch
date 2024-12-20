# Instance Method- Accessor Method/ Getter Method

class Mobile:
    def __init__(self):
        self.model="Ralme X"        # Instance Method
    
    def SetModel(self):
        self.model="Realme C2"      # Mutator Method
        return self.model

# Befor setter 
Realme=Mobile()
print(Realme.model)
# After satter 
print()
m=Realme.SetModel()
print(m)
print(Realme.model)

