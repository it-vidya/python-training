import pymysql
db = pymysql.connect("localhost","root","","test" )
#(url,uname,passwd,dbname)
cursor = db.cursor()
fname=input("Enter fname: ")
lname=input("Enter lname: ")
query="Insert into USER VALUES('{}','{}')"
cursor.execute(query.format(fname,lname))
db.commit()
db.close()
