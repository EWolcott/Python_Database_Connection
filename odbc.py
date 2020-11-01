import pyodbc

##def listProducts(maxprice):
#    conn_str = (
#        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
#        r'DBQ=F:\\ethan\\ethan_school\\CS\\DB_MGT\\Northwind.accdb;'
#        )
#    cnxn = pyodbc.connect(conn_str)
#    crsr = cnxn.cursor()
#    sql = "SELECT C.Company, E.[Last Name] as LastName "
#    sql = sql + "FROM Customers C, Employees E, Orders O "
#    sql = sql + "WHERE E.ID=O.[Employee ID] AND C.ID=O.[Customer ID] AND "
#    sql = sql + "O.[Shipping Fee] < " + str(maxprice)
#    sql = sql + " ORDER BY O.[Shipping Fee]"

 #   rows = crsr.execute(sql)
#    for row in rows:
#        print(row.Company + ": " + row.LastName)

def priceIncrease():
    conn_str = (
        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
        r'DBQ=F:\\ethan\\ethan_school\\CS\\DB_MGT\\Northwind.accdb;'
        )
    cnxn = pyodbc.connect(conn_str)
    crsr = cnxn.cursor()
    sql = "SELECT [Product Name] as ProductName, ([List Price] * 1.10) as PriceIncrease "
    sql = sql + "FROM Products "

    rows = crsr.execute(sql)
    for row in rows:
        print(row.ProductName + ": " + str(row.PriceIncrease))

def targetLevel():
    conn_str = (
        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
        r'DBQ=F:\\ethan\\ethan_school\\CS\\DB_MGT\\Northwind.accdb;'
        )
    cnxn = pyodbc.connect(conn_str)
    crsr = cnxn.cursor()
    sql = "SELECT MAX([Target Level]) as MaxTL, MIN([Target Level]) as MinTL, AVG([Target Level]) as AvgTL "
    sql = sql + "FROM Products "

    rows = crsr.execute(sql)
    for row in rows:
        print("Max: " + str(row.MaxTL) + ", " + "Min: " + str(row.MinTL) + ", " + "Avg: " + str(row.AvgTL))

def discontinued():
    conn_str = (
        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
        r'DBQ=F:\\ethan\\ethan_school\\CS\\DB_MGT\\Northwind.accdb;'
        )
    cnxn = pyodbc.connect(conn_str)
    crsr = cnxn.cursor()
    sql = "SELECT COUNT(*) as NumDiscontinued "
    sql = sql + "FROM Products "
    sql = sql + "WHERE [Discontinued] = TRUE "

    rows = crsr.execute(sql)
    for row in rows:
        print(row)

def dried():
    conn_str = (
        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
        r'DBQ=F:\\ethan\\ethan_school\\CS\\DB_MGT\\Northwind.accdb;'
        )
    cnxn = pyodbc.connect(conn_str)
    crsr = cnxn.cursor()
    sql = "SELECT [Product Name] as ProductName "
    sql = sql + "FROM Products "
    sql = sql + "WHERE [Product Name] LIKE ('%dried%') "

    rows = crsr.execute(sql)
    for row in rows:
        print(row.ProductName)

def beverages():
    conn_str = (
        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
        r'DBQ=F:\\ethan\\ethan_school\\CS\\DB_MGT\\Northwind.accdb;'
        )
    cnxn = pyodbc.connect(conn_str)
    crsr = cnxn.cursor()
    sql = "SELECT [Product Name] as ProductName "
    sql = sql + "FROM Products "
    sql = sql + "WHERE Category = 'Beverages' AND Discontinued <> TRUE "

    rows = crsr.execute(sql)
    for row in rows:
        print(row.ProductName)

def shippers():
    conn_str = (
        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
        r'DBQ=F:\\ethan\\ethan_school\\CS\\DB_MGT\\Northwind.accdb;'
        )
    cnxn = pyodbc.connect(conn_str)
    crsr = cnxn.cursor()
    sql = "SELECT [Ship Name] as ShipName "
    sql = sql + "FROM Orders "
    sql = sql + "WHERE [Shipping Fee] > 100 "

    rows = crsr.execute(sql)
    for row in rows:
        print(row.ShipName)

def allEmployees():
    conn_str = (
        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
        r'DBQ=F:\\ethan\\ethan_school\\CS\\DB_MGT\\Northwind.accdb;'
        )
    cnxn = pyodbc.connect(conn_str)
    crsr = cnxn.cursor()
    sql = "SELECT [Last Name] as LastName, [First Name] as FirstName, [Job Title] as JobTitle "
    sql = sql + "FROM Employees "

    rows = crsr.execute(sql)
    for row in rows:
        print(row.LastName + ", " + row.FirstName + ": " + row.JobTitle)

def shipDates():
    conn_str = (
        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
        r'DBQ=F:\\ethan\\ethan_school\\CS\\DB_MGT\\Northwind.accdb;'
        )
    cnxn = pyodbc.connect(conn_str)
    crsr = cnxn.cursor()
    sql = "SELECT [Shipped Date] as ShippedDate, [Last Name] as LastName "
    sql = sql + "FROM Orders, Employees "
    sql = sql + "WHERE Orders.[Employee ID] = ID"

    rows = crsr.execute(sql)
    for row in rows:
        print(str(row.ShippedDate) + ": " + row.LastName)

def allProducts():
    conn_str = (
        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
        r'DBQ=F:\\ethan\\ethan_school\\CS\\DB_MGT\\Northwind.accdb;'
        )
    cnxn = pyodbc.connect(conn_str)
    crsr = cnxn.cursor()
    sql = "SELECT MAX([List Price]) as MaxLP, MIN([List Price]) as MinLP, AVG([List Price]) as AvgLP "
    sql = sql + "FROM Products "

    rows = crsr.execute(sql)
    for row in rows:
        print("Max: " + str(row.MaxLP) + ", " + "Min: " + str(row.MinLP) + ", " + "Avg: " + str(row.AvgLP))    

def allProductsGrouped():
    conn_str = (
        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
        r'DBQ=F:\\ethan\\ethan_school\\CS\\DB_MGT\\Northwind.accdb;'
        )
    cnxn = pyodbc.connect(conn_str)
    crsr = cnxn.cursor()
    sql = "SELECT Category, MAX([List Price]) as MaxLP, MIN([List Price]) as MinLP, AVG([List Price]) as AvgLP "
    sql = sql + "FROM Products "
    sql = sql + "GROUP BY [Category]"

    rows = crsr.execute(sql)
    for row in rows:
        print(row.Category + " - " + "Max: " + str(row.MaxLP) + ", " + "Min: " + str(row.MinLP) + ", " + "Avg: " + str(row.AvgLP))    


print (30 * '-')
print ("  EX_05 M A I N - M E N U")
print (30 * '-')
print ("1. 10% increase to list price of all products")
print ("2. Max, Min, and Avg Target Level of all products")
print ("3. How many products ae discontinued")
print ("4. All products containing the word 'dried'")
print ("5. All non-doscontinued beverages")
print ("6. Shippers with a shipping fee greater than 100")
print ("7. All employees and their job titles")
print ("8. Ship date for all orders and the employee assigned")
print ("9. Max, Min, and Avg price for all products")
print ("10. Max, Min, and Avg price for products by category")
print (30 * '-')
 
## Get input ###
choice = input('Enter your choice [1-10] : ')
 
### Convert string to int type ##
choice = int(choice)
 
### Take action as per selected menu-option ###
if choice == 1:
        priceIncrease()
elif choice == 2:
        targetLevel()
elif choice == 3:
        discontinued()
elif choice == 4:
        dried()
elif choice == 5:
        beverages()
elif choice == 6:
        shippers()
elif choice == 7:
        allEmployees()
elif choice == 8:
        shipDates()
elif choice == 9:
        allProducts()
elif choice == 10:
        allProductsGrouped()
else:    ## default ##
        print ("Invalid number. Try again...")



#if __name__ == "__main__":
 #listProducts(20.5)