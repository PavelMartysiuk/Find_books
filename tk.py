from tkinter import *
from tkinter import messagebox
from os import listdir
from collections import defaultdict
import book_for_tk

''' ПРиложение'''
def show_books():
    m = message.get().split(',')
    messagebox.showinfo('Books',book_for_tk.findbooks(m))
def save_dict():
    book_for_tk.helpy(message.get())
 
root = Tk()
root.title("Find book")
root.geometry("500x500")
 
btn = Button(root,text="Find book", background = 'red', command = show_books)
btn.place(relx=.5, rely=.5, anchor="c")
btn2 = Button(root,text="Find folder", background = 'red', command = save_dict)
btn2.place(relx=.7, rely=.5, anchor="c")
message = StringVar()
message_entry = Entry(textvariable=message,width = 20)
message_entry.place(relx=.5, rely=.1, anchor="c")
#print(type(message.get()))
root.mainloop()
