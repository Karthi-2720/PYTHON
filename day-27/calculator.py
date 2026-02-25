from tkinter import *
window = Tk()
window.title("Miles to Km")
window.maxsize(400, 400)
window.config(padx=30, pady=60)


input1 = Entry()
input1.insert(END, "0")
input1.grid(row=0, column=1)

label = Label(text="is equal to", font=("Arial", 20))
label.grid(row=1, column=0)

label2 = Label(text="Miles", font=("Arial", 20))
label2.grid(row=0, column=2)

label3 = Label(text="Km", font=("Arial", 20))
label3.grid(row=1, column=2)

label4 = Label(text="0", font=("Arial", 15))
label4.grid(row=1, column=1)

def action():
    mi = input1.get()
    km = (int(mi) * 1.6)
    label4.config(text=str(round(km)))

button = Button(text="calculate", command=action)
button.grid(row=2, column=1)




window.mainloop()