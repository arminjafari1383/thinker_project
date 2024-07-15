from tkinter import *
root = Tk()
#creating alabel widget 
myLabel1 = Label(root,text="hello world")
myLabel2 = Label(root,text="my name is john elder ")
myLabel1.grid(row=0,column=0)
myLabel2.grid(row=1,column=5)

root.mainloop()