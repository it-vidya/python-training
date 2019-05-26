fo=open("mydata.txt","r")
data =fo.readline()#first line
print(data)
data =fo.readline()#second line
print(data)
data =fo.readline()#third line
print(data)
fo.close()
#if file does not  exist "r" errors out.
