import MySQLdb
import sys
def write():
    try:
      dbConnection = MySQLdb.connect("localhost","root","done@1234","pythondatabase" )

    except:
      print("Connection to the database was not successful")
      return 0
    print("Connected")
    valueToBeInserted = int(input("Enter a value to be inserted into the database"))
    sqlCommand = "INSERT INTO PYTHONTABLE2(value) VALUES ('%d')" %(valueToBeInserted)
    cursor = dbConnection.cursor()
    cursor.execute(sqlCommand)
    dbConnection.commit()
    dbConnection.close()
    userInput = input("Enter your choice")
    switchStatement(int(userInput))

def read():
    try:
      dbConnection = MySQLdb.connect("localhost","root","done@1234","pythonDatabase" )
    except:
       print("Connection not successful")
       return 0
    cursor = dbConnection.cursor()
    sqlCommand = "SELECT * FROM PYTHONTABLE2"
    try:
      cursor.execute(sqlCommand)
      result = cursor.fetchall()
      print(result)
    except:
        print("Unable to fetch data from the database")
    dbConnection.close()
    userInput = input("Enteryour choice")
    switchStatement(int(userInput))

def update():
    try:
        dbConnection = MySQLdb.connect("localhost","root","done@1234","pythonDatabase" )
    except:
        print("Connection was not successful")
        return 0
    cursor = dbConnection.cursor()
    userId = int(input("Enter the id of the user whose details are to be updated"))
    valueToBeUpdated = int(input("Enter the value to be updated"))
    sqlCommand = "UPDATE PYTHONTABLE2 SET VALUE = '%d' WHERE id = '%d'" %(valueToBeUpdated,userId)
    cursor.execute(sqlCommand)
    dbConnection.commit()
    dbConnection.close()
    userInput = input("Enter your choice")
    switchStatement(int(userInput))

def delete():
    try:
        dbConnection = MySQLdb.connect("localhost","root","done@1234","pythonDatabase" )
    except:
        print("Connection was not successful")
        return 0
    cursor = dbConnection.cursor()
    userId = int(input("Enter the id of the user whose records are to be deleted"))
    sqlCommand = "DELETE FROM PYTHONTABLE2 WHERE id = '%d'" %(userId)
    cursor.execute(sqlCommand)
    dbConnection.commit()
    dbConnection.close()
    userInput = input("Enter your choice")
    switchStatement(int(userInput))


def switchStatement(userInput):
       if userInput == 1:
         write()
       elif userInput == 2:
         read()
       elif userInput == 3:
         update()
       elif userInput == 4:
         delete()
       elif userInput == 5:
           sys.exit(0)
       else:
        print("Invalid User Input")

print("1.) Write Data")
print("2.) Read Data")
print("3.) Update Data")
print("4.) Delete Data")
print("5. Exit")

userInput = input("Enter your choice")

switchStatement(int(userInput))
