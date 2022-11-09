from tkinter import *
from tkinter import ttk

win = Tk()

win.geometry("500x300")

def sum_nums():
    sum = float(entry1.get()) + float(entry2.get())  # type: ignore
    entry3.insert(0, str(sum))  # type: ignore

def sub_nums():
    sub = float(entry1.get()) - float(entry2.get())
    entry3.insert(0, str(sub))  # type: ignore

def mult_nums():
    mult = float(entry1.get()) * float(entry2.get())
    entry3.insert(0, str(mult))

def div_nums():
    div = float(entry1.get()) / float(entry2.get())
    entry3.insert(0, str(div))

label1 = Label(win, text = "Enter first number: ")  # type: ignore
label1.pack()

entry1 = Entry(win, width = 40)  # type: ignore
entry1.focus_set()
entry1.pack()

label2 = Label(win, text = "Enter second number: ")  # type: ignore
label2.pack()

entry2 = Entry(win, width = 40)
entry2.focus_set()
entry2.pack()

label3 = Label(win, text = "Answer: ")
label3.pack()

entry3 = Entry(win, width = 40)
entry3.focus_set()
entry3.pack()

ttk.Button(win, text = "Sum numbers", width = 20, command = sum_nums).pack(pady = 10)
ttk.Button(win, text = "Subtract numbers", width = 20, command = sub_nums).pack(pady = 10)
ttk.Button(win, text = "Multiplicate numbers", width = 20, command = mult_nums).pack(pady = 10)
ttk.Button(win, text = "Divide numbers", width = 20, command = div_nums).pack(pady = 10)

win.mainloop()