#class SampleProblems:
#    def __init__(self):
#        return None
#        
#    def getter(self):
#        data = input("enter the data")
#        return data
#        
#    def setter(self, data):
#        self.data = data
#        return self
#    
#    
#classObject = SampleProblems()
#value = classObject.getter()        
#classObject.setter(value)
#print(classObject.data)
#
#def multiplesOf7():
#    for iterator in range(2000, 3200):
#        if (iterator % 7 == 0) and not (iterator % 5 == 0):
#            print(iterator,",", end = " ")
#        else:
#            pass
#        
#def upperCase():
#    userInput = input("Enter the Sentence")
#    print(userInput.upper())
#    
#def firstLetterCaps():
#    userInput = input("Enter the Sentence")
#    dummyString = ""
#    for alphabet in range(1, len(userInput) - 2):
#        print(userInput[alphabet])
#        str = dummyString + userInput[alphabet]
##        print(str)
#        if userInput[alphabet] == " ":
#            userInput = userInput[alphabet + 1].upper()
#            str = dummyString + userInput
##    print(str)
#
#def printWords():
#    userInput = input("Enter the Sentence")
#    word = ""
#    wordArray = []
#    for alphabet in userInput: #range(0, len(userInput)):
#        if alphabet == " ":
#            wordArray.append(word)
#            slicedString = u 
#            userInput.replace(word, "")
#            print("22222222", userInput)
#            pass
#        else:
#            word += alphabet
#    print(wordArray)
#    
#
#def numbersWithEvenDigits():
#    for number in range(1000, 3000):
#        for alphabet in userInput:
#            unitsDigit = int(number % 10)
#            tensDigit = int(int(number % 100) / 10)
#            hundredsDigit = int(int(number / 100) % 10)
#            thousandsDigit = int(number / 1000)
#            if (unitsDigit % 2 == 0) and (tensDigit % 2 == 0) and (hundredsDigit % 2 == 0) and (thousandsDigit % 2 == 0):
#                 print(number)
#            else:
#                 pass
#
#def countDigitsAndLetters():
#    userInput = input("Enter the Sentence")
#    letters = 0
#    digits = 0
#    for element in userInput:
#        if element.isdigit():
#            digits += 1
#        if element.isalpha():
#            letters += 1
#        else:
#            pass
#    print("Letters =", letters)
#    print("Digits = ", digits)
#    
#
#def countUpperAndLowerCase():
#    userInput = input("Enter the Sentence")
#    lowerCase = 0
#    upperCase = 0
#    for alphabet in userInput:
#        if alphabet.islower():
#            lowerCase += 1
#        elif alphabet.isupper():
#            upperCase += 1
#        else:
#            pass
#    print("Upper Case", upperCase)
#    print("Lower Case", lowerCase)
#    
#def calculateValue():
#    #a + aa + aaa... 
#    digit = (input("enter the digit"))
#    twoDigits = int(digit + digit)
#    threeDigits = int(digit + digit + digit)
#    fourDigits = int(digit + digit + digit + digit)
#    sum = int(digit) + twoDigits + threeDigits + fourDigits
#    print(sum)
#    
##calculateValue()
##countUpperAndLowerCase()
##countDigitsAndLetters()
##numbersWithEvenDigits()            
##printWords()
##firstLetterCaps()
##upperCase()
##multiplesOf7()
## Work on removing duplicate words
#
#class Tree:
#    def __init__(self, data):
#        self.data = data
#        self.left = None
#        self.right = None
#        
#    def insert(self, data):
#        if data > self.left.data:
#            if self.right is None:
#                self.right.data = data
#            else:
#                self.right.insert(data)
#        elif data < self.head.data:
#            if self.left is None:
#                self.left.data = data
#            else:
#                self.left.insert(data)
#                
#        else:
#            self.head.data = data
#            
#    def printTree(self):
#        temp = self.head
#        if self.left:
#            self.left.printTree()
#        print(self.data)
#        
#        if self.right:
#            print(self.right.data)
#            
#root = Tree(10)
#root.insert(20)
#root.insert(2)
#root.insert(12)
#root.insert(7)
#root.insert(30)
#root.insert(50)
#root.insert(1)  
#root.printTree()
#  
##                
#def getFilteredList(element):
#    global listOfDigits
#    count = listOfDigits.count(element)
#    if count > 1: 
#        listOfDigits.remove(element)
#    else: 
#         pass
#
#listOfDigits = [1,2,3,4,5,5,5,6,7,8,9,1, 3, 2]
#
#for ele in listOfDigits: 
#     getFilteredList(ele)
#        
#print(listOfDigits)

#
#def checkForMinLength(password):
#    global isValid
#    if len(password) < 6 or len(password) > 12:
#        isValid = False
#    else:
#        isValid = True
#
#def checkForSpecialCharacters(password): 
#    for char in password:
#        if char == '$' or char == '#' or char == '@':
#            checkForMinLength(password)
#
#def checkIfUpperCase(password):
#    for char in password: 
#        if char.isupper():
#            checkForSpecialCharacters(password)
#
#def checkIfNumeric(password): 
#    for char in password:
#        if char.isnumeric():
#            checkIfUpperCase(password)
#        
#
#def checkIfPasswordIsValid(password): 
#    for char in password: 
#        if char.isalpha(): 
#            checkIfNumeric(password)
#        
#isValid = False
#
#password = input("Enter the password")
#    
#checkIfPasswordIsValid(password)
#print(isValid)



#
#currentPosition = [0,0]
#userChoice = 'y'
#
#def calculatePosition(inputPosition): 
#    global currentPosition
#    seperatedString = inputPosition.split(' ')
#    direction = seperatedString[0]
#    value = int(seperatedString[1])
#    if direction == 'UP' or direction == 'up':
#        currentPosition[1] = value
#    elif direction == 'DOWN' or direction == 'down':
#        currentPosition[1] = (0 - value)
#    elif direction == 'LEFT' or direction == 'left':
#        currentPosition[0] = (0 - value)
#    elif direction == 'RIGHT' or direction == 'right':
#        currentPosition[0] = value
#        
#    print(currentPosition)
#    return currentPosition
#        
#def getCommand(userChoice):
#    global currentPosition
#    if userChoice == 'y' or userChoice == 'Y':
#        inputPosition = input("enter the position: ")
#        calculatePosition(inputPosition)
##        print("+++  ",currentPosition)
#        userChoice = input("Do you want to add more {Y/N} ")
#        getCommand(userChoice)
#    else: 
#        print(currentPosition)
#        
#getCommand(userChoice)


#def getUpdatedFirstNumber(firstNumber, secondNumber):
#    if firstNumber >= secondNumber:
#        return (firstNumber + (firstNumber - secondNumber))
#    elif secondNumber >= firstNumber:
#        return (firstNumber + (secondNumber - firstNumber))
#    
#def getUpdatedSecondNumber(firstNumber, secondNumber):
#    if secondNumber >= firstNumber:
#        return (secondNumber - (secondNumber - firstNumber))
#    elif firstNumber >= secondNumber:
#        return (secondNumber - (firstNumber - secondNumber))
#
#
#firstNumber = int(input("Enter first number"))
#secondNumber = int(input("Enter second number"))
#newFirstNumber = getUpdatedFirstNumber(firstNumber, secondNumber)
#newSecondNumber = getUpdatedSecondNumber(firstNumber, secondNumber)
#
#print(newFirstNumber)
#print(newSecondNumber)




#list = [10,20,30,40,50,60,70,80,90,100]
#sum = 0
#filteredList = filter(lambda element: not (list.index(element) % 2 == 0), list)
#for ele in filteredList:
#    sum = sum + ele
#    
#print(sum)

#list = [10,20,30,40,50,60,70,80,90,100]
#n = int(input("Enter the value of n"))
#elementAtIndex = list[n]
#elementIndex = list.index(elementAtIndex)
#subList = filter(lambda element: list.index(element) < elementIndex, list)
#for ele in subList:
#    print(ele)

#
#import MySQLdb 
#
#def createFile():
#    nameOfFile = input("Enter the name of file")
#    fileName = nameOfFile + ".txtag"
#    fileData = input("enter the data to writen in file")
#    fileConnection = open(fileName, "w")
#    fileConnection.write(fileData)
#    fileConnection.close()
#    userChoice = int(input("Enter choice"))
#    switchStatement(userChoice)
#    
#def readFile():
#    nameOfFile = input("Enter the name of the file")
#    fileName = nameOfFile + ".txt"
#    try: 
#        fileConnection = open(fileName, "r")
#        fileContents = fileConnecton.read()
#        print(fileContents)
#        fileConnection.close()
#    except IOerror:
#        print("Unable to open file")
#        
#def updateFile():
#    nameOfFile = input("Enter the name of the file")
#    fileName = nameOfFile + ".txt"
#    
#def updateFile():
#    nameOfFile = input("Enter the name of the file")
#    fileName = nameOfFile + ".txt"
#    try:
#        fileConnection = open(fileName, "r")
#        fileData = fileConnection.read()
#        print("This is the file data     => ", fileData)
#        fileConnection.close()
#        updatedFileData = input("Enter updated data")
#        fileConnection = open(fileName, "a+")
#        fileConnection.write(updatedFileData)
#        fileConnection.close()
#    except IOError:
#        print("unable to update file")
#    
#        
#def switchStatement(userChoice):
#    if userChoice == 1:
#        createFile()
#    elif userChoice == 2:
#        readFile()
#    elif userChoice == 3:
#        updateFile()
#        
#        
#print("1.) Create File")
#print("2.) Read File")
#print("3.) Update File")
#userChoice = int(input("Enter choice"))
#switchStatement(userChoice)


#class C(object):
#    dummyName = "Dummy Name"
#    
#
#
#class A(object):
#    name = 'Aditya'
#    
#    def changeValue(self, newValue):
#        self.value = newValue
#
#class B(A, C):
#    anotherName = 'Another name'
#    
#object = B()
#print(object.dummyName)




#class Node:
#    def __init__(self, data):
#        self.data = data
#        self.next = None
#        
#class LinkedList:
#    def __init__(self):
#        self.head = None
#        
#    def insertElement(self,valueToBeInserted):
##        print(valueToBeInserted)
#        newNode = Node(valueToBeInserted)
#        if self.head is None:
#            self.head = newNode
#            return
#        else:
#            lastNode = self.head
#            while lastNode.next:
#                lastNode = lastNode.next
#            lastNode.next = newNode
#            
#    def printList(self):
#        temp = self.head
#        while(temp):
#            print(temp.data)
#            temp = temp.next
#
#userInput = input("Enter the number")
#number = list(userInput)
#wholeNumber  = int(userInput)
#updatedNumber = wholeNumber + 1
#numberString = list(str(updatedNumber))
#firstDigit = int(numberString[0])
#secondDigit = int(numberString[1])
#thirdDigit = int(numberString[2])
#fourthDigit = int(numberString[3])
#headNode = LinkedList()
#headNode.insertElement(firstDigit)
#headNode.insertElement(secondDigit)
#headNode.insertElement(thirdDigit)
#headNode.insertElement(fourthDigit)
#
#headNode.printList()

##
#class Node:
#    def __init__(self, data):
#        self.data = data
#        self.next = None
#        self.nodeCount = 0
#        
#        
#class LinkedList:
#    def __init__(self):
#        self.head = None
#    
#    def insertIntoLinkedList(self, nodeValue):
#        newNode = Node(nodeValue)
#        if self.head == None:
#            self.head = newNode
#            return 
#        else:
#            lastNode = self.head
#            while lastNode.next:
#                lastNode = lastNode.next
#            lastNode.next = newNode
#                    
#    def printList(self):
#        temp = self.head
#        while(temp):
#            print(temp.data)
#            temp = temp.next
#            
#    def deleteNode(self, nodeValue):
#        if self.head is None:
#            print("Node does not exist")
#            return
#        elif self.head.data == nodeValue:
#            self.head = self.head.next
#            return
#            
#        else:
#            lastNode = self.head
#            while lastNode.next:
#                if lastNode.next.data == nodeValue:
#                    lastNode.next = lastNode.next.next
#                    return
#                else:
#                    lastNode = lastNode.next
#                    
#    def dummy(self, listLength):
#        counter = 0
#        middle = int(listLength / 2)
#        if self.head is None:
#            print("Length is 0")
#        else:
#            lastNode = self.head
#            while lastNode:
#                if counter == middle:
#                    print(lastNode.data)
#                    return
#                else:
#                    counter = counter + 1
#                    lastNode = lastNode.next
#    
#            
#                    
#    def findLength(self):
#        length = 0
#        if self.head is None:
#            print("0")
#        else:
#            lastNode = self.head
#            while lastNode:
#                length = length + 1
#                lastNode = lastNode.next
#                
#        self.dummy(length)
#                    
#                    
#    def updateNode(self, updatedValue, valueToBeUpdated):
#        if self.head is None:
#            self.head = Node(updatedValue)
#            return
#        elif self.head.data == valueToBeUpdated:
#            self.head.data = updatedValue
#        else:
#            lastNode = self.head
#            while lastNode:
#                if lastNode.data  == valueToBeUpdated:
#                    lastNode.data = updatedValue
#                    return
#                elif lastNode.next is None:
#                    lastNode.data == updatedValue
#                    return 
#                else:
#                    lastNode = lastNode.next
#                    
#    def detectLoop(self):
#        traversedNodes = []
#        if self.head is None:
#            print("Empty List")
#            return
#        else:
#            lastNode = self.head
#            while lastNode:
#                if lastNode.next.data in traversedNodes:
#                    print("Loop Detected at   ", lastNode.data)
#                    self.removeLoop(lastNode.data)
#                    return
#                else:
#                    traversedNodes.append(lastNode.data)
#                    lastNode = lastNode.next
#            print("No loop detected")    
#            
#    def removeLoop(self, loopNode):
#        if self.head is None:
#            return
#        else:
#            lastNode = self.head
#            while lastNode:
#                if lastNode.data == loopNode:
#                    lastNode.next = None
#                    print("Loop removed")
#                    return
#                else:
#                    lastNode = lastNode.next
#            
#    def makeLoop(self):
#        if self.head is None:
#            print("Empty Link list")
#            return 
#        else:
#            lastNode = self.head
#            while lastNode.next:
#                   lastNode = lastNode.next
#            lastNode.next = self.head
#            
#    def findTotalLength(self):
#        length = 0
#        if self.head is None:
#            return
#        else:
#            lastNode = self.head
#            while lastNode:
#                if lastNode.next is None:
#                    self.findNthNode((length + 1))
#                    return
#                else:                    
#                    length = length + 1
#                    lastNode = lastNode.next
#            
#    def findNthNode(self, length):
#        print("+++++",length)
#        n = (length - 3)
#        counter = 0
#        if self.head is None:
#            print("Empty Link list")
#            return
#        else:
#            lastNode = self.head
#            while lastNode:
#                if counter == (n - 1):
#                    print("Node found at position", lastNode.data)
#                    return
#                elif n == 0:
#                    print("Illegal value of n")
#                    return
#                else:
#                    counter = counter + 1
#                    lastNode = lastNode.next
#                    
#    def reverseLinkList(self):
#        if self.head is None:
#            print("Empty List")
#            return
#        elif self.head.next is None:
#            print(self.head.data)
#            return
#        else:
#            lastNode = self.head
#            while lastNode.next.next:
#                lastNode = lastNode.next
#            
#            if lastNode.next.next is None:
#                print(lastNode.next.data)
##                print(lastNode.data)
#                lastNode.next = None
#                self.reverseLinkList()
#        
#    def shiftLinkedList(self):
#        headNode = self.head
#        if self.head is None:
#            return
#        else:
#            lastNode = self.head
#            while lastNode:
#                if lastNode.next is None:
#                    self.head = lastNode
#                    self.head.next = headNode
#                else:
#                    lastNode = lastNode.next
#    
#headNode = LinkedList()
#headNode.insertIntoLinkedList(10)
#headNode.insertIntoLinkedList(20)
#headNode.insertIntoLinkedList(30)
#headNode.insertIntoLinkedList(40)
#headNode.insertIntoLinkedList(50)
#headNode.insertIntoLinkedList(60)
##headNode.findNthNode(1)
##headNode.findTotalLength()
##headNode.deleteNode(20)
##headNode.updateNode(35, 50)
##headNode.printList()
##headNode.findLength()
##headNode.makeLoop()
##headNode.detectLoop()
##headNode.printList()
##headNode.reverseLinkList()
#headNode.shiftLinkedList()
#headNode.printList()


#from bs4 import BeautifulSoup
#import requests
#import time
#import urllib
#
##url = 'http://web.mta.info/developers/turnstile.html'
##response = requests.get(url)
#print("alsidaskdh")


#series = [0, 1]
#n = int(input("Enter the value of n"))
#for iter in range(0, (n - 1)):
#    elementToBeAdded = series[iter] + series[iter + 1]
#    series.append(elementToBeAdded)
#    
#print(series)

#number = int(input("Enter the number"))
#power = int(input("Enter the power tobe calculated"))
#answer = number
#for iter in range(1, (power)):
#    answer = answer * number
#    mm
#print(answer)

#def checkFirstAndLastBracket(brackets, firstBracket):
#    if firstBracket == brackets[len(brackets) - 1]:
#        return True
#    else:
#         return False
#        
#def checkBalancing(brackets):
#    
#
#def checkBrackets(brackets):
#    if not (len(brackets) % 2 == 0):
#        print("Unbalanced")
#        return
#    else:
#         firstBracket = brackets[0]
#        if checkFirstAndLastBracket(brackets, firstBracket):
#            checkBalancing(brackets)
#        else:
#            print("Unbalanced")
#            return
#
#
#
#checkBrackets(brackets)

#def getCurrentCounterPart(bracket):
#    if bracket == "{":
#        return "}"
#    elif bracket == "}":
#        return "{"
#    elif bracket == "(":
#        return ")"
#    elif bracket == ")":
#        return "("
#    elif bracket == "[":
#        return "]"
#    elif bracket == "]":
#        return "["
#
#def checkBalancing(stack):
#    if not(len(stack) == 0):
#        global stack
#        currentBracket = stack.pop(0)
#        currentCounterPart = getCurrentCounterPart(currentBracket)
#        stack.remove(currentCounterPart)
#        checkBalancing()
#    else: 
#        return
#
#def checkBrackets(brackets):
#    global stack
#    if not (len(brackets) % 2 == 0):
#        print("Unbalanced")
#        return
#    else:
#         firstBracket = brackets[0]
#            checkBalancing(stack)
#        else:
#            print("Unbalanced")
#            return
#
#
#userInput = input("Enter the brackets")
#brackets= []
#for bracket in userInput:
#    brackets.append(bracket)
#
#stack = bracskets
#    
#checkBrackets(brackets)


#from iterator in range(0, len(links)):
#    tag

#csvFile = pd.read_csv("legislators.csv", encoding = "ISO-8859-1", na_values= [])
#
#updatedFile = csvFile.fillna(" ")
#
#
#
#senatorsWithTwitter = []
#for iter in updatedFile.index: 
#    data = updatedFile["twitter_id"][iter]
#    if data == " ":
#        pass
#    else:
#         senatorsWithTwitter.append(data)
#            
#print(senatorsWithTwitter)
#    if data is None:
#        pass
#    else:
#        senatorsWithTwitter.append(data)
        
#for name in senatorsWithTwitter:
#    print(name)

#file = pd.read_csv("2010_City.csv", encoding= "ISO-8859-1")
#salaries = []
#for iter in file.index:
#    data = file["MaxPositionSalary"][iter]
#    salaries.append(data)
##       
#print(max(salaries))



#def getData(idList): 
#    for id in idList: 
#        fetchedLi = soup.findAll("li", {"id": id})
#        fetchedData.append(fetchedLi)
#    
#    for li in fetchedData: 
#        data.append(li[0].find("a").text)
#    
#data = []
#idList = []
#fetchedData = []
#url = "https://publicpay.ca.gov/Reports/RawExport.aspx"
#response = requests.get(url)
#soup = BeautifulSoup(response.text, "html.parser")
#text = ""
#for iter in range(1,6):
#    id = "2010_" + str(iter)
#    idList.append(id)
#getData(idList)
#idList.clear()
#for iter in range(1,7):
#    id = "2011_" + str(iter)
#    idList.append(id)
#getData(idList)
#idList.clear()
#for iter in range(1,7):
#    id = "2012_" + str(iter)
#    idList.append(id)
#    
#getData(idList)
#idList.clear()
#for iter in range(1,12):
#    id = "2013_" + str(iter)
#    idList.append(id)
#
#getData(idList) 
#print(data)
#    aTag = li.find_all("a")


#for li in fetchedData:
#    print(li)
#    aTag = li.find("a").text
#for li in fetchedLi:
#    print("++++++=", li)
#    aTag = li.find("a").text
#    print(aTag)
    
#aTags = soup.findAll("a")
#listOfLinks = []
#for link in aTags:
#    print(link.text)
##    if checkLink(link.text):
##        listOfLinks.append(link.text)
##    else: 
##        pass
#    
#print(listOfLinks)


#excelFile = pd.read_csv("magnitude.csv")s
#magnitudes = []
#for iter in excelFile.index:
#    link = excelFile["mag"][iter]
#    if int(link) >= 4.5:
#        magnitudes.append(link)
#    else: 
#        pass
#
#print(len(magnitudes))
        
#titleList = []
#castings = []
#movieNames = []
#hrefList = []
#summaries = []
#
#url = "http://www.imdb.com/chart/top"
#response = requests.get(url)
#soup = BeautifulSoup(response.text, "html.parser")
#titleColumn = soup.findAll("td", {"class": "titleColumn"})
#for title in titleColumn:
#    while (len(titleList) <= 5):
#        randomChoice = random.choice(titleColumn)
#        titleList.append(randomChoice)
#    else:
#         break
#    
#for title in titleList:
#    link = title.find("a")["title"]
#    href = title.find("a")
#    hrefList.append(href)
#    castings.append(link)
#    movieNames.append(title.find("a").text)
#    
#for href in hrefList:
#    movieUrl = "http://www.imdb.com" + href["href"]
#    response = requests.get(movieUrl)
#    soupObj = BeautifulSoup(response.text, "html.parser")
#    summary = soupObj.find("div", {"class": "summary_text"})
#    summaries.append(summary.text)
#    
#dataFrame = pd.DataFrame({"Title": movieNames, "Cast": castings,"Synopsis": summaries})
#writer = ExcelWriter("RandomMovies.xlsx")
#dataFrame.to_excel(writer, "Sheet1", index=False)
#writer.save()
    
#selectionCounter = 0
#list = [1,2,3,4,5,6,7,8, 9,0]
#for iter in range(0, 5):
#    print(random.choice(list))
#castings = []
#movieNames = []
#releaseYears = []


#url = "http://www.imdb.com/chart/top"
#response = requests.get(url)
#soup = BeautifulSoup(response.text, "html.parser")
#titleColumn = soup.findAll("td", {"class": "titleColumn"})
#for iter in range(225, len(titleColumn)):
#    aTags = titleColumn[iter].find("a")
#    title = aTags["title"]
#    castings.append(title)
#    movieNames.append(aTags.text)
#    releaseYears = titleColumn[iter].find("span",{"class": "secondaryInfo"})
#    sliced = slice(1, 5, 1)
#    slicedValue = releaseYears.text[sliced]
##    print(slicedValue)
#    releaseYears.append(str(slicedValue))
#    
#for y in releaseYears:
#    print(y)
    
#dataFrame = pd.DataFrame({"Name": movieNames, "Casting": castings, "Release Year": releaseYears})
#writer = pd.ExcelWriter("MovieDetails.xlsx")
#dataFrame.to_excel(writer, "Sheet1", index=False)
#writer.save()


#eventNames = []
#eventLocations = []
#eventStartDates = []
#eventEndDates = []
#
#url = "https://hackevents.co/search/anything/anywhere/anytime"
#response = requests.get(url)
#soup = BeautifulSoup(response.text, "html.parser")
#cards = soup.findAll("div", {"class": "card-body"})
#for card in cards:
#    c = card.find("div", {"class": "row"}).find("div", {"class": "col-12 col-sm-7"})
#    hackathonTitle = c.find("h3")
#    eventNames.append(hackathonTitle.text)
#    hackathonLocations = c.find("p")
#    eventLocations.append(hackathonLocations.text)
#    dates = c.findAll("p")
#    eventStartDates.append(dates[1].text)
#    eventEndDates.append(dates[2].text)
#
#dataFrame = pd.DataFrame({"Event Name": eventNames,  "Location": eventLocations, "Starting Date": eventStartDates, "Ending Date": eventEndDates})
#writer = ExcelWriter('EventDetails.xlsx')
#dataFrame.to_excel(writer, "Sheet1", index=False)
#writer.save()
    
    
#papercards = soup.findAll("h3")
#for card in papercards):
#    eventNames.append(card.text)
#    
#locations = soup.findAll("&emsp")
#for location in locations:
#    print(location)


#("i", {"class": "fas fa-map-marker-alt"})
#valuesList = []
#twitterHandle = input("Enter the name of your twitter handle")
#url = 'https://twitter.com/' + twitterHandle
#response = requests.get(url)
#soup = BeautifulSoup(response.text, "html.parser")
#profile = soup.findAll("span", {"class": "ProfileNav-value"})
#for value in profile:
#    valuesList.append(value.text)
#    
#dictionary = {"tweets": valuesList[0], "following": valuesList[1], "followers": valuesList[2], "likes": valuesList[3], "lists": valuesList[4]}
#print(dictionary["followers"])



#import requests
#import urllib.request
#from bs4 import BeautifulSoup
#import time
#import pandas as pd
#import os.path as op   
#import os
#import xlsxwriter

#root = op.abspath(os.sep)
#filepath = op.join(root , 'Html and Css Programs', 'testfile.csv')
#print(filepath)
#file = pd.read_csv(r'C:\HtmlandCssPrograms\testfile.csv')
#
#writer = pd.ExcelWriter("example.xlsx", engine="xlsxwriter")
#data = "ADitya Chaturvedi"
#data.to_excel(writer, 'Sheet1')
#writer.save()

#url = "http://www.pythonforbeginners.com"
#response = requests.get(url)
#content = response.text
#soup = BeautifulSoup(content, "html.parser")
#links = soup.findAll('a')
#webContent = []
#for iter in range(0, (len(links))):
#    aTag = soup.findAll('a')[iter]
#    link = aTag['href']
#    print(link)
#    downloadUrl = url + link
#    webContent.append(downloadUrl)
#    
#dataFrame = pd.DataFrame(webContent)
#dataFrame.to_csv("Output.csv")
#
#
#file = pd.read_csv('Output.csv', names = ['id', 'link'])
#file.drop(columns="id")
#print(file)



#import urllib.request
#import requests
#import time
#import pandas as pd
#from lxml import html
#
#
#url = 'https://twitter.com/johncena'
#resp = requests.get(url)
#soup = BeautifulSoup(resp.text, "html.parser")
#tweets = soup.findAll("p", {"class": "TweetTextSize"})
#for tweet in tweets: 
#        print(tweet.text)


#url = 'http://maps.googleapis.com/maps/api/geocode/json'
#address = {'address': '21 Ramkrishana Road, Burdwan, East Burdwan, West Bengal, India', 'language': 'en'}
#
#response = requests.get(url, params =address)
#
#print(response.json()['results'])
#url = 'https://www.us-cert.gov/ncas/alerts/2019'
#
#resp = requests.get(url)
#soup = BeautifulSoup(resp.text, "html.parser")
#soup.findAll("a")
#



#strongTags = soup.findAll("strong")
#for tag in strongTags: 
#    print(tag.text)
#resp = requests.get(url)
#soup = BeautifulSoup(resp.text, "html.parser")
#title = soup.title
#print(title)
#if title is None: 
#     print(" No title on the page")
#else: 
#    print("Title is present on the page")
#aTags = soup.findAll("a")   
#for aTag in aTags:
#    print(aTag.text )


#url = 'https://www.data.gov/meta/'
#response = requests.get(url)
#soup = BeautifulSoup(response.text, "html.parser")
#hTags = soup.findAll("h2", {"class": "entry-title"})
#list = soup.findAll("nav", {"class": "post-nav"})
#
#for hTag in hTags:
#    print(hTag.text)



#url = 'https://en.wikipedia.org/'
#downloadUrl = url + 'robots.txt'
#urllib.request.urlretrieve(downloadUrl, "Robots.txt")

#response = requests.get(url)
#soup = BeautifulSoup(resp.retonse.text, "html.parser")
#
#listOfLinks = soup.findAll("a", {"id": "post-title-25589992"})
#print(listOfLinks[0].text)
#for link in listOfLinks:
#    print(link.text)


#
#dataFrame = pd.read_excel('pandasexample.xlsx', sheet_name= 'Sheet1')
#
#csvData = []
#
#for iter in dataFrame.index:
#    link = dataFrame['Links'][iter]
#    csvData.append(link)
#    
#for url in csvData:
#    response = requests.get(url)
#    soup = BeautifulSoup(response.text, "html.parser")
#    links = soup.findAll('a')
#    for iterator in range(0, len(links)):
#        tag = soup.findAll('a')[iterator]
#        link = tag['href']
#        downloadUrl = url + link
#        urllib.request.urlretrieve(downloadUrl, "File" + str(iterator))
#        time.sleep(1)



#url = 'https://catalog.data.gov/dataset?q=&sort=metadata_created+desc'
#response = requests.get(url)
#
#soup = BeautifulSoup(response.text, "html.parser")
#
##hTags = soup.findAll('h3')
##tag = soup.findAll('h3')[0]
#print(soup.h3.a.text)
#list = [1,2,3,4,5]
#anotherList = map(lambda x: x + x, list)
#for ele in list:
#    print(ele)

#def removeDuplicates(list, element):
#    list.remove(element)
#
#def checkIfDuplicate(element, anotherList):
#    counter = 0
#    for ele in anotherList:
#        if element == ele:
#            counter = counter + 1
#        else:
#             pass
#            
#    return counter
#
#list = [1,2,3,4,5,6,0, 4]
#anotherList = list
#duplicates = []
#
#for element in list:
#    numberOfOccurence =  checkIfDuplicate(element, anotherList)
#    if numberOfOccurence >= 2:
#        duplicates.append(element)
#        print("duplicate element is -> ", element)
#    else: 
#        pass
#
#if duplicates == []:
#    print("No duplicate elements found")
#    
#else:
#    for element in duplicates:
#        removeDuplicates(list, element)
#        
#print(list)


#sentence = input("Enter the sentence")
#listOfWords = sentence.split(" ")
#listOfWords.reverse
#for ele in range((len(listOfWords) - 1),-1,-1):
#    print(listOfWords[ele])

#import random
#def checkBulls(digit):
#    global bulls
#    for ele in str(randomNumber):
#        if digit == ele:
#            bulls = bulls + 1
#    
#def checkCows(digit, index):
#    global randomNumber
#    global cows
#    if str(randomNumber)[iter] == digit:
#        cows = cows + 1
#    
#    
#randomNumber = random.randint(1000, 10000)
#bulls = 0
#cows = 0
#number = int(input("Enter your number"))
#for digit in str(number):
#    checkBulls(digit)
#    
#    
#for iter in range(0, len(str(number))):
#    checkCows(str(number)[iter], iter)
#
#print(cows)
#print(bulls)

#def checkForCommons(element):
#    global anotherList
#    global commons
#    if element in anotherList:
#        commons.append(element)
#    else:
#        pass
#    
#list = [1,2,3,4,5,6,7,8]
#anotherList = [1,2,3,12,43, 4,5]
#commons = []
#
#for element in list:
#    checkForCommons(element)
#    
#print(commons)


#string = "banana"
#combinations = []
#
#for char in string:
#    combinations.append(char)
#    
#for iter in range(0, (len(string) - 1)):
#    subset = slice(0, iter , 1)
#    combinations.append(string[subset])
#    print(string[subset])
#dictionary = { }

#def insertValues(key):
#    global dictionary 
#    dictionary.__setitem__(key, (key * key))
#    
#for iter in range(1, 4):
#    insertValues(iter)
#    
#print(dictionary)


#list = [1,2,3,4,5,6,7,8,9,10]
#squared = map(lambda x: x*x,list)
#for ele in squared:
#    print(ele)

#for iter in range((len(list) - 5), len(list)):
#    print(list[iter])

#class Practice:
#    
#    def staticMethod():
#        print(" I am static")
#
##Practice.staticMethod = staticmethod(Practice.staticMethod)
#Practice.staticMethod()


#class American:
#    def printNationality():
#        print("Nationality = American")
#        
#American.printNationality()


#string = "2 cats and 3 dogs"
#digits = []
#splittedString = string.split(" ")
#digits = [ word for word in splittedString]
#print(digits)
#for word in splittedString:
#    try:
#        digits.append(int(word))
#    except ValueError:
#        pass
#    
#if digits == []:
#    print(" No digits")
#else: 
#    print(digits)
#        
#series = [0,1]
#n = int(input("Enter the value of n"))
#while len(series) <= n:
#    list = [x  for x in range(n) if len(series) <= n]
##    series = [(series[len(series) - 2] + series[len(series) - 1]) for ele in series]
##    series.append((series[len(series) - 2] + series[len(series) - 1]))
#    
#print(list)



#TODO
#list = [1,2,3,4,5,6,7,8,9,10]
#def binary_search(element, list):
#        middleValue = list[int(len(list) / 2) - 1]
#        if element > middleValue:
#            filtered_list = [list[ele] for ele in range((int(len(list) / 2) - 1), (len(list) - 1))]
#            print(filtered_list)
#
#element = int(input("enter the element to be searched for"))
#binary_search(element, list)

#import zlib
#string = "aditya"
#print(zlib.compress(string))
#
#subjects = ["I", "You"]
#verbs = ["Play", "Love"]
#objects = ["Hockey", "Football"]
#sentences = []
#def makeSentence():
#    global subjects, verbs, objects, sentences
#    for subject in subjects:
#        for iter in range(0, (len(verbs))):
#            for iterator in range(0, (len(objects))):
#                sentence = subject + " " + verbs[iter] + " " + objects[iterator]
#                sentences.append(sentence)
#
#makeSentence()
#
#for sentence in sentences:
#    print(sentence)
#


#list  = [5,6,77,45,22,12,24]
#
#filteredList = [ele for ele in list if not (ele % 2 == 0)]
#print(filteredList)


#list = [12,24,35,70,88,120,155]
#filteredList = [ele for ele in list if ele is not list[0] and ele is not list[2] and ele is not list[4] and ele is not list[6]]
#print(filteredList)

#
#string =  "abcdefgabc"
#for char in string:
#    print(char, string.count(char))

#import json 
#print("111111111111111111111111")
#with open('json_dataset.txt') as json_file:
#    data = json.load(json_file)
#    print(data)
#
# class A:
#     def __init__(self):
#         self._a = "1"
        
#     def get_self_a():
#         return self._a
    
# class B(A):
#     def __init__(self):
#         A.__init__(self)
#         print(self._a)
        
# obj = B()
#print(obj._a)

class Time():
    def __init__(self, *args):
        if len(args) is 0: 
            (hours, minutes, seconds) = (0, 0, 0)
        else:
            (hours, minutes, seconds)  = args
        self.hours = hours
        self.minutes = minutes 
        self.seconds = seconds 


time_1 = Time(1, 2, 3)
time_2 = Time(1, 2, 3)

def check_for_hours(time):
    if time.hours >= 24:
        return True
    else: 
        return False 

def check_for_minutes(time):
    if time.minutes >= 60:
        return True 
    else: 
        return False 

def update_minutes_and_hours(time_1):
    if check_for_hours(time_1): 
        time_1.hours = time_1.hours + 1
    else: 
        pass

def change_time(time_1):
    if time_1.seconds >= 60:
        time_1.seconds = time_1.seconds - 60
        if check_for_minutes(time_1):
            time_1.minutes = time_1.minutes - 60
            if check_for_hours(time_1): 
                time_1.hours = time_1.hours + 1
            else: 
                pass 
        else: 
            pass 
    elif check_for_minutes(time_1):
        time_1.minutes =  time_1.minutes - 60
        if time_1.hours == 23: 
            time_1.hours = 24
        update_minutes_and_hours(time_1)

    elif check_for_hours(time_1):
        time_1.hours = time_1.hours - 24
    else: 
        time_1 

# o = Time(23, 64, 67)
# change_time(o)
# print(o.hours, o.minutes, o.seconds)

# This is a pure function
def add_time(time_obj, time_obj_2):
    time_3 = Time()
    time_3.hours = time_1.hours + time_2.hours 
    time_3.minutes = time_1.minutes + time_2.minutes 
    time_3.seconds = time_1.seconds + time_2.seconds 
    return time_3  

time_3 = add_time(time_1, time_2)
# print(time_3.hours, time_3.minutes, time_3.seconds)

def change_time_v2(time): 
    hrs = time.hours 
    mins = time.minutes 
    secs = time.seconds
    updated_secs = time.seconds - 60
    updated_mins = time.minutes - 60 
    updated_hrs = time.hours - 24

    if secs >= 59: 
        if mins >= 59:
            if hrs >= 23: 
                time.seconds =  updated_secs
                time.minutes = updated_mins 
                time.hours = updated_hrs 
            else: 
                time.seconds = updated_secs 
                time.minutes = updated_mins

        else: 
            if hrs >=23: 
                time.seconds = updated_secs 
                time.hours = updated_hrs 
            else: 
                time.seconds = updated_secs 

    if not (secs >= 59):
        if mins >= 59: 
            if hrs >= 23: 
                time.minutes = updated_mins
                time.hours = updated_hrs 
            else: 
                time.minutes = updated_mins 
        else: 
            if hrs >= 23: 
                time.hours = updated_hrs 
            else: 
                time

# o = Time(25, 62, 70)
# change_time_v2(o)
# print(o.hours, o.minutes, o.seconds)



even_numbers = [x for x in range(0, 20) if x % 2 == 0 ]

test_list = [ x for x in range(100) if x % 5 == 0 and x % 3 == 0]

nested_list = [x * y for x in range(3) for y in range(3)]

dummy_function = lambda x: x * 2


dummy_list = [x for x in range(20)]

print(list(filter(lambda x: x % 2 == 0, dummy_list)))

