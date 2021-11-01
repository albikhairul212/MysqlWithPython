import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
)

cursor = mydb.cursor()
cursor.execute("CREATE DATABASE kampus")

print("Database KAMPUS sukses dibuat")
