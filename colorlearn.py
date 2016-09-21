from Tkinter import *
import random
import tkFont

class Application(Frame):
    def __init__(self, master):
        #canvas / colored rectangle dimensions
        self.width = 1000
        self.height = 500
        #Actual color of the displayed rectangle (r,g,b)
        self.current_color = (0,0,0)

        #just a big font so things are bigger
        self.big_font = tkFont.Font(root=master,family='Helvetica',size=24)

        Frame.__init__(self, master)
        self.grid()
        self.generate()
        self.next_color()

    def next_color(self):
        """Change the color currently displayed"""
        self.current_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        self.w.create_rectangle(0,0,1000,500, fill='#%02x%02x%02x' % self.current_color)

    def submit(self):
        """Display the results: comparing user-entered values to actual color values"""

        r = int(self.r_in.get())
        g = int(self.g_in.get())
        b = int(self.b_in.get())

        self.out.delete(1.0, END)
        self.out.insert(END, "Actual Red:%i\n"%self.current_color[0])
        self.out.insert(END, "Actual Green:%i\n"%self.current_color[1])
        self.out.insert(END, "Actual Blue:%i\n"%self.current_color[2])

        diffsum = abs(self.current_color[0] - r) + abs(self.current_color[1] - g) + abs(self.current_color[2] - b)
        score = int(((765 - diffsum)/765.0)**2 * 100)
        self.out.insert(END, "Your Score:%i"%score)
            
    def generate(self):
        """Draw fields on the window"""

        #Canvas used to display the color rectangle
        self.w = Canvas(self, width=1000, height=500)
        self.w.grid(row=0, column=0, columnspan=4)

        Label(self, font=self.big_font, text="Red:").grid(row=1, column=0)
        self.r_in = Entry(self, font=self.big_font)
        self.r_in.grid(row=1, column=1)

        Label(self, font=self.big_font, text="Green:").grid(row=2, column=0)
        self.g_in = Entry(self, font=self.big_font)
        self.g_in.grid(row=2,column=1)

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
        self.out = Text(self, width=50, height=4, font=self.big_font)
        self.out.grid(row=5, column=0, columnspan=2)

root = Tk()
root.title("Learn RGB")
app = Application(root)
root.mainloop()