class number:
    def __init__(self, n):
        self.n = n
        
    def __add__(self, num):# it is a dunder method which can be used to overlap the operators like addition , substraction, division, len, floordiv, truediv, str..
        return self.n + num.n
        
n = number(1)
m = number(2)
print(n + m)