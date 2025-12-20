class office:
    salary = "1000000"
    post = "Jr. Engineer" #This is the class attribute
    language = "python"
    
    def __init__(self, name, salary, post, language): # an type of dandar method which calls itself automatically whenever a object is formed.
        self.name = name
        self.salary = salary
        self.post = post
        self.language = language
        print("THis line will be called every time an object is formed because it is a dunder menthod which calls itself automatically whenever a object is called")
    
    def getinfo(self):
        print(f"This is the salary {self.salary}\nThis is the language {self.language}")
        
    @staticmethod
    def greetings():
        print("Good morning")
        

harsh = office("harsh", 1300000, "Senior engineer", "Javascript")
harsh.name = "harsh"
print(harsh.salary, harsh.post , harsh.language, harsh.name )

# rohan = office()