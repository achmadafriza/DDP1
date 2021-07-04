import validators.url
from tabulate import tabulate
import csv

class BudayaKB:
    """
    This is a base Class for BudayaKB.

    Data structure:
        - cultureData = {"Name": ["Name", "Type", "Province", "Reference URL"]}
        - dictType = {"Type": set("Name")}
        - dictProv = {"Prov": set("Name")}

    Traditional Getter-Setter is not needed due to the Problem Type.
    """
    def __init__(self):
        """ Initializes data structure """
        print("#####")
        print("BudayaKB Lite v1.0")
        print("~Let’s promote and conserve our culture!~")
        print("#####")
        print("Type HELP for reference.")

        self.__cultureData = {}
        self.__dictType = {}
        self.__dictProv = {}


    def switcher(self, command):
        """
        Args:
            - (list)command = [FUNCTION, [Command]]

        Runs the function specified in the Command: switcher(object, functionName) -> object.functionName()
        Raises AttributeError if not found.

        I know writing many if-elif case is hard, this is a switch-case method familiar in Java and C++.
        """
        run = getattr(self, command[0])
        run(command[1])

        return print("#####")

    def HELP(self, command):
        """
        Args:
            - (list)command: [HELP, FunctionName]

        This is a helper function for Class BudayaKB.

        Calling:
            - HELP at prompt prints help for BudayaKB.
            - HELP FUNCTION at prompt prints help for specific method in BudayaKB.

        When FunctionName is invalid, i.e. 'stat prov' or 'lalala', it prints "Invalid".
        """
        if not command[0]:
            help(BudayaKB)
        else:
            try:
                help(getattr(self, command[0].upper()))
            except AttributeError:
                print(f"There's no function {command[0].upper()}")

    def _validateValue(self, value):
        if len(value) != 4: # Checks if format is valid
            print("There should be 4 items formatted as: Name;;;Type;;;Province;;;Reference URL")
            raise SyntaxError

        if value[3][:7] != "http://" and value[3][:8] != "https://": # Validator is weird, i need to add http://
            value[3] = "http://" + value[3]
        if not validators.url(value[3]): # Validates URL
            print("URL is Invalid")
            raise SyntaxError

    def _validateAdd(self, value):
        if value[0] in self.__cultureData.keys(): # Checks whether value exists in BudayaKB
            raise ValueError

    def _addValue(self, value):
        self.__cultureData[value[0]] = value # Adds Name;;;Type;;;Province;;;Reference URL to cultureData

        # Adds Name into dictType[Type]
        if value[1] not in self.__dictType.keys():
            self.__dictType[value[1]] = {value[0]} # Initiates Set(Name)
        else:
            self.__dictType[value[1]].add(value[0])

        # Adds Name into dictType[Type]
        if value[2] not in self.__dictProv.keys():
            self.__dictProv[value[2]] = {value[0]} # Initiates Set(Name)
        else:
            self.__dictProv[value[2]].add(value[0])

    def _removeValue(self, value):
        # Removes Name from dictType[Type]
        if len(self.__dictType[value[1]]) == 1:
            self.__dictType.pop(value[1])
        else:
            self.__dictType[value[1]].remove(value[0])

        # Removes Name from dictProv[Type]
        if len(self.__dictProv[value[2]]) == 1:
            self.__dictProv.pop(value[2])
        else:
            self.__dictProv[value[2]].remove(value[0])

        self.__cultureData.pop(value[0]) # Removes Name from BudayaKB

    def _askOverwrite(self, value):
        if value == self.__cultureData[value[0]]: # If value is equal, we don't need to ask for overwrite
            return print(f"{value} exists")

        while True: # Keeps asking for the correct input
            ask = input(f"Name {value} = {self.__cultureData[value[0]]}, do you want to overwrite (y/n)? ")
            if ask.lower() == 'y':
                return self.UPDATE(value)
            elif ask.lower() == 'n':
                return print(f"\"{value[0]}\" is not overwritten")

    def ADD(self, command):
        """
        Args:
            - (list)command: ["Name", "Type", "Province", "Reference URL"]
        Format: ADD Name;;;Type;;;Province;;;ReferenceURL

        Setter method for BudayaKB.

        When:
            - "Name" doesn't exist, adds (list)command to BudayaKB.
            - "Name" exists, it asks for Overwrite. If yes, then calls UPDATE().
            - When command (list) format is invalid, it prints "Invalid".
        """
        try:
            self._validateValue(command) # Raises SyntaxError if not valid
            self._validateAdd(command) # Raises ValueError if not valid

            self._addValue(command)
            print(f"\"{command[0]}\" is added")
        except ValueError:
            self._askOverwrite(command)
        except SyntaxError:
            print(f"Adding \"{command[0]}\" failed")

    def UPDATE(self, command):
        """
        Args:
            - (list)command: ["Name", "Type", "Province", "Reference URL"]
        Format: UPDATE Name;;;Type;;;Province;;;ReferenceURL

        Setter method for BudayaKB.

        When:
            - "Name" exists, it updates "Name" in BudayaKB to command (list).
            - "Name" doesn't exist in BudayaKB, it prints "Invalid".
            - When (list)command format is invalid, it prints "Invalid".
        """
        try:
            self._validateValue(command) # Raises SyntaxError if not valid

            self._removeValue(self.__cultureData[command[0]])
            self._addValue(command)

            print(f"\"{command[0]}\" is updated")
        except KeyError:
            print(f"\"{command[0]}\" doesn't exist")
        except SyntaxError:
            print(f"Updating \"{command[0]}\" failed")

    def REMOVE(self, command):
        """
        Args:
            - (list)command: ["Name"]
        Format: REMOVE Name

        Delete method for BudayaKB.

        When:
            - "Name" exists, it Deletes "Name" in BudayaKB.
            - "Name" doesn't exist in BudayaKB, it prints "Invalid".
            - When (list)command format is invalid, it prints "Invalid".
        """
        try:
            if command[0] == False: # Invalid, User only inputs REMOVE
                return print("Command is invalid, format: REMOVE Name")

            self._removeValue(self.__cultureData[command[0]]) # Raises KeyError if value doesn't exist
            print(f"\"{command[0]}\" is removed")
        except KeyError:
            print(f"\"{command[0]}\" doesn't exist")

    def FINDNAME(self, command):
        """
        Args:
            - (list)command: ["Name"]
        Format: FINDNAME *
                FINDNAME Name

        Getter (Name) method for BudayaKB.

        When:
            - '*', prints all values.
            - Name, prints ("Name", "Type", "Province", "Reference URL") for Name
            - Name is not found in cultureData, prints "Invalid"
        """
        try:
            if command[0] == '*':
                if not self.__cultureData: # Invalid if BudayaKB is empty
                    return print("Culture data is empty!")

                print(tabulate(self.__cultureData.values(), headers=["Name", "Type", "Province", "Reference URL"]))
            else: # Raises KeyError if value doesn't exist
                print("{0[0]}, {0[1]}, {0[2]}, {0[3]}".format(self.__cultureData[command[0]]))
        except KeyError:
            print(f"\"{command[0]}\" is not found")

    def FINDTYPE(self, command):
        """
        Args:
            - (list)command: ["Type"]
        Format: FINDTYPE Type

        Getter (Type) method for BudayaKB.

        When:
            - Type, it prints all Name's that have Type = Type
            - Type is not found in cultureData, prints "Invalid"
        """
        try:
            print(f"Found {len(self.__dictType[command[0]])} {command[0]}") # If not found raises KeyError

            values = [self.__cultureData[i] for i in self.__dictType[command[0]]]
            print(tabulate(values, headers=["Name", "Type", "Province", "Reference URL"]))
        except KeyError:
            print(f"\"{command[0]}\" is not found")

    def FINDPROV(self, command):
        """
        Args:
            - (list)command: ["Prov"]
        Format: FINDPROV Prov

        Getter (Province) method for BudayaKB.

        When:
            - Prov, it prints all Name's that have Province = Prov
            - Prov is not found in cultureData, prints "Invalid"
        """
        try:
            print(f"Found {len(self.__dictProv[command[0]])} {command[0]}") # If not found raises KeyError

            values = [self.__cultureData[i] for i in self.__dictProv[command[0]]]
            print(tabulate(values, headers=["Name", "Type", "Province", "Reference URL"]))
        except KeyError:
            print(f"\"{command[0]}\" is not found")

    def STAT(self, command):
        """
        Format: STAT

        Prints how many cultural heritage are there
        """
        if command[0] == False:
            print(f"There are {len(self.__cultureData)} cultural heritage")
        else:
            print("STAT doesn't need other command")

    def STATTYPE(self, command):
        """
        Format: STATTYPE

        Prints table for Type and it's Occurrence.
        i.e.
              Type    Occurrence
            ------  ------------
                 2             2
                 3             1
        """
        if command[0] == False:
            ans = [(i, len(self.__dictType[i])) for i in self.__dictType] # Makes Tuples of Type and length of Set(Type)
            ans.sort(key = lambda a: a[1], reverse = True) # Sorts based on Occurrence

            print(tabulate(ans, headers=["Type", "Occurrence"]))
        else:
            print("STATTYPE doesn't need other command")

    def STATPROV(self, command):
        """
        Format: STATTYPE

        Prints table for Province and it's Occurrence.
        i.e.
              Province    Occurrence
            ----------  ------------
                     4             2
                     3             1
        """
        if command[0] == False:
            ans = [(i, len(self.__dictProv[i])) for i in self.__dictProv] # Makes Tuples of Prov and length of Set(Type)
            ans.sort(key = lambda a: a[1], reverse = True) # Sorts based on Occurrence

            print(tabulate(ans, headers=["Province", "Occurrence"]))
        else:
            print("STATPROV doesn't need other command")

    def IMPORT(self, fileName):
        """
        Args:
            - (list)fileName: ["fileName"]
        Format: IMPORT file.csv
        Value Format: Name, Type, Province, ReferenceURL

        Imports .csv file to BudayaKB.

        When on Value:
            - a value in the file is invalid, it is skipped.
            - a value overlaps in BudayaKB, asks for Overwrite
        """
        try:
            if '.csv' != fileName[0][-4:]:
                return print("Wrong Format. Please use .csv file format")

            with open(fileName[0], 'r') as file: # Raises FileNotFoundError and OSError
                lines = csv.reader(file)
                for value in lines:
                    try:
                        self._validateValue(value) # Raises SyntaxError if not valid
                        self._validateAdd(value) # Raises ValueError if not valid

                        self._addValue(value)
                    except ValueError:
                        self._askOverwrite(value)
                    except SyntaxError:
                        if value == []:
                            continue
                        print(f"{value} is skipped")

            print(f"{fileName[0]} is successfully imported")
        except FileNotFoundError:
            print("File doesn't exist")
        except OSError as e:
            print(e)
            print("File error/corrupted, can't be accessed")

    def _writeFile(self, command, parameter):
        with open(command[0], parameter, newline='') as file:
            writer = csv.writer(file)
            writer.writerows(self.__cultureData.values())

    def EXPORT(self, command):
        """
        Args:
            - (list)command: ["fileName"]
        Format: EXPORT file.csv

        Exports BudayaKB to .csv file.
        Value Format: Name, Type, Province, ReferenceURL

        When file.csv exists, it asks for Overwrite:
            - if user says no, then BudayaKB is appended into file.csv
        """
        try:
            if command[0][-4:] != '.csv':
                return print("Wrong Format. Please use .csv file format")
            if len(self.__cultureData) == 0:
                return print("BudayaKB is empty")

            self._writeFile(command, 'x') # Exclusive creation of file

            print(f"{len(self.__cultureData)} rows exported")
        except FileExistsError:
            while True:  # Asks for file overwrite until correct input
                ask = input("File Exists. Do you want to overwrite (y/n)?")
                if ask == 'y':
                    self._writeFile(command, 'w') # Overwrite file
                    break
                elif ask == 'n':
                    self._writeFile(command, 'a') # Appending to file
                    break

            print(f"{len(self.__cultureData)} rows exported")
        except OSError as e:
            print(e)
            print(f"Unexpected Error has happened while Exporting to {command[0]}")


def formatCommand(s):
    """
    Formats command into [FUNCTION, [Name, Type, Province, referenceURL]]
    For further info of FUNCTION please refer to specific FUNCTION in BudayaKB
    """
    command = s.split(' ', maxsplit=1)
    try:
        command[0] = command[0].upper()

        command[1] = command[1].split(';;;') # Splits Command by Syntax
        for i in range(len(command[1])):
            if i != len(command[1])-1: # Capitalizes every word in Command except for URL
                command[1][i] = command[1][i].split()
                for k in range(len(command[1][i])):
                    command[1][i][k] = command[1][i][k].capitalize()

                command[1][i] = ' '.join(command[1][i])

        return command
    except IndexError:
        command.append([False]) # Indicates that FUNCTION does not need other commands
        return command


def inputCommand(s, database):
    command = formatCommand(s)
    if command[0] == "EXIT":
        return print("~Goodbye, don't forget to love Indonesian cultural heritage!~")

    try:
        database.switcher(command)
    except AttributeError:
        print(f"There's no function {command[0]}, please try again.")

    return True


def main():
    database = BudayaKB()
    while inputCommand(str(input("> Insert Command: ")), database):
        pass


if __name__ == '__main__':
    main()