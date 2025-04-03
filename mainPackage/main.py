#main.py
#Student Name: Annapoorna Nair
# email: nairap@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date: April 3, 2025
# Course #/Section: IS4010 Section 1
# Semester/Year: Spring 2025
# Brief Description of the assignment: We are working to access SQL server

# Brief Description of what this module does. This sets up the initial query stuff


from PeytonPackage.peytonWork import get_manufacturer_name, get_brand_name
from DatabasePackage.database import DatabaseManagement  
import pyodbc

dbm = DatabaseManagement()
conn = dbm.connect_to_database()

if conn:
    Description = 'Sweet & Sour Chicken'
    ProductID = 483
    ManufacturerID = 39
    BrandID = 65

    manufacturer_name = get_manufacturer_name(conn, ManufacturerID)
    brand_name = get_brand_name(conn, BrandID)

    print(f"Description: {Description}")
    print(f"ProductID: {ProductID}")
    print(f"Manufacturer: {manufacturer_name}")
    print(f"Brand: {brand_name}")

    conn.close()
else:
    print("Database connection failed.")



