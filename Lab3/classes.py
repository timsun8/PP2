class myClass():

    def getString(self):
        self.userInput = input()
    def printString(self):
        print(self.userInput.upper())
    
x = myClass()
x.getString()

x.printString()
