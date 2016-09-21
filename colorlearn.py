from Tkinter import *
import random
import tkFont

master = Tk()

#just a big font so things are bigger
big_font = tkFont.Font(root=master,family='Helvetica',size=24)

#Actual color of the displayed rectangle
current_red = 0
current_green = 0
current_blue = 0

def next_color(change_focus=0):
	global current_red, current_green, current_blue
	current_red = random.randint(0,255)
	current_green = random.randint(0,255)
	current_blue = random.randint(0,255)
	w.create_rectangle(0,0,1000,500, fill='#%02x%02x%02x' % (current_red, current_green, current_blue))
	if change_focus:
		r_in.focus()

def submit():
	"""Display the results: comparing user-entered values to actual color values"""
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

#Canvas used to display the color rectangle
w = Canvas(master, width=1000, height=500)
w.grid(row=0, column=0, columnspan=4)

Label(master, font=big_font, text="Red:").grid(row=1, column=0)
r_in = Entry(master, font=big_font)
r_in.grid(row=1, column=1)

Label(master, font=big_font, text="Green:").grid(row=2, column=0)
g_in = Entry(master, font=big_font)
g_in.grid(row=2,column=1)

Label(master, font=big_font, text="Blue:").grid(row=3, column=0)
b_in = Entry(master, font=big_font)
b_in.grid(row=3, column=1)

btn_submit = Button(master, font=big_font, text="Submit!", command=submit)
btn_submit.grid(row=4, column=1)
btn_submit.bind('<Return>', lambda x:submit())

btn_color = Button(master, font=big_font, text="Next Color", command=next_color)
btn_color.grid(row=4, column=0)
#Automatically select the first color input if user hits enter while "next color" is active
btn_color.bind('<Return>', lambda x:next_color(change_focus=1))

#The text output section - display scores and results
out = Text(master, width=50, height=4, font=big_font)
out.grid(row=5, column=0, columnspan=2)

next_color()
mainloop()