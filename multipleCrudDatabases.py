import MySQLdb
import sys
import os




tableCounter = 0

def callAppropriateCase(userInput):
    if userInput == 1:
        insertValuesInTable()
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

def getCreateTableCommand(listOfColumnNames, listOfColumnDataTypes, databaseName, tableName):
    global tableCounter
    try:
        while tableCounter < len(listOfColumnNames):
           commandForCreateTable  = ""
           lengthOfList = len(listOfColumnNames)
           for i in range(lengthOfList):
               if i == (lengthOfList - 1):
                  concatenatedString = str((listOfColumnNames[i] + " " + listOfColumnDataTypes[i]))
                  commandForCreateTable = commandForCreateTable + concatenatedString
                  tableCounter = tableCounter + 1

               else:
                  concatenatedString = str((listOfColumnNames[i] + " " + listOfColumnDataTypes[i] + ","))
                  commandForCreateTable = commandForCreateTable + concatenatedString
                  tableCounter = tableCounter + 1

           dbConnection = MySQLdb.connect("localhost","root","done@1234", databaseName )
           cursor = dbConnection.cursor()
           createTableCommand = "CREATE TABLE " + tableName  + "(" + str(commandForCreateTable) + ");"
           if tableCounter >= len(listOfColumnNames):
                 try:
                    cursor.execute(createTableCommand)
                    dbConnection.commit()
                    print("Table successfully created")
                 except:
                    print("Unable to create table")
                    dbConnection.close()
           else:
                 getCreateTableCommand(listOfColumnNames, listOfColumnDataTypes, databaseName, dbConnection)

    except IOError:
        print("Error in getCreateTableCommand")

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
         createTable(databaseName, "")
    else:
       sys.exit(0)

def createTable(databaseName, x):

    global tableCounter
    tableName = input("Enter the name of the table to be created")
    numberOfColumns = input("Enter the number of columns for the table")
    listOfColumnNames = []
    listOfColumnDataTypes = []
    numberOfColumns = int(numberOfColumns)
    for i in range(numberOfColumns):
        columnName = input("Enter column name")
        columnType = input("Enter column type")
        columnDataType = convertStringTypeToSQLType(columnType)
        listOfColumnNames.append(columnName)
        listOfColumnDataTypes.append(columnDataType)
    getCreateTableCommand(listOfColumnNames, listOfColumnDataTypes, databaseName, tableName)


def insertValuesInTable():
  databaseName = input("Enter the name of the database to be used")
  tableName = input("Enter the name of the table to be used")
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
    tableName = input("Enter the name of the table to be used")
    try:
        dbConnection = MySQLdb.connect("localhost","root","done@1234", databaseName)

    except:
        print("Connection to the database was not successful")
        return 0
    cursor = dbConnection.cursor()
    sqlCommand = "SELECT * FROM " + tableName

print("1.) Select Database/Table and insert")
print("2.) Read data")
print("3.) Create Database")
userChoice = int(input("Enter your choice"))
callAppropriateCase(userChoice)
