from tkinter import *
# button = you click it, then it does stuff
def click():
    '''while True:
        count += 1'''
    print("You clicked the button!")

window = Tk()

button = Button(window,
                text="Click me!",
                command=click,
                font=("Comic sans", 30),
                fg="red",
                bg="black")
button.pack()

window = mainloop()