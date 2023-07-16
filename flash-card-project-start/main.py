import tkinter
from tkinter import *
import random
import pandas
import time

select = {}  # chosen vocab starts with empty dict to globalize and for collection
BACKGROUND_COLOR = "#B1DDC6"
question = {}


def clear():
    timeprompt.config(text="")
    timeprompt.place(x=1000, y=1000)
    countselection.place(x=1000, y=1000)
    countdown(int(countselection.get()))

    canvas.itemconfig(bkgd, image=frontside)  # flip card's color
    canvas.itemconfig(title, text="Question", font=("Ariel", 60, "italic"))
    if len(question) > 25:
        canvas.itemconfig(word, text=question, font=("Ariel", 30, "bold"), width=600)
    else:
        canvas.itemconfig(word, text=question,  font=("Ariel", 35, "bold"))


def countdown(count):
    # print(count)
    clock = reveallabel.config(text=count)  # change reveallabel text from "" to the count
    reveallabel.place(x=805, y=625)  # where to position the count on the app
    if count > 0:
        clock
        revealbutton.place(x=1000, y=1000)
        windows.after(1000, countdown, count - 1)
    if count == 0:
        reveallabel.config(text="")
        revealbutton.place(x=755, y=625)


def englishside():  # Flips Card
    if len(select["Answer"]) > 25:  # if the answer is too long, reformat size/width so it'll fit
        canvas.itemconfig(word, text=select["Answer"], font=("Ariel", 30, "bold"), width=600)
    else:
        canvas.itemconfig(word, text=select["Answer"])
    canvas.itemconfig(title, text="Answer")
    canvas.itemconfig(bkgd, image=backside)


def newcard():
    global select, question
    data = pandas.read_csv("data/ITquestions.csv")  # create df
    datalist = data.to_dict(orient="records")  # turn into list of dicts
    select = random.choice(datalist)  # pick a word/dict; goes into empty dict
    question = select["Question"]  # get the IT question & def
    # print(select)
    clear()


windows = Tk()
windows.title("Flashy")
windows.config(padx=50, pady=50, background=BACKGROUND_COLOR)

# IMAGES
canvas = Canvas(width=800, height=620, background=BACKGROUND_COLOR, highlightthickness=0)
frontside = PhotoImage(file="images/card_front.png")
backside = PhotoImage(file="images/card_back.png")
bkgd = canvas.create_image(400, 264, image=frontside)
canvas.grid(column=0, row=0, columnspan=2)

# TEXT/TITLE
title = canvas.create_text(400, 175, text="Press The Button To Start", font=("Ariel", 45, "italic"), fill="black")
word = canvas.create_text(400, 325, text="", font=("Ariel", 35, "bold"), fill="black")
canvas.grid(column=0, row=0)

# LABEL
reveallabel = Label(text="", font=("Ariel", 20, "normal"), fg="black", bg=BACKGROUND_COLOR)
reveallabel.place(x=785, y=650)

timeprompt = Label(text="Pick the time to reveal the answer: ", font=("Ariel", 25, "normal"), fg="black", bg="white")
timeprompt.place(x=165, y=300)

# SPINBOX
countselection = Spinbox(width=5, bg="white", from_=3, to=10, fg="black",
                         highlightthickness=0, highlightbackground="white", wrap=True)
countselection.place(x=545, y=310)

# BUTTONS
green = Button()
correctbutton = PhotoImage(file="images/right.png")
green.config(image=correctbutton, highlightbackground=BACKGROUND_COLOR, command=newcard)
green.place(x=350, y=525)

revealbutton = Button(text="Reveal", highlightbackground=BACKGROUND_COLOR, command=englishside)

windows.mainloop()
