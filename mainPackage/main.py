#main.py
#Student Name: Annapoorna Nair
# email: nairap@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date: April 3, 2025
# Course #/Section: IS4010 Section 1
# Semester/Year: Spring 2025
# Brief Description of the assignment: We are working to access SQL server

# Brief Description of what this module does. This sets up the initial query stuff



from DatabasePackage.database import *

import pyodbc 

dbm = DatabaseManagement()

conn = dbm.connect_to_database()


cursor = dbm.submit_sql_to_server(conn, 'SELECT ProductID, [UPC-A ], Description, ManufacturerID, BrandID FROM tProduct')

total_enrollment = 0
# Step through all the rows in the results set
for row in cursor:
    print(row);     # All columns in the row
    print (row[1]); # Second column
    print (row[2]); # Third column
    print (row[3]); # Fourth column
    total_enrollment = total_enrollment + int(row[2])   # running sum of enrollments

