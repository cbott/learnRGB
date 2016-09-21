from Tkinter import *
import random
import tkFont

master = Tk()
helv36 = tkFont.Font(root=master,family='Helvetica',size=24)

current_red = 0
current_green = 0
current_blue = 0

def next_color():
	global current_red, current_green, current_blue
	current_red = random.randint(0,255)
	current_green = random.randint(0,255)
	current_blue = random.randint(0,255)
	w.create_rectangle(0,0,1000,500, fill='#%02x%02x%02x' % (current_red, current_green, current_blue))

def submit():
	global current_red, current_green, current_blue

	r = int(r_in.get())
	g = int(g_in.get())
	b = int(b_in.get())

	out.delete(1.0, END)
	out.insert(END, "Actual Red:%i\n"%current_red)
	out.insert(END, "Actual Green:%i\n"%current_green)
	out.insert(END, "Actual Blue:%i\n"%current_blue)

	score = int(((765 - abs(current_red - r) - abs(current_green - g) - abs(current_blue - b))/765.0)**2 * 100)
	out.insert(END, "Your Score:%i"%score)

w = Canvas(master, width=1000, height=500)
w.grid(row=0, column=0, columnspan=4)

Label(master, text="Red:").grid(row=1, column=0)
r_in = Entry(master)
r_in.grid(row=1, column=1)

Label(master, text="Green:").grid(row=2, column=0)
g_in = Entry(master)
g_in.grid(row=2,column=1)

Label(master, text="Blue:").grid(row=3, column=0)
b_in = Entry(master)
b_in.grid(row=3, column=1)

btn = Button(master, text="Submit!", command=submit)
btn.grid(row=4, column=1)

btn = Button(master, text="Next Color", command=next_color)
btn.grid(row=4, column=0)

out = Text(master, width=50, height=4, font=helv36)
out.grid(row=5, column=0, columnspan=2)

next_color()
mainloop()