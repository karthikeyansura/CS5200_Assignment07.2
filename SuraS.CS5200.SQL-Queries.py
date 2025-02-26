# Title: Query a Database with SQL in Python
# Author: Sai Karthikeyan, Sura
# Date: 02/25/2025

import sqlite3

# Function to connect to the SQLite database
def connect_to_database(db_path):
    dbCon = sqlite3.connect(db_path)
    cursor = dbCon.cursor()
    return dbCon, cursor


# Function to get the name, contact name, and country of all suppliers sorted by supplier name
def get_suppliers_sorted_by_name(cursor):
    print("\nSuppliers sorted by name:")
    cursor.execute("""
        SELECT SupplierName, ContactName, Country 
        FROM Suppliers 
        ORDER BY SupplierName;
    """)
    for row in cursor.fetchall():
        print(row)


# Function to get the total number of different products offered for sale by each supplier
def get_total_products_by_supplier(cursor):
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


# Function to list countries with more than ten suppliers
def get_countries_with_more_than_ten_suppliers(cursor):
    print("\nCountries with more than 10 suppliers:")
    cursor.execute("""
        SELECT Country, COUNT(SupplierID) AS SupplierCount 
        FROM Suppliers 
        GROUP BY Country 
        HAVING COUNT(SupplierID) > 10;
    """)
    rows = cursor.fetchall()
    
    if rows:  # Check if there are any rows
        for row in rows:
            print(row)
    else:
        print("No countries have more than 10 suppliers.")


# Main function
def main():
  
    # Step 1: Connect to the SQLite database
    db_path = "OrdersDB.sqlitedb.db"
    dbCon = sqlite3.connect(db_path)
    cursor = dbCon.cursor()

    # Step 2: Get the name, contact name, and country of all suppliers sorted by supplier name
    get_suppliers_sorted_by_name(cursor)
    
    # Step 3: Get the total number of different products offered for sale by each supplier
    get_total_products_by_supplier(cursor)
    
    # Step 4: List countries with more than ten suppliers
    get_countries_with_more_than_ten_suppliers(cursor)

    # Step 5: Close the connection
    dbCon.close()


# Run main function
if __name__ == "__main__":
    main()
