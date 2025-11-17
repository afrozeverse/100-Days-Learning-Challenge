import mysql.connector
try:
    mydb=mysql.connector.connect(
        host='localhost',user='root',password='Afroze352##7',database='db2'
    )
    if mydb.is_connected():
        print("Connected to mysql database")
        cursor=mydb.cursor()
        cursor.execute("show databases")
        for x in cursor:
            print(x)
    else:
        print("Not connected to mysql database")
except mysql.connector.Error as e:
    print("Error ",e)
finally:
    if mydb.is_connected():
        cursor.close()