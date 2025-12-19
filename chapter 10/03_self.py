class office:
    salary = "1000000"
    post = "Jr. Engineer" #This is the class attribute
    language = "python"
    
    def getinfo(self):
        print(f"This is the salary {self.salary}\nThis is the language {self.language}")
    @staticmethod
    def greetings():
        print("Good morning")
harsh = office()
harsh.language = "javascript"#javascript is printed because instance 
# attribute is given priority instead of class...
print(harsh.language)
harsh.greetings()
harsh.getinfo()
