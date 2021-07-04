from tkinter import Tk, Canvas, Frame, Button, Label, TOP, BOTTOM, BOTH, LEFT
from tkinter.colorchooser import askcolor
class Scribble(object):
    '''a simple pen drawing application'''

    def __init__(self):

        master = Tk()
        master.title("Simple Pen (Finger) Scribble")

        # mouse coordinates and the drawing color are instance variables
        self.oldx, self.oldy = 0, 0
        self.color = 'green'

        # create canvas 400X250 and bind mouse events to handlers
        self.canvas = Canvas(master, width=400, height=250)
        self.canvas.bind("<Button-1>", self.begin)
        self.canvas.bind("<Button1-Motion>", self.draw)
        
        self.canvas.pack(expand=True, fill=BOTH)

        # create a new frame for holding the buttons
        frame1 = Frame(master)
        frame1.pack(side=TOP)
        
        self.bt_clear = Button(frame1, text='Clear', command=self.delete, bg="orange")
        self.bt_clear.pack(side=LEFT, padx=5)
        
        self.bt_color = Button(frame1, text='Color', command=self.change_color, bg=self.color)
        self.bt_color.pack(side=LEFT)


        self.message = Label(master, text='Press and drag the left mouse-button to draw', fg="blue")
        self.message.pack( side = BOTTOM )

        # start the event loop
        master.mainloop()

    def begin(self, event):
        '''handles left button click by recording mouse position
           as the start of the curve'''
        self.oldx, self.oldy = event.x, event.y


    def draw(self, event):
        '''handles mouse motion, while pressing left button, by
           connecting the previous mouse position to the new one'''
        self.canvas.create_line((self.oldx, self.oldy, event.x, event.y), fill=self.color)
        self.oldx, self.oldy = event.x, event.y

    def delete(self):
        '''clear the canvas'''
        self.canvas.delete('all')   
          
    def change_color(self):
        '''change the drawing color using the color chooser,
           also change the background color of the color button'''
        self.color = askcolor()[-1] #get the hex value from the color chooser
        self.bt_color["bg"] = self.color

if __name__ == "__main__":
    Scribble()
