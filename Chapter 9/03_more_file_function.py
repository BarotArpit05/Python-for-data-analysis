f=open("Chapter 9/file.txt")
#lines=f.readlines()
#print(lines)
#print(type(lines))
line=f.readline()
while(line!=""):
    print(line)
    line=f.readline()
f.close()