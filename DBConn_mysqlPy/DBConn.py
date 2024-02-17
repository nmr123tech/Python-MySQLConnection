import mysql.connector

db = mysql.connector.connect(
    database="kgs_mahi",
    host="localhost",
    user="root",
    password="NPRnlnr@123",
    port="3306"
)

my=db.cursor()

my.execute("select * from kgs_workday")

users=my.fetchall()

for user in users:
    print(user)

#Mysql connector -> Cursor -> Methods