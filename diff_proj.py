from tkinter import *
 
root = Tk()
 
e = Entry(width=100)
b = Button(text="Определить")
l = Label(bg='yellow', fg='black', width=100)
 
def strToSortlist(event):
    l['text'] = 'я хз'
 
b.bind('<Button-1>', strToSortlist)
 
e.pack()
b.pack()
l.pack()
root.mainloop()
