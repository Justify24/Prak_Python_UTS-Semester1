import mysql.connector

#Koneksi dari database
dataBase = mysql.connector.connect(
    user  = 'root',
    host = 'localhost'
)
#menyiapkan objek kursor
cursorObject = dataBase.cursor()

#membuat database dengan nama "db_sales_V3922033"
cursorObject.execute("CREATE DATABASE db_sales_V3922033")