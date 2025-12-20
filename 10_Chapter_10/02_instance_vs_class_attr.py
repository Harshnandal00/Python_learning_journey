class office:
    salary = "1000000"
    post = "Jr. Engineer" #This is the class attribute
    language = "python"
    
harsh = office()
harsh.language = "javascript"
print(harsh.language) #javascript is printed because instance 
# attribute is given priority instead of class... 