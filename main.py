import random
from tkinter import *
import pandas
BACKGROUND_COLOR = "#B1DDC6"
to_learn={}
current_card={}
try:
    data= pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    file = pandas.read_csv("data/french_words.csv")
    to_learn=file.to_dict(orient="records")
else:
    to_learn= data.to_dict(orient="records")

def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word,text=current_card["French"], fill="black")
    canvas.itemconfig(front_img,image=log_img)
    flip_timer=window.after(3000,func=card_back)
def card_back():
    canvas.itemconfig(title,  text="English",fill="white")
    canvas.itemconfig(word, text=current_card["English"],fill="white")
    canvas.itemconfig(front_img,image=back_img)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50)
window.config(bg=f"{BACKGROUND_COLOR}")
flip_timer=window.after(3000,func=card_back)

canvas = Canvas(width=800, height=526,highlightthickness=0)
back_img= PhotoImage(file="images/card_back.png")
log_img = PhotoImage(file="images/card_front.png")
front_img=canvas.create_image(400,263, image=log_img)

title=canvas.create_text(400,150,text="", font=("Ariel",40,"italic"))
word=canvas.create_text(400,263,text="", font=("Ariel",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(column=0,row=0,columnspan=2)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button= Button(image=wrong_img,highlightthickness=0,command=next_card)
wrong_button.grid(column=0,row=1)

correct_img = PhotoImage(file="images/right.png")
right_button = Button(image=correct_img,highlightthickness=0,command=is_known)
right_button.grid(row=1,column=1)
next_card()

window.mainloop()