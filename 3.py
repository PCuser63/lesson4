from tkinter import *
root = Tk()
root.geometry("400x300")
def myClick():
    myLabel = Label(root, text = "Нажата кнопка!")
    myLabel.pack()

myButton = Button(root, text = "Нажмите кнопку",
                  command= myClick,fg = 'blue',bg = 'white' )
myButton.pack()
root.mainloop()