#!/usr/bin/python3
import MySQLdb

db = MySQLdb.connect(host="localhost", port=3306,db="hbtn_0e_0_usa")
cursor = db.cursor()
cursor.execute("SELECT * FROM ANTIOO")

result = cursor.fetchall()
for row in result:
        print(row)


cursor.close()
db.close()

