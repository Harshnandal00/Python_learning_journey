class office:
    salary = "1000000"
    post = "Jr. Engineer" #This is the class attribute
    language = "python"
    
harsh = office()
harsh.name = "harsh" #This is the instaqnce(object) attribute
print(harsh.name , harsh.salary , harsh.post, harsh.language)
robin = office()
robin.name = "robinhood"
print(robin.name , robin.salary , robin. post , robin.language)

# Here name is the object attribute and the salary , post ,
# language are class attribute because they directly belong to 
# the class~ office
