#pip install mysql-connector-python
# pip install pymysql
import mysql.connector
mydb = mysql.connector.connect(host="127.0.0.1", user="root", password="1GopiAmbi!")
cursor=mydb.cursor()
cursor.execute('create database if not exists placement_app')
print('Database created successfully')
cursor.close()
mydb.close()



