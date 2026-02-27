from json import JSONDecodeError
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    p_l = [choice(letters) for _ in range(randint(8, 10))]
    p_s = [choice(symbols) for _ in range(randint(2, 4))]
    p_n = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = p_l + p_s + p_n
    shuffle(password_list)
    password = "".join(password_list)
    entry3.delete(0, "end")
    entry3.insert(0, f"{password}")
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    is_it_ok = False
    new_dist = {
        entry1.get():{
            "email": entry2.get(),
            "password": entry3.get(),
        }
    }

    if entry1.get() == "" or entry2.get() == "example@gmail.com" or entry3.get() == "":
        if entry2.get() == "example@gmail.com":
            messagebox.showerror(" Oops", "Change the Email/Username")
        else:
            messagebox.showerror("Error", "Please enter all fields")
    else:
        messagebox.askokcancel(title=entry1.get(),  message=f"your Email: {entry2.get()}\nyour Password:"
                                                                   f" {entry3.get()}\n is it ok for you")
        is_it_ok = True
    if is_it_ok:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_dist, file, indent=4)
        else:
            data.update(new_dist)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            entry1.delete(0, "end")
            entry2.delete(0, "end")
            entry2.insert(0,"example@gmail.com")
            entry3.delete(0, "end")
            entry1.focus()

def search_account():
    user = entry1.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror("Error", "No data found")
    else:
        if user in data:
            messagebox.showinfo(title="website", message=f"Email/Username: {data[user]['email']} \nPassword: {data[user]['password']}")
        else:
            messagebox.showerror("Error", "Account not found")
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=0, columnspan=3)

text1 = Label(text="Website:")
text1.grid(row=1, column=0)
text2 = Label(text="Email/Username:")
text2.grid(row=2, column=0)
text3 = Label(text="Password:")
text3.grid(row=3, column=0)


entry1 = Entry(width=21)
entry1.grid(row=1, column=1)
entry1.focus()
entry2 = Entry(width=35)
entry2.grid(row=2, column=1, columnspan=2)
entry2.insert(0, "example@gmail.com")
entry3 = Entry(width=21)
entry3.grid(row=3, column=1)

button_search = Button(text="Search", width=15, command=search_account)
button_search.grid(row=1, column=2)
button_generate = Button(text="Generate Password", command=pass_generate)
button_generate.grid(row=3, column=2)
button_add = Button(text="Add", width=36, command=save)
button_add.grid(row=4, column=1, columnspan=2)

window.mainloop()