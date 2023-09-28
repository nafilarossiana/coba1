import sqlite3

# Connect to a SQLite database (it will create the database file if it doesn't exist)
connection = sqlite3.connect("deteksi.db")

# Create a cursor object to execute SQL commands
cursor = connection.cursor()

# Create a table
cursor.executescript("""
    CREATE TABLE IF NOT EXISTS deteksi (
        id_kendaraan INTEGER PRIMARY KEY,
        status TEXT,
        lokasi TEXT, 
        waktu_lintas TEXT
    );
    CREATE TABLE IF NOT EXISTS analisiswaktu (
        id_analisis INTEGER PRIMARY KEY,
        waktu TEXT,
        sesi TEXT, 
        jumlah_kendaraan INTEGER, 
        status TEXT
    ); 
    CREATE TABLE IF NOT EXISTS analisishari (
        id_analisis INTEGER PRIMARY KEY,
        hari TEXT,
        jumlah_kendaraan TEXT, 
        status TEXT
    );                 
""")

# Insert data into the table
cursor.execute("INSERT INTO deteksi (id_kendaraan, status, lokasi, waktu_lintas) VALUES (?, ?, ?, ?)", (1, "Masuk", "Gerbang depan", "01:10"))
cursor.execute("INSERT INTO analisiswaktu (id_analisis, waktu, sesi, jumlah_kendaraan, status) VALUES (?, ?, ?, ?, ?)", (1, "09:00", "Pagi", 2, "Keluar"))
cursor.execute("INSERT INTO analisishari (id_analisis, hari, jumlah_kendaraan, status) VALUES (?, ?, ?, ?)", (1, "Senin", 2, "Keluar"))

# Commit the changes
connection.commit()

# Retrieve and print data from the table
cursor.execute("SELECT * FROM deteksi")
deteksi = cursor.fetchall()
cursor.execute("SELECT * FROM analisiswaktu")
analisiswaktu = cursor.fetchall()
cursor.execute("SELECT * FROM analisishari")
analisishari = cursor.fetchall()

for user in deteksi:
    print(f"ID Kendaraan: {user[0]}, Status: {user[1]}, Lokasi: {user[2]}, Waktu Lintas: {user[3]}")
for user in analisiswaktu:
    print(f"ID Analisis: {user[0]}, Waktu: {user[1]}, Sesi: {user[2]}, Waktu: {user[3]}, Jumlah Kendaraan: {user[4]},Status: {user[5]} ")
for user in analisishari:
    print(f"ID Analisis: {user[0]}, Hari: {user[1]}, Jumlah Kendaraan: {user[2]}, Status: {user[3]}")

# Close the connection
connection.close()