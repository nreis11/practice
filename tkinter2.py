from tkinter import *
# Main window
root = Tk()
# Create a label
# thelabel = Label(root, text='Basic text')
# Put the label in the window
# thelabel.pack()


# topFrame = Frame(root)
# topFrame.pack()
# bottomFrame = Frame(root)
# bottomFrame.pack(side=BOTTOM)
#
# button1 = Button(topFrame, text="Button 1", fg='red')
# button2 = Button(topFrame, text="Button 2", fg='blue')
# button3 = Button(topFrame, text="Button 3", fg='green')
# button4 = Button(bottomFrame, text="Button 4", fg='black')
#
# button1.pack(side=LEFT)
# button2.pack(side=LEFT)
# button3.pack(side=LEFT)
# button4.pack(side=BOTTOM)

one = Label(root, text='One', bg='black', fg='yellow')
one.pack()
two = Label(root, text='Two', bg='green', fg='black')
two.pack(fill=X)
three = Label(root, text='Three', bg='black', fg='white')
three.pack(side=LEFT, fill=Y)

# Needed to display infinitely
root.mainloop()
