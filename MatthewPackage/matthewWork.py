# File Name : matthewWork.py
# Student Name: Matthew Boutros
# email:  boutromw@mail.uc.edu
# Assignment Number: Assignment 09 
# Due Date:   4/3/25
# Course #/Section:   IS 4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment: Work with SQL Server and Python to analyze grocery data.
# Brief Description of what this module does: Fetches product data, selects a random product, and calculates quantity sold.
# Citations:
# Anything else that's relevant: N/A

import pyodbc
import random

def get_all_products(conn):
    """
    Retrieve all product rows from the database
    @param conn: pyodbc connection object
    @return list of product tuples
    """
    cursor = conn.cursor()
    cursor.execute("SELECT ProductID, [UPC-A ], Description, ManufacturerID, BrandID FROM tProduct")
    return cursor.fetchall()

def get_random_product(products):
    """
    Select a random product from a list
    @param products: list of product tuples
    @return tuple of selected product
    """
    return random.choice(products)

def get_items_sold(conn, product_id):
    """
    Retrieve the number of items sold for the given product
    @param conn: pyodbc connection object
    @param product_id: ID of the product
    @return integer count of items sold
    """
    cursor = conn.cursor()
    query = f"""
    SELECT TOP (100) PERCENT SUM(dbo.tTransactionDetail.QtyOfProduct) AS NumberOfItemsSold
    FROM dbo.tTransactionDetail 
    INNER JOIN dbo.tTransaction 
    ON dbo.tTransactionDetail.TransactionID = dbo.tTransaction.TransactionID 
    WHERE (dbo.tTransaction.TransactionTypeID = 1) AND (dbo.tTransactionDetail.ProductID = {product_id})
    """
    cursor.execute(query)
    result = cursor.fetchone()
    return result[0] if result and result[0] is not None else 0

