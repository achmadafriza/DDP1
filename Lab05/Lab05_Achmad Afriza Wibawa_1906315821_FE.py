def putNumber(line, number): # Function to format the Number and String
    return "{:0>3}. {}".format(number, line)

def fileInput(fileName): # Function to open the file and change it into a List format per lines
    try: # Try Catch method for Error Prone open()
        if '.txt' != fileName[-4:]: # I want to make the opened file only .txt format
            raise OSError

        file = open(fileName, 'r')
        lines = file.readlines() # Read the lines and returns a List of lines
        file.close() # Garbage Collection

        return lines

    except OSError: # Prompting user to input the correct file
        fileInput(input("Wrong format/file inputted. Please input another file: "))

def main(): # Starting block for Program
    # Asks user for initial input
    lineArray, charNumber = fileInput(input("Please enter the input file name: ")), 0
    outputFile = open(input("Please enter the output file name (it will replace any file): "), 'w')

    for i in range(len(lineArray)): # Processing the file per line, accessing by index of array
        charNumber += len(lineArray[i]) # Counting how many chars per line
        print(putNumber(lineArray[i], i+1), file = outputFile, end = '') # Outputting to file

    print(f"\nThe total number of characters of the input file: {charNumber}", file = outputFile, end = '')
    outputFile.close() # Garbage Collection

if __name__ == '__main__': # From the Template
    main()