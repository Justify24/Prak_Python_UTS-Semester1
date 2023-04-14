import mysql.connector

dataBase= mysql.connector.connect(
    user  = 'root',
    host = 'localhost',
    database = 'db_sales_V3922033'
)

cursorObject = dataBase.cursor()

#membuat tabel database sesuai dengan ketentuan yang ada
studentRecord = """CREATE TABLE data_stok_barang (
                    id_Barang VARCHAR(10) PRIMARY KEY,
                    nama_barang VARCHAR(20),
                    harga_barang FLOAT,
                    stok_awal INT,
                    barang_masuk INT,
                    Barang_Keluar INT,
                    Stok_Akhir INT
                    )"""

cursorObject.execute(studentRecord)

#Disconect dari server
dataBase.close()