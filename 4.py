from tkinter import *
root = Tk()
root.geometry("400x300")
e = Entry(root, width = 50, bg = "blue", fg = "white", 
          borderwidth = 5)
e.pack()
e.insert(0,"Введите ваше имя: ")

def myClick():
    hello = "Привет " + e.get()
    myLabel = Label(root, text = hello)
    myLabel.pack()
myButton = Button(root,text = "Ввести", command = myClick,fg = "black", bg = "white")
myButton.pack()
root.mainloop()