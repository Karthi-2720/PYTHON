from tkinter import *
import random
import pandas
import time

data = pandas.read_csv("data/french_words.csv")
learn = data.to_dict(orient="records")
print(learn)
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
def button_click():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(learn)
    canvas.itemconfig(French_page, text=current_card["French"])
    canvas.itemconfig(front_img, image=img)
    canvas.itemconfig(Title_page, text="French")
    flip_timer = window.after(3000, func=button_click2)

def button_click2():
    canvas.itemconfig(Title_page, text="English")
    canvas.itemconfig(French_page, text=current_card["English"])
    canvas.itemconfig(front_img, image= img2)

window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=button_click2)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
img = PhotoImage(file = "./images/card_front.png")
img2 = PhotoImage(file="./images/card_back.png")
front_img = canvas.create_image(400,263, image=img)
canvas.grid(row=0, column=0, columnspan=2)
Title_page = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
French_page = canvas.create_text(400, 263, text="word", font=("Arial", 68, "bold"))
right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")
button1 = Button(image=right, highlightthickness=0, command=button_click)
button1.grid(row=1, column=1)
button2 = Button(image=wrong, highlightthickness=0, command=button_click)
button2.grid(row=1, column=0)
button_click()

window.mainloop()

