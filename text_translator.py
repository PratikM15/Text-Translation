from tkinter import *
from translate import Translator

#translator function
def translate():
    translator = Translator(from_lang=lan1.get(),to_lang=lan2.get())
    translation = translator.translate(var.get())
    var1.set(translation)

#Tkinter root window with title
root = Tk()
root.title("Translator")

#Creating a Frame and Grid to hold the Content
mainframe = Frame(root)
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
mainframe.pack(pady=100, padx=100)

#Variables for dropdown list
lan1 = StringVar(root)
lan2 = StringVar(root)

#Choices to show in the dropdown
choices = {'English', 'Hindi', 'Gujarati', 'Spanish', 'German', 'Marathi'}
lan1.set('English')
lan2.set('Hindi')

#Creating dropdown and arranging in the grid
lan1menu = OptionMenu(mainframe, lan1, *choices)
Label(mainframe, text="Select a language").grid(row=0, column=1)
lan1menu.grid(row=1, column=1)

lan2menu = OptionMenu(mainframe, lan2, *choices)
Label(mainframe, text="Select a language").grid(row=0, column=3)
lan2menu.grid(row=1, column=3)

#Textbox to take user input
Label(mainframe, text="Enter text").grid(row=2, column=0)
var = StringVar()
textbox = Entry(mainframe, textvariable=var).grid(row=2, column=1)

#Textbox to show Output
Label(mainframe, text="Output").grid(row=2, column=2)
var1 = StringVar()
textbox = Entry(mainframe, textvariable=var1).grid(row=2, column=3)

#Creating a button to call translator
b = Button(mainframe, text="Translate", command=translate).grid(row=3, column=1, columnspan=3)
root.mainloop()


