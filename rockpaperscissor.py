from tkinter import *
import random
f=Tk()
f.title("Rock Paper scissor game for CodSoft")
f.geometry("760x180")
f.configure(bg="#16F529")
def name():
	pass
def score(aug):
	if aug=="Rock":
		player=1
	elif aug=="Paper":
		player=2
	elif aug=="Scissor":
		player=3
	computer=random.randint(1,3)
	if computer==1:
		com="Rock"
	elif computer==2:
		com="Paper"
	elif computer==3:
		com="Scissor"
	comchoice.set(com)
	if player==1:
		if computer==2:
			s="computer won"
		elif computer==3:
			s="you won"
		else:
			s="Tie"
	if player==2:
		if computer==1:
			s="you won"
		elif computer==3:
			s="computer won"
		else:
			s="Tie"
	if player==3:
		if computer==1:
			s="Computer won"
		elif computer==2:
			s="You won"
		else:
			s="Tie"
	point.set(s)


l1=Label(f,bg="#800080",fg="white",text="      ROCK-PAPER-SCISSOR     Game    ",width="40")
l1.grid(row=0,column=0)

l2=Label(f,bg="#00FFFF",fg="black",text="  ENTER YOUR CHOICE :",width="17")
l2.grid(row=2,column=0)

b1=Button(f,text="Rock",bg="#DAEE01",width="8",fg="black",command=lambda:score("Rock"))
b1.grid(row=2,column=4)

b2=Button(f,text="Paper",bg="#DAEE01",width="8",fg="black",command=lambda:score("Paper"))
b2.grid(row=2,column=5)

b3=Button(f,text="Scissor",bg="#DAEE01",width="8",fg="black",command=lambda:score("Scissor"))
b3.grid(row=2,column=6)

l3=Label(f,bg="#00FFFF",fg="black",text="Computer choice :")
l3.grid(row=6,column=4)
comchoice=StringVar()
e1=Entry(f,bg="lightpink",fg="black",textvariable=comchoice)
e1.grid(row=6,column=5)

point=StringVar()
e1=Entry(f,bg="lightpink",fg="black",textvariable=point)
e1.grid(row=7,column=5)

f.mainloop()