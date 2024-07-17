from tkinter import *
root = Tk()
root.title("simple Calculator")
e = Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
e.pack()

def button_add():
    return
button_1 = Button(root,text="1",padx=40,pady=20,command=button_add)

myButton = Button(root, text="enter your name",padx=50,pady=50,command=myClick,fg ="blue",bg="white")
myButton.pack()

root.mainloop()