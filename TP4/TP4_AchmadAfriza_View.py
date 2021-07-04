from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class App:
    def __init__(self):
        # BaseApp
        self.__root = Tk()
        self.__root.title("EAN-13 [by Achmad Afriza Wibawa]")
        self.__root.resizable(width=False, height=False)

        # Variables
        self.__psFileName = StringVar()
        self.__code = StringVar()

        # Main Frame
        self.__mainFrame = ttk.Frame(self.__root, padding=(10, 0, 10, 5))
        self.__mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))

        ttk.Style().configure('BlueText.TLabel', foreground='blue', font='bold')

        # PostScript Frame
        self.__psFrame = ttk.Frame(self.__mainFrame, padding=(0, 0, 0, 5))
        self.__psFrame.grid(column=0, row=0)
        ttk.Label(self.__psFrame, text="Save barcode to PostScript File [eg: EAN13.eps]:", style='BlueText.TLabel')\
            .grid(column=0, row=0, pady=5)
        self.__psEntry = ttk.Entry(self.__psFrame, width=50, textvariable=self.__psFileName)
        self.__psEntry.grid(column=0, row=1)

        # Code Frame
        self.__codeFrame = ttk.Frame(self.__mainFrame)
        self.__codeFrame.grid(column=0, row=1)
        ttk.Label(self.__codeFrame, text="Enter code (First 12 decimal digits):", style='BlueText.TLabel')\
            .grid(column=0, row=0, pady=5)
        self.__codeEntry = ttk.Entry(self.__codeFrame, width=12, textvariable=self.__code)
        self.__codeEntry.focus()
        self.__codeEntry.grid(column=0, row=1)

        # Tab KeyBind
        self.__codeEntry.bind('<Tab>', lambda e: self.__psEntry.focus())
        self.__psEntry.bind('<Tab>', lambda e: self.__codeEntry.focus())

        # Barcode Canvas
        self.__canvas = Canvas\
            (self.__codeFrame, bg='white', highlightthickness=1, highlightbackground='black', width=400)
        self.__canvas.grid(column=0, row=2, pady=10)

    def setBind(self, ps, code):
        self.__psEntry.bind('<Return>', ps)
        self.__codeEntry.bind('<Return>', code)

    def getFilename(self):
        return self.__psFileName.get()

    def getCode(self):
        return self.__code.get()

    def showError(self, title, message):
        messagebox.showerror(title, message)

    def savePS(self):
        if self.__psFileName.get()[-3:] != '.ps' and self.__psFileName.get()[-4:] != '.eps':
            raise TypeError
        if not self.__canvas.find_all():
            raise IndexError

        self.__canvas.postscript(file=self.__psFileName.get(), colormode='color')

    def print(self, bits, code):
        self.__canvas.delete('all')
        self.__canvas.create_text(200, 40, fill='blue', font='* 18 bold', text='EAN-13 Barcode:')

        for i in range(95):
            if bits[i] != '0':
                if 0 <= i <= 2 or 45 <= i <= 49 or 92 <= i <= 94:
                    self.__canvas\
                        .create_rectangle((57 + i * 3, 70, 60 + i * 3, 235), fill='red', outline='red', width=0)
                else:
                    self.__canvas.create_rectangle((57 + i * 3, 70, 60 + i * 3, 220), fill='black')

        self.__canvas.create_text(46, 240, font='* 16 bold', text=code[0])
        for i in range(13):
            if 1 <= i <= 6:
                self.__canvas.create_text(58 + i * 21, 240, font='* 16 bold', text=code[i])
            elif 7 <= i <= 12:
                self.__canvas.create_text(70 + i * 21, 240, font='* 16 bold', text=code[i])

        self.__canvas.create_text(200, 275, fill='darkred', font='* 16 bold', text=f'Check Digit: {code[-1]}')

    def run(self):
        self.__root.mainloop()