#database.py
#Student Name: Annapoorna Nair
# email: nairap@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date: April 3, 2025
# Course #/Section: IS4010 Section 1
# Semester/Year: Spring 2025
# Brief Description of the assignment: We are working to access SQL server

# This sets up the database and the connection

import pyodbc 


class DatabaseManagement:
    def connect_to_database(self):
        '''
        Connect to our sql server instance
        @return the connection object
        '''
        try:
            conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
                          'Database=GroceryStoreSimulator;'
                          'uid=IS4010Login;'
                          'pwd=P@ssword2;')
        except:
            
            print("Unable to connect to database")
            return None
        return conn;
    """def submit_sql_to_server(self, conn, sql_statement):
        '''
        submit a sql statement to our sql server
        @ oaram conn connection object: the connection object
        @param sql_statement String: the sql to submit
        @return the pyodbc cursor object that contains query results
        '''
        cursor = conn.cursor()
        cursor.execute('SELECT ProductID, [UPC-A ], Description, ManufacturerID, BrandID FROM tProduct')    # Submit a query to the SQL Server instance and store the results in the cursor object
        return cursor"""


