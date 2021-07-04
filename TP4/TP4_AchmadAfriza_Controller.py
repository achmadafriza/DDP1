from TP4_AchmadAfriza_Model import Barcode
from TP4_AchmadAfriza_View import App


class Controller:
    def __init__(self):
        self.mainWindow = App()
        self.mainWindow.setBind(self.saveFile, self.printCode)

    def printCode(self, *args):
        try:
            codeObject = Barcode(self.mainWindow.getCode())
            self.mainWindow.print(codeObject.getBarcode(), codeObject.getCode())

            if self.mainWindow.getFilename():
                self.saveFile()
        except IndexError:
            self.mainWindow.showError("IndexError", "Length of code is not 12!")
        except ValueError:
            self.mainWindow.showError("TypeError", "Code is not comprised of Integers!")

    def saveFile(self, *args):
        try:
            if self.mainWindow.getCode():
                codeObject = Barcode(self.mainWindow.getCode())
                self.mainWindow.print(codeObject.getBarcode(), codeObject.getCode())

            try:
                with open(self.mainWindow.getFilename(), 'r') as f:
                    if f: raise FileExistsError
            except FileNotFoundError:
                pass

            self.mainWindow.savePS()
        except FileExistsError:
            self.mainWindow.showError("FileExistsError", "File Exists. Program will not continue to save file!")
        except TypeError:
            self.mainWindow.showError("FileTypeError", "File format is wrong!")
        except IndexError:
            self.mainWindow.showError("EmptyCanvasError", "Code is yet to be inputted!")
        except ValueError:
            self.mainWindow.showError("TypeError", "Code is not comprised of Integers!")


def main():
    x = Controller()
    x.mainWindow.run()


if __name__ == '__main__':
    main()