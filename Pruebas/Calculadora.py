from Tkinter import *

raiz = Tk()
marco = Frame(raiz).grid(row=0, column=0)

visor = Entry(marco, width=30).grid(row=0, column=0, columnspan=4)

btn = Button(marco, text="CE", height=2, width=5).grid(row=1, column=0)
btn = Button(marco, text="C", height=2, width=5).grid(row=1, column=1)
btn = Button(marco, text="<", height=2, width=5).grid(row=1, column=2)
btn = Button(marco, text="/", height=2, width=5).grid(row=1, column=3)
btn = Button(marco, text="7", height=2, width=5).grid(row=2, column=0)
btn = Button(marco, text="8", height=2, width=5).grid(row=2, column=1)
btn = Button(marco, text="9", height=2, width=5).grid(row=2, column=2)
btn = Button(marco, text="*", height=2, width=5).grid(row=2, column=3)
btn = Button(marco, text="4", height=2, width=5).grid(row=3, column=0)
btn = Button(marco, text="5", height=2, width=5).grid(row=3, column=1)
btn = Button(marco, text="6", height=2, width=5).grid(row=3, column=2)
btn = Button(marco, text="-", height=2, width=5).grid(row=3, column=3)
btn = Button(marco, text="1", height=2, width=5).grid(row=4, column=0)
btn = Button(marco, text="2", height=2, width=5).grid(row=4, column=1)
btn = Button(marco, text="3", height=2, width=5).grid(row=4, column=2)
btn = Button(marco, text="+", height=2, width=5).grid(row=4, column=3)
btn = Button(marco, text="+-", height=2, width=5).grid(row=5, column=0)
btn = Button(marco, text="0", height=2, width=5).grid(row=5, column=1)
btn = Button(marco, text=",", height=2, width=5).grid(row=5, column=2)
btn = Button(marco, text="=", height=2, width=5).grid(row=5, column=3)

raiz.mainloop()


