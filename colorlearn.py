#!/usr/bin/env python2

from Tkinter import *
from colorlib import *
import random
import tkFont

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
        self.grid(sticky=(E, W, S, N))

        master.columnconfigure(0, weight=1)
        master.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.mode = StringVar() #format for representing colors: INT/HEX
        self.generate()
        self.next_color()


    def next_color(self):
        """Change the color currently displayed"""
        self.current_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.color_canvas.config(bg=to_hex(self.current_color))


    def submit(self):
        """Display the results: comparing user-entered values to actual color values"""

        if self.mode.get() == "INT":
            # string to int
            def convert(s): return float(s)
            # int to string
            def fmt(color): return str(color)
        else:
            # "HEX" mode
            # convert a hex string to an integer ("a" -> 10)
            def convert(s): return int(s, 16)
            # Format integers as hex strings (10 -> "0a")
            def fmt(color): return hex(color)[2:].zfill(2)

        try:
            r = convert(self.r_in.get())
        except:
            r = 0
        try:
            g = convert(self.g_in.get())
        except:
            g = 0
        try:
            b = convert(self.b_in.get())
        except:
            b = 0

        r = clamp_rgb(r)
        g = clamp_rgb(g)
        b = clamp_rgb(b)

        

        self.r_in.delete(0,END)
        self.r_in.insert(0, fmt(r))
        self.g_in.delete(0,END)
        self.g_in.insert(0, fmt(g))
        self.b_in.delete(0,END)
        self.b_in.insert(0, fmt(b))

        # Show results in output Text box
        self.out.delete(1.0, END)
        if self.mode.get() == "INT":
            self.out.insert(END, "Actual Red    : %i\n"%self.current_color[0])
            self.out.insert(END, "Actual Green: %i\n"%self.current_color[1])
            self.out.insert(END, "Actual Blue   : %i\n"%self.current_color[2])
        else: # "HEX" mode
            self.out.insert(END, "Actual Red    : #%s\n"%fmt(self.current_color[0]))
            self.out.insert(END, "Actual Green: #%s\n"%fmt(self.current_color[1]))
            self.out.insert(END, "Actual Blue   : #%s\n"%fmt(self.current_color[2]))

        score = color_score(self.current_color, (r,g,b))
        self.out.insert(END, "Your Score: %i"%score)

        #Show the user what their answer was
        self.answer_canvas.create_rectangle(1, 20, self.ans_width-1, self.ans_height-1, fill=to_hex((r, g, b)))

    def generate(self):
        """Draw fields on the window"""

        #Canvas used to display the color rectangle
        self.color_canvas = Canvas(self)
        self.color_canvas.grid(row=0, column=0, columnspan=3, sticky=(E, W, S, N))

        self.content = Frame(self, pady=10)
        self.content.grid(sticky=N)

        Label(self.content, font=self.big_font, text="Red:").grid(row=1, column=0)
        self.r_in = Entry(self.content, font=self.big_font)
        self.r_in.grid(row=1, column=1)

        Label(self.content, font=self.big_font, text="Green:").grid(row=2, column=0)
        self.g_in = Entry(self.content, font=self.big_font)
        self.g_in.grid(row=2, column=1)

        Label(self.content, font=self.big_font, text="Blue:").grid(row=3, column=0)
        self.b_in = Entry(self.content, font=self.big_font)
        self.b_in.grid(row=3, column=1)

        Label(self.content,text="Representation:").grid(row=1, column=2, sticky=S)
        self.select_int = Radiobutton(self.content, text="Int", variable=self.mode, value="INT", takefocus=False)
        self.select_hex = Radiobutton(self.content, text="Hex", variable=self.mode, value="HEX", takefocus=False)
        self.select_int.select()
        self.select_int.grid(row=2, column=2, sticky=W)
        self.select_hex.grid(row=3, column=2, sticky=NW)

        self.btn_submit = Button(self.content, font=self.big_font, text="Submit!", command=self.submit)
        self.btn_submit.grid(row=4, column=1)
        self.btn_submit.bind('<Return>', lambda x:self.submit())

        self.btn_color = Button(self.content, font=self.big_font, text="Next Color", command=self.next_color)
        self.btn_color.grid(row=4, column=0)
        #Automatically select the first color input if user hits enter while "next color" is active
        self.btn_color.bind('<Return>', lambda x:[self.next_color(), self.r_in.focus()])

        #The text output section - display scores and results
        self.out = Text(self.content, width=40, height=4, font=self.big_font, takefocus=False)
        self.out.grid(row=5, column=0, columnspan=2)

        #Field to show the color that the user entered
        self.answer_canvas = Canvas(self.content, width=self.ans_width, height=self.ans_height)
        self.answer_canvas.create_rectangle(1, 1, self.ans_width, self.ans_height)
        self.answer_canvas.create_text(self.ans_width/2, 1, text="Your Answer:", anchor=N)
        self.answer_canvas.grid(row=5, column=2)

root = Tk()
root.title("Learn RGB")
app = Application(root)
root.mainloop()
