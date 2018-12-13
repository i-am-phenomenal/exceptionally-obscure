import MySQLdb
import sys
class Customer:
     def __init__(self, customerId, customerAddress):
         self.customerName = customerName
         self.customerAddress = customerAddress

def callAppropriateCase(userInput):
    if userInput == 1:
        useDatabaseAndInsert()
    elif userInput == 2:
        readData()
    elif userInput == 3:
         createDatabase()
    elif userInput < 3:
        sys.exit(0)
    else:
      print("Invalid Input")

def convertStringTypeToSQLType(columnType):
    if columnType == "int" or "Int" or "INT":
        return "INT"
    elif columnType == "string" or "String" or "STRING":
        return "VARCHAR"
    elif columnType == "float" or "Float" or "FLOAT":
        return "FLOAT"
    else:
        print("Invalid Input")


def createDatabase():
    databaseName = input("Enter the name of the database to be created")
    dbConnection = MySQLdb.connect("localhost","root","done@1234", "customers" )
    cursor = dbConnection.cursor()
    sqlCommand = "CREATE DATABASE " + databaseName
    try:
      cursor.execute(sqlCommand)
      dbConnection.commit()
    except:
        print("Unable to create a database")
    dbConnection.close()
    createTableOrNot = input("Would you like to create a table within this database ? (Y/N)")
    if createTableOrNot == "Y" or "y":
         createTable(databaseName)
    else:
       sys.exit(0)

def createTable(databaseName):
    tableName = input("Enter the name of the table to be created")
    numberOfColumns = input("Enter the number of columns for the table")
    listOfColumnNames = []
    listOfColumnDataTypes = []
    numberOfColumns = int(numberOfColumns, 10)
    for i in range(numberOfColumns):
        columnName = input("Enter column name")
        columnType = input("Enter column type")
        columnDataType = convertStringTypeToSQLType(columnType)
        listOfColumnNames.append(columnName)
        listOfColumnDataTypes.append(columnDataType)
    dbConnection = MySQLdb.connect("localhost","root","done@1234", databaseName )
    cursor = dbConnection.cursor()
    createTableCommand = "CREATE TABLE " + tableName + "()"
    cursor.execute(createTableCommand)
    dbConnection.commit()
    dbConnection.close()

def useDatabaseAndInsert():
  databaseName = input("Enter the name of the database to be used")
  tableName = input("Enter the nme of the table to be used")
  try:
      dbConnection = MySQLdb.connect("localhost","root","done@1234", databaseName)

  except:
      print("Connection to the database was not successful")
      return 0
  print("Connected")
  customerName = input("Enter the name of the customer")
  customerAddress = input("Enter the address of the customer")
  sqlCommandToInsertData = "INSERT INTO " + tableName + " (customerName, customerAddress) VALUES ('%s', '%s')" %(customerName, customerAddress)
  cursor = dbConnection.cursor()
  cursor.execute(sqlCommandToInsertData)
  dbConnection.commit()
  dbConnection.close()
  userInput = int(input("Enter your choice"))
  callAppropriateCase(userInput)

def readData():
    databaseName = input("Enter the name of the database to be used")
    tableName = input("Enter the nme of the table to be used")
    try:
        dbConnection = MySQLdb.connect("localhost","root","done@1234", databaseName)

    except:
        print("Connection to the database was not successful")
        return 0
    cursor = dbConnection.cursor()
    sqlCommand = "SELECT * FROM " + tableName
    # try:
    #  customerInstance = Customers()


print("1.) Select Database/Table and insert")
print("2.) Read data")
print("3.) Create Database")
userChoice = int(input("Enter your choice"))
callAppropriateCase(userChoice)
