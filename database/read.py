import pymysql
db = pymysql.connect("localhost","root","","test" )
#(url,uname,passwd,dbname)
cursor = db.cursor()
cursor.execute("Select * from user")
rows = cursor.fetchall()
print(rows)
db.close()
