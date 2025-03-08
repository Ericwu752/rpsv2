from tkinter import *
import random

root = Tk()
root.geometry("300x300")
root.title("Rock Paper Scissor Game")

Computer = {
     "1" : "Rock",
     "2" : "Paper",
     "3" : "Scissor"
}

def button_disable():
     b1["state"] = "disable"
     b2["state"] = "disable"
     b3["state"] = "disable"


def chooseRock():
      c_v = Computer[str(random.randint(1, 3))]
      if c_v == "Rock":
          result = "Draw"
      elif c_v == "Paper":
          result = 'Computer Wins'
      else:
            result = 'You Win'
      l4.config(text=result)
      l1.config(text="Rock            ")
      l3.config(text=c_v)
      button_disable()

def choosePaper():
      c_v = Computer[str(random.randint(1, 3))]
      if c_v == "Rock":
          result = "You Win"
      elif c_v == "Paper":
          result = 'Draw'
      else:
            result = 'Computer Wins'
      l4.config(text=result)
      l1.config(text="Paper            ")
      l3.config(text=c_v)
      button_disable()

def chooseScissor():
      c_v = Computer[str(random.randint(1, 3))]
      if c_v == "Rock":
          result = "Computer Wins"
      elif c_v == "Paper":
          result = 'You Win'
      else:
            result = 'Draw'
      l4.config(text=result)
      l1.config(text="Paper            ")
      l3.config(text=c_v)
      button_disable()


def reset_game():
    b1["state"] = "active"
    b2["state"] = "active"
    b3["state"] = "active"
    l1.config(text="Player              ")
    l3.config(text="Computer")
    l4.config(text="")

Label(root,
      text="Rock Paper Scissor",
      font="normal 20 bold",
      fg="blue").pack(pady=20)
 
frame = Frame(root)
frame.pack()
 
l1 = Label(frame,
           text="Player              ",
           font=10)
 
l2 = Label(frame,
           text="VS             ",
           font="normal 10 bold")
 
l3 = Label(frame, text="Computer", font=10)
 
l1.pack(side=LEFT)
l2.pack(side=LEFT)
l3.pack()

l4  = Label(root, 
            text = "",
            font="normal 20 bold",
            bg="white",
            width=15,
            borderwidth=2,
            relief="solid")
l4.pack(pady=20)


frame1 = Frame(root)
frame1.pack()

b1 = Button(frame1, text = "Rock", font = 10, width = 7, command = chooseRock)
b2 = Button(frame1, text = "Paper", font = 10, width = 7, command = chooseRock)
b3 = Button(frame1, text = "Scissor", font = 10, width = 7, command = chooseRock)
b1.pack(side=LEFT, padx = 10)
b2.pack(side=LEFT, padx = 10)
b3.pack(side=RIGHT, padx = 10)

Button(root, text = "Reset", command = reset_game).pack(pady = 20)
root.mainloop()