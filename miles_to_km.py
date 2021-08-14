from tkinter import *

km = 0


def button_clicked():
    miles = input.get()
    km = float(miles)*1.6
    answer.config(text=int(km))


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

is_equal = Label(text="is equal to")
is_equal.grid(column=0, row=1)

miles = Label(text="Miles")
miles.grid(column=2, row=0)

Km = Label(text="Km")
Km.grid(column=2, row=1)

answer = Label(text="0")
answer.grid(column=1, row=1)

input = Entry(width=10)
input.grid(column=1, row=0)

calculate = Button(text="Calculate", command=button_clicked)
calculate.grid(column=1, row=3)


window.mainloop()
