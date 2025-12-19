# f = open("file.txt")
# data = f.read()
# print(data)
# f.close()

# this same can be written as with statement

with open("file.txt") as f:
    data = f.read()
    print(data)
    