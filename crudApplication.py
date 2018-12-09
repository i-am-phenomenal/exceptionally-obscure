import os

def createFile():
    fileToBeCreated = input("Enter the name of the file")
    fileExtension = ".txt"
    fileName = fileToBeCreated + fileExtension
    textOfTheFile = input("Enter text to be added in the file")
    file = open(fileName, "w+")
    file.write(textOfTheFile)
    file.close()
    userInput = input("Enter your choice")
    switchStatement(int(userInput))
    
def readFile():
    fileToBeCreated = input("Enter the name of the file")
    fileExtension = ".txt"
    fileName = fileToBeCreated + fileExtension
    file = open(fileName, "r")
    fileData = file.read()
    print(fileData)
    file.close()
    userInput = input("Enter your choice")
    switchStatement(int(userInput))
        
def updateFile():
    fileToBeEdited = input("Enter the name of the file")
    fileExtension = ".txt"
    fileName = fileToBeEdited + fileExtension
    textOfTheFile = input("Enter text to be added in the file")
    file = open(fileName, "a")
    file.write(textOfTheFile)
    file.close()
    userInput = input("Enter your choice")
    switchStatement(int(userInput))
    
def deleteFile():
    fileToBeDeleted = input("Enter the name of the file")
    fileExtension = ".txt"
    fileName = fileToBeDeleted + fileExtension
    os.remove(fileName)
    userInput = input("Enter your choice")
    switchStatement(int(userInput))
    

def switchStatement(userInput):
 while userInput < 5:
  if userInput == 1:
    createFile()
  elif userInput == 2:
    readFile()
  elif userInput == 3:
    updateFile()
  elif userInput == 4:
    deleteFile()
  elif userInput == 5:
    break
  else: print("Invalid Input") 
     
    
print("1.) Create File")
print("2.) Read File")
print("3.) Update File")
print("4.) Delete File")
print("5. Exit")

    
userInput = input("Enter your choice")

switchStatement(int(userInput))
 