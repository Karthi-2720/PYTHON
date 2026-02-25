from tkinter import *
window = Tk()
window.title("My first GUI")
window.minsize(600, 800)
window.config(padx=30, pady=20)

tk_label = Label(window, text="My first GUI", font=("Arial", 25, "bold"))
tk_label.grid(row=0, column=0)
 

def button():
    print("Button pressed")
    input = enter.get()
    tk_label.config(text=input)

tk_label.config(text="karthiekya")
button = Button(text= "Click me", command=button)
button1 = Button(text= "Click me")
button.grid(row=1, column=1)
button1.grid(row=0, column=3)


enter = Entry(width=35, bd=10)
enter.grid(row=2, column=4)





mainloop()