queue = []


def insert():
    global queue
    valueToBeInserted = input("Enter the value to be inserted")
    queue.insert(0,valueToBeInserted)
    print(queue)
    userChoice()

def delete():
    global queue
    queue.reverse()
    del queue[0]
    queue.reverse()
    print(queue)
    userChoice()

def callAppropriateFunction(userInput):
    if userInput == "1":
        insert()
    elif userInput == "2":
        delete()
    else:
        print("Invalid Input")
        exit(0)

def userChoice():
  print("1.) Insert Value into queue")
  print("2.) Delete Value from queue")
  userInput= input("Enter your choice")
  callAppropriateFunction(userInput)


userChoice()
