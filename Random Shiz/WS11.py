from tkinter import *

def number3():
    window = Tk()
    window.title('Counter with Lambda')

    counter = IntVar()
    counter.set(0)

    Button(window, text="Up", bg = "Yellow", command=lambda:counter.set(counter.get()+1)).pack()
    Button(window, text="Down", bg = "Cyan", command=lambda:counter.set(counter.get()-1)).pack()

    Label(window, bg="gray", textvariable=counter).pack()
    window.mainloop()

def abc(num):
    if num < 10:
        return num
    else:
        return abc(num%10 + num//10)

# def createIntList(a):
#     if isinstance(a[0], int):
#         print(a[0])
#     elif isinstance(a[0], list):
#         createIntList(a[0])
#
#     if len(a) > 1:
#         createIntList(a[1:])

# def createIntList(a):
#     if a == [] or len(a) == 1:
#         print(1, a)
#         return a
#     elif isinstance(a[0], int):
#         print(2, a)
#         return [a[0]] + createIntList(a[1:])
#     elif isinstance(a[0], list):
#         print(3, a)
#         return createIntList(a[0]) + createIntList(a[1:])

class TallyCounter:
    def __init__(self):
        window = Tk()
        window.title("Tally Counter")
        self.value = 0
        self.label = Label(window, text = "{:04d}".format(self.value))
        self.click = Button(window, text = "Click", bg = "cyan", command = self.inc)
        self.reset = Button(window, text = "Reset", bg = "yellow", command = self.zero)

        self.label.pack()
        self.click.pack()
        self.reset.pack()
        window.mainloop()

    def inc(self):
        self.value = (self.value + 1)%10000
        self.label["text"] = "{:04d}".format(self.value)

    def zero(self):
        self.value = 0
        self.label["text"] = "{:04d}".format(self.value)

print(createIntList([2, 4, [1, 2]]))