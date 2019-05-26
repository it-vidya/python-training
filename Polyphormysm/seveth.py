fo=open("mydata.txt","rb")
for line in fo:
    print(line.decode(),end="")
fo.close()
