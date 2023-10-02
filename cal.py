"""
CALCULATOR using python by tkinter,for
CODESOFT INTERNSHIP
"""
#importing tkinter
from tkinter import *
#creating a window for tkinter
win=Tk()
#setting its size
win.configure(bg="#E799A3")
win.geometry("1000x325")
#giving title to window
win.title("CALCULATOR FOR CODESOFT INTERNSHIP")
#initializing the expression as none
exp=" "
#defining the functions
def clicknum(num):
    """ for typing expression on text box"""
    global exp
    exp = exp + str(num)
    eq.set(exp)
def cal():
    """ for calculating the expression and
     setting the result of expression
      in textbox (which is bottom)
      if we press '=' button
    """
    try:
        global exp
        eq=str(eval(exp))
        result.set(eq)
    except:
        result.set("enter valid calculation")
def clear():
    """ for clearing the expression and textbox,
     after clicking 'c' button"""
    global exp
    exp=" "
    eq.set(exp)
    result.set(exp)
""" creating buttons and text fields for our calculator"""
eq=StringVar()
e1=Entry(win,width="55",font="7",textvariable=eq,bg="#F6358A",fg="white")
e1.grid(row=1,column=1,columnspan=4,ipadx=75)
b1=Button(win,text="1",width="7",bg="#E30B5D",fg="white",command=lambda:clicknum(1))
b1.grid(row=2,column=0)
badd=Button(win,text="+",width="7",bg="#A74AC7",fg="white",command=lambda:clicknum("+"))
badd.grid(row=2,column=3)
b2=Button(win,text="2",width="7",bg="#E30B5D",fg="white",command=lambda:clicknum(2))
b2.grid(row=2,column=1)
b3=Button(win,text="3",width="7",bg="#E30B5D",fg="white",command=lambda:clicknum(3))
b3.grid(row=2,column=2)
b4=Button(win,text="4",width="7",bg="#E30B5D",fg="white",command=lambda:clicknum(4))
b4.grid(row=3,column=0)
bsub=Button(win,text="-",width="7",bg="#A74AC7",fg="white",command=lambda:clicknum("-"))
bsub.grid(row=3,column=3)
b5=Button(win,text="5",width="7",bg="#E30B5D",fg="white",command=lambda:clicknum(5))
b5.grid(row=3,column=1)
b6=Button(win,text="6",width="7",bg="#E30B5D",fg="white",command=lambda:clicknum(6))
b6.grid(row=3,column=2)
b7=Button(win,text="7",width="7",bg="#E30B5D",fg="white",command=lambda:clicknum(7))
b7.grid(row=4,column=0)
bmul=Button(win,text="x",width="7",bg="#A74AC7",fg="white",command=lambda:clicknum("*"))
bmul.grid(row=4,column=3)
b8=Button(win,text="8",width="7",bg="#E30B5D",fg="white",command=lambda:clicknum(8))
b8.grid(row=4,column=1)
b9=Button(win,text="9",width="7",bg="#E30B5D",fg="white",command=lambda:clicknum(9))
b9.grid(row=4,column=2)
b0=Button(win,text="0",width="7",bg="#E30B5D",fg="white",command=lambda:clicknum(0))
b0.grid(row=5,column=0)
bdiv=Button(win,text="/",width="7",bg="#A74AC7",fg="white",command=lambda:clicknum("/"))
bdiv.grid(row=5,column=3)
bdot=Button(win,text=".",width="10",bg="#8B008B",fg="white",command=lambda:clicknum("."))
bdot.grid(row=5,column=1)
bpow=Button(win,text="^",width="7",bg="#A74AC7",fg="white",command=lambda:clicknum("**"))
bpow.grid(row=5,column=2)
sub=Button(win,text="=",width="20",bg="#483D8B",fg="white",command=cal)
sub.grid(row=7,column=0)
l1=Label(win,width="10",font="50",bg="#9D00FF",fg="white",text="RESULT      :")
l1.grid(row=10,column=0)
result=StringVar()
e2=Entry(win,width="20",font="50",textvariable=result,bg="#FF00FF",fg="white")
e2.grid(row=10,column=1)
brac1=Button(win,text="(",width="10",bg="#8B008B",fg="white",command=lambda:clicknum("("))
brac1.grid(row=6,column=0)
brac2=Button(win,text=")",width="10",bg="#8B008B",fg="white",command=lambda:clicknum(")"))
brac2.grid(row=6,column=1)
c=Button(win,text="C",width="15",command=clear,bg="#FCDFFF",fg="#3A3B3C")
c.grid(row=11,column=0)
#for
win.mainloop()