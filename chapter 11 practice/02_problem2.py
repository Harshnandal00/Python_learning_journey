class animals:
    pass

class pets(animals):
    pass

class dog(pets):
    
    @staticmethod
    def bark():
        print("Boww boww !!")
        
d = dog
d.bark()