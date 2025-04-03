#main.py
#Student Name: Annapoorna Nair
# email: nairap@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date: April 3, 2025
# Course #/Section: IS4010 Section 1
# Semester/Year: Spring 2025
# Brief Description of the assignment: We are working to access SQL server
#Citation: mainly based it over the in class assignment we did that one day

# Brief Description of what this module does. This sets up the initial query stuff

from MatthewPackage import Matthew
from PeytonPackage.Peyton import get_manufacturer_name, get_brand_name
from DatabasePackage.database import DatabaseManagement  
import pyodbc

dbm = DatabaseManagement()
conn = dbm.connect_to_database()

if conn:
    products = Matthew.get_all_products(conn)
    selected_product = Matthew.get_random_product(products)

    ProductID = selected_product[0]
    Description = selected_product[2]
    ManufacturerID = selected_product[3]
    BrandID = selected_product[4]

    manufacturer_name = get_manufacturer_name(conn, ManufacturerID)
    brand_name = get_brand_name(conn, BrandID)
    items_sold = Matthew.get_items_sold(conn, ProductID)

    print(f"The product '{Description}', manufactured by '{manufacturer_name}', under the brand '{brand_name}', sold {items_sold} units.")
    conn.close()
else:
    print("Database connection failed.")



