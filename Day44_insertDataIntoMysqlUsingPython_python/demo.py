import mysql.connector

def fetchEmployee(cursor):
    cursor.execute("select * from employee")
    return list(cursor)

def insertEmployee(cursor):
    pass

def main():
    try:
        mydb=mysql.connector.connect(host='localhost',user='root',password='1234',database='employee')
        if mydb.is_connected():
            print("Connected to mySql database")
            cursor=mydb.cursor()

            employeeList=fetchEmployee(cursor)
            for record in employeeList:
                print(record)
        else:
            print("Database not connected")
    except mysql.connector.Error as e:
        print("ERROR: ",e)