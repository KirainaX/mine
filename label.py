from tkinter import *

# label an area widget taht holds text and/or an image within a windodw

window = Tk()

photo = PhotoImage(file='xxxxxxxddddddddd.PNG')

label = Label(window,
              text='Hello! KirainaX', # text that will printed in window
              font=('Arial', 40, 'bold'), # font of text
              fg='red',# color of the text
              bg='black',# color of background of the text
              relief=RAISED,
              bd=10,
              padx=20,# how much space that kep from right and left
              pady=20,# how much space that kep from abouve and below
              image=photo, # add a photo to the wondow
              compound='bottom', )

# label.place(x='100', y='100') # place = its gona put text with x=100px and y=100px in window
label.pack() # pack = put the text in midel of the window

window.mainloop()
