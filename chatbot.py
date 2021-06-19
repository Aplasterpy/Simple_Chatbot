from tkinter import *
root = Tk()
root.configure(background= 'Black')

def send():
	send = "you -->> "+e.get()
	txt.insert(END, "\n" + send)

	if (e.get() == "Hi"):
		txt.insert(END,"\n"+"Jarvis -->> Hello ")
	elif (e.get() == "Hi"):
		txt.insert(END,"\n"+"Jarvis -->> How are You? ")
	elif (e.get() == "Hi"):
		txt.insert(END,"\n"+"Jarvis -->> How mau I help You? ")
	elif (e.get() == "I am fine"):
		txt.insert(END,"\n"+"Jarvis -->> Great ")
	elif (e.get() == "Where are you from"):
		txt.insert(END,"\n"+"Jarvis -->> I am from USA ")
	elif (e.get() == "How many years old?"):
		txt.insert(END,"\n"+"Jarvis -->> I am 30 years old ")
	elif (e.get() == "Do you know Python?"):
		txt.insert(END,"\n"+"Jarvis -->> Yes Python is a programming Lnaguage ")
	elif (e.get() == "Okay, Bye"):
		txt.insert(END,"\n"+"Jarvis -->> Bye.. ")
	else:
		txt.insert(END,"\n"+"Jarvis -->> Sorry I did't get You..")

	e.delete(0,END)



txt = Text(root)
txt.grid(row = 0, column = 0, columnspan = 3)

e = Entry(root,width = 100)
send = Button (root,text="SEND", command=send).grid(row = 1 , column = 1)
e.grid(row = 1, column = 0)
root.title("Jarvis")

root.mainloop()