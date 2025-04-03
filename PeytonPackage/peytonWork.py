# File Name : peytonWork.py
# Student Name: Peyton Bock
# email:  bockps@mail.uc.edu
# Assignment Number: Assignment 09 
# Due Date:   4/3/25
# Course #/Section:   4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  Running SQL in python
# Brief Description of what this module does. Learn to runSQL in Python within a online database
# Citations: 
# https://www.w3schools.com/python/python_mysql_select.asp

# Anything else that's relevant: N/A

import pyodbc

def get_manufacturer_name(conn, manufacturer_id):
    """
    Submit a SQL statement to our SQL server
    @param conn connection object: the connection object
    @param manufacturer_id Integer: the ID of the manufacturer to look up
    @return String: the name of the manufacturer, or None if not found
    """
    cursor = conn.cursor()
    query = f"SELECT Manufacturer FROM tManufacturer WHERE ManufacturerID = {manufacturer_id}"
    cursor.execute(query)
    result = cursor.fetchone()
    return result[0] if result else None

def get_brand_name(conn, brand_id):
    """
    Submit a SQL statement to our SQL server
    @param conn connection object: the connection object
    @param brand_id Integer: the ID of the brand to look up
    @return String: the name of the brand, or None if not found
    """
    cursor = conn.cursor()
    query = f"SELECT Brand FROM tBrand WHERE BrandID = {brand_id}"
    cursor.execute(query)
    result = cursor.fetchone()
    return result[0] if result else None

