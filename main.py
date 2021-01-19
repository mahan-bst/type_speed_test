from tkinter import *
import random
import time

counter = 0
start_time = 0
with open("sentence.txt") as f:
	content = f.readlines()
sentence = random.choice(content)[:-1]



window = Tk()
window.geometry("500x500")

def get_input(event):
	global counter
	global start_time
	keypress = event.keysym

	if keypress == "space": keypress = " "
	if keypress == "quoteleft": keypress = "'"
	if keypress == "question": keypress = "?"
	if keypress == "exclam": keypress = "!"
	if keypress == "period": keypress = "."
	if keypress == "comma": keypress = ","

	if keypress == sentence[counter]:
		if counter == 0:
			start_time = time.time()


		if counter+1 == len(sentence):
			final_time = time.time() - start_time
			wps = len(sentence.split()) / final_time
			res = Label(window, text="nice, your time = " + str(round(final_time, 2))+" S and wps = " + str(round(wps, 2)))
			res.place(rely=.9)

		lbl.tag_add("start", "1.0", f"1.{counter+1}")
		lbl.tag_config("start", background="black", foreground="yellow")
		counter += 1



window.bind("<Key>", get_input)

lbl = Text(window, font=(None, 13), height=5, width=40)
lbl.place(relx=.5, anchor="n")
lbl.insert(INSERT, sentence)
lbl.config(state=DISABLED)


window.mainloop()