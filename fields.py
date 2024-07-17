from tkinter import *
root = Tk()
e = Entry(root,width=50)
e.pack()
e.insert(0, "enter your name:")

def myClick():
    hello = "HELLO"+e.get()
    myLabel = Label(root,text=hello)
    myLabel.pack()


myButton = Button(root, text="enter your name",padx=50,pady=50,command=myClick,fg ="blue",bg="white")
myButton.pack()

root.mainloop()