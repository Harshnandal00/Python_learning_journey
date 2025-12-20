class complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i
        
    def __add__(self, c2):
        return (self.r + c2.r , self.i + c2.i)
    
    def __mul__(self, c2):
        return (
        (self.r * c2.r) - (self.i * c2.i),  
        (self.r * c2.i) + (self.i * c2.r))
    
    
    def __str__(self):
        return (f"{self.r} + {self.i}i")
    
a = complex(1,2)
b = complex(3,4)
print(a+b)
print(a*b)