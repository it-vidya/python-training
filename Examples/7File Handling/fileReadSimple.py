fo = open("my.txt", "rb")
'''
data=fo.read()
print(data)

for line in fo:
		print(line)
		'''
		
		
fo.seek(-10,2)
print(fo.read())
print(fo.tell())
fo.close()
		

