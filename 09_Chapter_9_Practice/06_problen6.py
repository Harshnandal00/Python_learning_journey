with open("log.txt" , "r") as file:
    data = file.read()
    if(("python") in data.lower()):
        print("log.txt contains the word python as a substring")
        
    else:
        print("the txt file doesn't contains the word python in it!")