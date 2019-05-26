import pymysql
#pymysql.install_as_MySQLdb()
db = pymysql.connect("localhost","root","","test" )
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print("Database version : %s"%data)
db.close()












'''
cursor.execute("SELECT * FROM sample")
rows= cursor.rowcount
results = cursor.fetchall()
   for row in results:
      fname = row[0]
      lname = row[1]
	  print('fname: {0}, lname: {1}'.format(fname,lname))
db.commit()
db.close()

'''
	




"""CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""

"""INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME)
         VALUES ('Mac', 'Mohan')"""
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 