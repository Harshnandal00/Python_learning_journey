
with open("this.txt" , "r") as f:
    data = f.read()
    
with open("copyofthis.txt", "w") as f:
    f.write(data)