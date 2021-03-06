#!/usr/bin/env python2

from Tkinter import *
from colorlib import to_hex, clamp_rgb, color_score
import random
import tkFont

class Application(Frame):
    def __init__(self, master):
        #(r, g, b) displayed to the user
        self.color_prompt = [0, 0, 0]

        # user-selected color
        self.color_response = [random.randint(0,255) for i in range(3)]

        #just a big font so things are bigger
        self.big_font = tkFont.Font(root=master, family='Helvetica', size=20)

        Frame.__init__(self, master)
        self.grid()
        self.generate()
        self.next_color()
        self.select_color(0,0)

    def next_color(self):
        """Change the current (r, g, b) prompt"""
        self.color_prompt = [random.randint(0,255) for i in range(3)]
        self.rgb_string.set("(R, G, B) = " + str(self.color_prompt))

    def submit(self):
        """Display the results: comparing user-entered values to actual color values"""
        self.prompt_canvas.create_rectangle(1, 20, 99, 99, fill=to_hex(tuple(self.color_prompt)))
        self.text_out.delete(1.0, END)
        self.text_out.insert(END, "You Entered:(%i, %i, %i)\n"%tuple(self.color_response))
        self.text_out.insert(END, "Your Score:%i"%color_score(self.color_prompt, self.color_response))


    def select_color(self, color, change):
        """ modify color_response
            0 = red, 1 = green, 2 = blue """
        self.color_response[color] = clamp_rgb(self.color_response[color]+change)
        self.answer_canvas.config(bg=to_hex(tuple(self.color_response)))

    def generate(self):
        """Draw fields on the window"""
        self.rgb_string = StringVar()
        self.rgb_text = Label(self, textvariable=self.rgb_string, font=self.big_font, fg="#000000")
        self.rgb_text.grid(row=0, column=0, columnspan=3, sticky=W)

        self.red_decrease = Button(self, text="<", font=self.big_font, command=lambda:self.select_color(0, -1), repeatdelay=200, repeatinterval=10)
        self.red_decrease.grid(row=1, column=0)
        Label(self, font=self.big_font, text="Red").grid(row=1, column=1, sticky=N)
        self.red_increase = Button(self, text=">", font=self.big_font, command=lambda:self.select_color(0, 1), repeatdelay=200, repeatinterval=10)
        self.red_increase.grid(row=1, column=2)

        self.green_decrease = Button(self, text="<", font=self.big_font, command=lambda:self.select_color(1, -1), repeatdelay=200, repeatinterval=10)
        self.green_decrease.grid(row=2, column=0)
        Label(self, font=self.big_font, text="Green").grid(row=2, column=1, sticky=N)
        self.green_increase = Button(self, text=">", font=self.big_font, command=lambda:self.select_color(1, 1), repeatdelay=200, repeatinterval=10)
        self.green_increase.grid(row=2, column=2)

        self.blue_decrease = Button(self, text="<", font=self.big_font, command=lambda:self.select_color(2, -1), repeatdelay=200, repeatinterval=10)
        self.blue_decrease.grid(row=3, column=0)
        Label(self, font=self.big_font, text="Blue").grid(row=3, column=1, sticky=N)
        self.blue_increase = Button(self, text=">", font=self.big_font, command=lambda:self.select_color(2, 1), repeatdelay=200, repeatinterval=10)
        self.blue_increase.grid(row=3, column=2)

        self.answer_canvas = Canvas(self, width=100, height=100)
        self.answer_canvas.grid(row=1, column=3, rowspan=3, columnspan=3)

        self.submit = Button(self, text="Submit", font=self.big_font, command = self.submit)
        self.submit.grid(row=4, column=0, columnspan=3)

        self.next = Button(self, text="Next Color", font=self.big_font, command=self.next_color)
        self.next.grid(row=5, column=0, columnspan=3)

        #Field to show the color the user was supposed to create
        self.prompt_canvas = Canvas(self, width=100, height=100)
        self.prompt_canvas.create_rectangle(1, 1, 100, 100)
        self.prompt_canvas.create_text(50, 1, text="Actual Color:", anchor=N)
        self.prompt_canvas.grid(row=4, column=3, rowspan=2, columnspan = 3)

        #Text output for scores
        self.text_out = Text(self, width="30", height=2, font=self.big_font)
        self.text_out.grid(row=6, column=0, columnspan=4)

root = Tk()
root.title("Learn RGB")
app = Application(root)
root.mainloop()
