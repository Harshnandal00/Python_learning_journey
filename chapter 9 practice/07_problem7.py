
with open("log.txt" , "r") as file:
    lines = file.readlines()
    
lineno = 1
for line in lines:
    if("python" in line):
        print(f"python is present in the file , line no: {lineno}")
        break
    lineno += 1

else:
    print("Python is not present in the file")