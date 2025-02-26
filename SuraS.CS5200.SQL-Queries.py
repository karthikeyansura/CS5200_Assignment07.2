# Title: Query a Database with SQL in Python
# Author: Sai Karthikeyan, Sura
# Date: 02/25/2025

import sqlite3

# Step 1: Connect to the SQLite database
db_path = "OrdersDB.sqlitedb.db"
dbCon = sqlite3.connect(db_path)
cursor = dbCon.cursor()

# Step 2: Get the name, contact name, and country of all suppliers sorted by supplier name
print("\nSuppliers sorted by name:")
cursor.execute("""
    SELECT SupplierName, ContactName, Country 
    FROM Suppliers 
    ORDER BY SupplierName;
""")
for row in cursor.fetchall():
    print(row)

# Step 3: Get the total number of different products offered for sale by each supplier
print("\nTotal number of different products offered by each supplier:")
cursor.execute("""
    SELECT s.SupplierName, COUNT(p.ProductID) AS ProductCount 
    FROM Suppliers s
    LEFT JOIN Products p ON s.SupplierID = p.SupplierID 
    GROUP BY s.SupplierID
    ORDER BY s.SupplierName;
""")
for row in cursor.fetchall():
    print(row)

# Step 4: List countries with more than ten suppliers
print("\nCountries with more than 10 suppliers:")
cursor.execute("""
    SELECT Country, COUNT(SupplierID) AS SupplierCount 
    FROM Suppliers 
    GROUP BY Country 
    HAVING COUNT(SupplierID) > 10;
""")
for row in cursor.fetchall():
    print(row)

# Step 5: Close the connection
dbCon.close()
