with open("10_problemfile.txt") as f:
    content = f.read()
    
if(content != ""):
    with open("10_problemfile.txt" , "w") as f:
        f.write("")
        
else:
    print("It is already empty , so i can't empty an empty file")