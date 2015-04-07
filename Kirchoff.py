class Array:

    def __init__(self, dimensions):
        self.dimensions = int(dimensions)
        self.array = [[0 for x in range(self.dimensions)] for x in range(self.dimensions)]
        self.last_action = "We start with this array:"

    def addRow(self, row, values):
        for i in range(self.dimensions):
            self.array[row][i] = int(values[i])

    def decrementDimension(self):
        self.dimensions -= 1

    def print(self):
        print("Printing Array")
        for i in range(self.dimensions):
            print("")
            for j in range(self.dimensions):
                print(self.array[i][j],end=" ")
        print('\n')

    def deleteRowAndColumn(self, row):
        tempArray = [[0 for x in range(self.dimensions - 1)] for x in range(self.dimensions - 1)]
        print(tempArray)
        tempArrayRow = 0
        tempArrayColumn = 0
        i = 0
        j = 0
        print("row: "+str(row))
        while(i < self.dimensions):
            if(i == row):
                i+=1
                continue
            print("i: "+str(i))
            while(j < self.dimensions):
                if(j == row):
                    j+=1
                    continue
                print("j: "+str(j))
                print(self.array[i][j])
                tempArray[tempArrayRow][tempArrayColumn] = self.array[i][j]
                j+=1
                tempArrayColumn += 1
            i+=1
            tempArrayRow+=1
            j=0
            tempArrayColumn = 0
        print(tempArray)
        self.array = [[0 for x in range(self.dimensions - 1)] for x in range(self.dimensions - 1)]
        for i in range(self.dimensions - 1):
            for j in range(self.dimensions - 1):
                self.array[i][j] = tempArray[i][j]

    def deleteRow(self, row):
        tempArray = [[0 for x in range(self.dimensions)] for x in range(self.dimensions - 1)]
        tempArrayRow = 0
        i = 0
        while(i < self.dimensions):
            if(i == row):
                i+=1
                continue
            for j in range(self.dimensions):
                tempArray[tempArrayRow][j] = self.array[i][j]
            tempArrayRow += 1
            i+=1
        self.array = tempArray
        self.last_action = "Deleted row " + str(row + 1)

    def deleteColumn(self, column):
        tempArray = [[0 for x in range(self.dimensions - 1)] for x in range(self.dimensions)]
        tempArrayColumn = 0
        j = 0
        for i in range(self.dimensions - 1):
            while(j < self.dimensions):
                if(j == column):
                    j+=1
                    continue
                tempArray[i][tempArrayColumn] = self.array[i][j]
                j+=1
                tempArrayColumn += 1
            tempArrayColumn = 0
            j = 0
        self.array = tempArray
        self.last_action += ". Deleted column " + str(column + 1)


    def addRowToRow(self, destination, source, coefficient=1):
        for i in range(self.dimensions):
            self.array[destination][i] += coefficient * self.array[source][i]
        self.print()
        self.last_action = "R" + str(destination + 1) + " <- R" + str(destination + 1) + " + " + \
                            str(coefficient) + "R" + str(source + 1)

    def subtractRowFromRow(self, destination, source, coefficient):
        for i in range(self.dimensions):
            self.array[destination][i] -= coefficient * self.array[source][i]
        self.print()
        self.last_action = "R" + str(destination + 1) + " <- R" + str(destination + 1) + " - " + \
                            str(coefficient) + "R" + str(source + 1)


    def outputToFile(self):
      output = open("output.txt", 'a')
      output.write(self.last_action)
      output.write('\n')
      for i in range(self.dimensions):
            for j in range(self.dimensions):
                output.write(str(self.array[i][j]))
                output.write(" ")
            output.write('\n')
      output.close()



def main():
    arrayDim = input("Please enter the dimensions of your array: ")
    theArray = Array(arrayDim)
    for i in range(theArray.dimensions):
        print("Please enter row: " + str(i+1))
        values = input()
        valuesArray = values.split()
        #the algorithm requires a square matrix
        while(len(valuesArray) != theArray.dimensions):
            print("Error")
            print("Please enter row: " + str(i+1))
            values = input()
            valuesArray = values.split()
        theArray.addRow(i, valuesArray)

    theArray.print()

    proceed = True
    while(proceed):
        print("Choose a following command: ")
        print("0. Exit")
        print("2. Print the array")
        print("3. Delete a row and column")
        print("4. Add row to another row")
        print("5. Subtract row from another row")
        print("6. Output to file")
        print('')
        action = input()
        if(action == "2"):
            theArray.print()
        elif(action == "3"):
            row = input("which row do you wish to delete? ")
            theArray.deleteRow(int(row) - 1)
            column = input("Which column do you wish to delete? ")
            theArray.deleteColumn(int(column) - 1)
            theArray.decrementDimension()
            theArray.print()
        elif(action == "4"):
            destination = input("Enter the row you wish to change: ")
            while(int(destination) > theArray.dimensions or int(destination) <= 0):
                destination = input("Enter the row you wish to change: ")
            source = input("Enter the row you wish to add to your destination: ")
            while(int(source) > theArray.dimensions or int(source) <= 0):
                source = input("Enter the row you wish to change: ")
            coefficient = input("Enter the coefficient: ")
            theArray.addRowToRow(int(destination) - 1, int(source) - 1, int(coefficient))
        elif(action == "5"):
            destination = input("Enter the row you wish to change: ")
            while(int(destination) > theArray.dimensions or int(destination) <= 0):
                destination = input("Enter the row you wish to change: ")
            source = input("Enter the row you wish to subtract your destination: ")
            while(int(source) > theArray.dimensions or int(source) <= 0):
                source = input("Enter the row you wish to change: ")
            coefficient = input("Enter the coefficient: ")
            theArray.subtractRowFromRow(int(destination) - 1, int(source) - 1, int(coefficient))
        elif(action == "0"):
            proceed = False
        elif(action == "6"):
            theArray.outputToFile()
        else:
            proceed = input("Enter 1 to proceed or press enter to exit: ")

main()
    
