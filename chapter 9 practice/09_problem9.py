with open("file1.txt") as f:
    content1 = f.read()
    
with open("file2.txt") as f:
    content2 = f.read()
    
if(content1 == content2):
    print("file1.txt and file2.txt have the same content...")   
    
else:
    print("these files don't have the same content")