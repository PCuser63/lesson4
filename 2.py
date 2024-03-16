from tkinter import *
root = Tk()
root.geometry("400x300")
myLabel1 = Label(root, text = "Hello World!").grid(row = 0, column = 0)
myLabel2 = Label(root, text = "Меня зовут Кайафас Каин").grid(row = 1, column = 0)

root.mainloop()