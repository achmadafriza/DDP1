# Import Library
import matplotlib.pyplot as plt # Graphing the array
import string # Punctuations
#-----------------------------------------------------------------------------------------------------------------------
# Here, i used divide and conquer method for better task organization and code reusability
def inputStopWord(): # Inputting stopWords.txt into a Set data structure for searching optimization
    fileName = "stopWords.txt"
    file = fileInput(fileName) # Inputting stopWords.txt, returns List of lines (str)

    fileSet = set() # Initializing Set
    for i in file: # Stripping whitespaces and adding to fileSet
        i = i.strip()
        fileSet.add(i)

    return fileSet

def fileInput(fileName): # Opens fileName and returns lines as a List
    try: # Try Catch method for open(), as it is error prone to user input
        if '.txt' != fileName[-4:]: raise OSError # I want to make the opened file only .txt format

        # As some characters in stopWord.txt, JokoWidodoSpeechAPEC2014.txt, etc have characters in Unicode,
        # when read, it is still encoded. I need to define the encoding for the file.
        file = open(fileName, 'r', encoding="utf-16")
        lines = file.readlines() # Read the lines and returns a List of lines
        file.close() # Garbage Collection

        return lines

    except OSError: # OSError Handling, prompting user to input the correct file
        fileInput(input("Wrong format/file inputted. Please input another file: "))

def wordFormatting(word): # Function to format word, returns formatted word
    word = word.lower() # Lowercases the word, needed for checking stopWords
    # Removing punctuations and whitespaces
    for punctuation in string.punctuation + " \n": word = word.replace(punctuation, '')
    if word in stopWord: word = '' # Checking if it is a stopWord, then changing into a blank string

    word = word.capitalize() # Capitalizing the word for aesthetical reasons
    return word

def inputInDictionary(word): # Counting the words, uses dictionary for easeness
    word = str(word) # Somehow, the parameter is a list of chars...
    if word in count.keys():
        count[word] += 1
    elif word != '': # As the stopWords are changed into '', we need to remove it (e.g. not count it)
        count[word] = 1

def compareUsage(array): # Comparison function for sorting by Usage
    return array[1]

def compareWord(array): # Comparison function for sorting by Words
    return array[0]

# Printing the Array into a Table (Actually there's a function tabulation(), but i'm not sure if i can use it)
def printTable(word, usage):
    print("{:>3}|{:>18}|{:>7}".format("No", "Word", "Usage"))
    print("{}|{}|{}".format("="*3, "="*18, "="*7))

    for num in range(len(word)):
        print("{:>3}|{:>18}|{:>7}".format(num+1, word[num], usage[num]))

# Printing the Bar Chart using matplotlib
def printBarChart(x, y, barWidth, fileName):
    plt.title("Word Frequencies of " + fileName)

    plt.xlabel("Usage")
    plt.barh(range(len(x)), x, barWidth, color = 'r')

    plt.yticks(range(len(y)), y)
    plt.show()

# Changing the Pair into 2 Lists (Tuple)
def changePairtoList(array):
    word, usage = [], []
    for i, j in arrWords:
        if len(word) == 36:
            break

        word.append(i)
        usage.append(j)

    return word, usage
#-----------------------------------------------------------------------------------------------------------------------
print("Create word frequency table and bar chart from a text file")
print("----------------------------------------------------------")

stopWord = inputStopWord()

fileName = input("Please enter the file name: ")
file = fileInput(fileName)

# Processing the lines, inputting it into Dictionary
count = {}
for line in file:
    splitLine = line.split(' ') # Splitting the string into array
    for word in splitLine: # Processing per word in the line
        word = wordFormatting(word)
        inputInDictionary(word)

# Changing the Dictionary into Pair-List format
arrWords = []
for i, j in count.items():
    temp = [i, j]
    arrWords.append(temp)

# Making the Table based on sorted Usage (From High to Low)
arrWords.sort(key = compareUsage, reverse = True)
word, usage = changePairtoList(arrWords) # changePairtoList returns Tuple
printTable(word, usage)

# Making the Bar Chart based on sorted Words (From High to Low)
arrWords = arrWords[:36] # Splitting the array into top 36 variables
arrWords.sort(key = compareWord, reverse = True)
word, usage = changePairtoList(arrWords) # changePairtoList returns Tuple
printBarChart(usage, word, 0.6, fileName)

input("\nPlease type Enter to exit ...")