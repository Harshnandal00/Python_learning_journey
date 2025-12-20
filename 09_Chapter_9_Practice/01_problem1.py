f = open("poems.txt")

data = f.read()

if("twinkle" in data ):
    print("the word twinkle is present in the data")
else:
    print("the word twinkle is not present in the data")

f.close()