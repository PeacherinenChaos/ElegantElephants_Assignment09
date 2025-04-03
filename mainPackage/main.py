#main.py
#Student Name: Annapoorna Nair
# email: nairap@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date: April 3, 2025
# Course #/Section: IS4010 Section 1
# Semester/Year: Spring 2025
# Brief Description of the assignment: We are working to access SQL server

# Brief Description of what this module does. This sets up the initial query stuff




from DatabasePackage.database import DatabaseManagement  
import pyodbc

dbm = DatabaseManagement()

conn = dbm.connect_to_database()

cursor = conn.cursor()  
cursor.execute('SELECT ProductID, [UPC-A ], Description, ManufacturerID, BrandID FROM tProduct')

total_enrollment = 0

for row in cursor:
    print(row)  
    print(row[0])  
    print(row[1]) 
    print(row[2])  
    print(row[3])  
    print(row[4]) 

Description = 'Sweet & Sour Chicken'
ProductID = 483
ManufacturerID = 39
BrandID = 65


