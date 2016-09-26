#!/usr/bin/env python2

from Tkinter import *
import random
import tkFont

def to_hex(rgb):
    """Change an (r, g, b) tuple to a tkinter-compatible hex string"""
    return '#%02x%02x%02x' % rgb
def clamp_rgb(num):
    """Limit inputs to between 0 and 255"""
    return max(0, min(num, 255))

class Application(Frame):
    def __init__(self, master):
        #canvas / colored rectangle dimensions
        self.width =  800
        self.height = 300
        #answer rectangle dimenstions
        self.ans_width = 120
        self.ans_height= 120
        #Actual color of the displayed rectangle (r, g, b)
        self.current_color = (0, 0, 0)

        #just a big font so things are bigger
        self.big_font = tkFont.Font(root=master, family='Helvetica', size=20)

        Frame.__init__(self, master)
        self.grid()
        self.generate()
        self.next_color()

    def next_color(self):
        """Change the color currently displayed"""
        self.current_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.color_canvas.create_rectangle(0, 0, self.width, self.height, fill=to_hex(self.current_color))

    def submit(self):
        """Display the results: comparing user-entered values to actual color values"""

        r = clamp_rgb(int(self.r_in.get()))
        g = clamp_rgb(int(self.g_in.get()))
        b = clamp_rgb(int(self.b_in.get()))

        self.out.delete(1.0, END)
        self.out.insert(END, "Actual Red:%i\n"%self.current_color[0])
        self.out.insert(END, "Actual Green:%i\n"%self.current_color[1])
        self.out.insert(END, "Actual Blue:%i\n"%self.current_color[2])

        diffsum = abs(self.current_color[0] - r) + abs(self.current_color[1] - g) + abs(self.current_color[2] - b)
        score = int(((765 - diffsum)/765.0)**2 * 100)
        self.out.insert(END, "Your Score:%i"%score)

        #Show the user what their answer was
        self.answer_canvas.create_rectangle(1, 20, self.ans_width-1, self.ans_height-1, fill=to_hex((r, g, b)))


    def generate(self):
        """Draw fields on the window"""

        #Canvas used to display the color rectangle
        self.color_canvas = Canvas(self, width=self.width, height=self.height)
        self.color_canvas.grid(row=0, column=0, columnspan=4)


        Label(self, font=self.big_font, text="Red:").grid(row=1, column=0)
        self.r_in = Entry(self, font=self.big_font)
        self.r_in.grid(row=1, column=1)

        Label(self, font=self.big_font, text="Green:").grid(row=2, column=0)
        self.g_in = Entry(self, font=self.big_font)
        self.g_in.grid(row=2, column=1)

        Label(self, font=self.big_font, text="Blue:").grid(row=3, column=0)
        self.b_in = Entry(self, font=self.big_font)
        self.b_in.grid(row=3, column=1)

        self.btn_submit = Button(self, font=self.big_font, text="Submit!", command=self.submit)
        self.btn_submit.grid(row=4, column=1)
        self.btn_submit.bind('<Return>', lambda x:self.submit())

        self.btn_color = Button(self, font=self.big_font, text="Next Color", command=self.next_color)
        self.btn_color.grid(row=4, column=0)
        #Automatically select the first color input if user hits enter while "next color" is active
        self.btn_color.bind('<Return>', lambda x:[self.next_color(), self.r_in.focus()])

        #The text output section - display scores and results
        self.out = Text(self, width=40, height=4, font=self.big_font)
        self.out.grid(row=5, column=0, columnspan=2)

        #Field to show the color that the user entered
        self.answer_canvas = Canvas(self, width=self.ans_width, height=self.ans_height)
        self.answer_canvas.create_rectangle(1, 1, self.ans_width, self.ans_height)
        self.answer_canvas.create_text(self.ans_width/2, 1, text="Your Answer:", anchor=N)
        self.answer_canvas.grid(row=5, column=2)

root = Tk()
root.title("Learn RGB")
root.resizable(0, 0)
app = Application(root)
root.mainloop()
