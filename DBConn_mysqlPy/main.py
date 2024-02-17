import mysql.connector
db=mysql.connector.connect(
    database='kgs_mahi',
    host='localhost',
    user='root',
    password='NPRnlnr@123',
    port='3306'

)
#Cursor class instance is created & used to execute the SQL statements
myc=db.cursor()
#Creating table
#myc.execute("CREATE TABLE kgs_WORKDAY(dept VARCHAR(100),emp_count varchar(100))")
#selecting table values
myc.execute("SELECT * from kgs_workday")

users= myc.fetchall()

for user in users:
    print(user)


