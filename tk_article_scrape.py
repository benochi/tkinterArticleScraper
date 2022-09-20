# import modules
from tkinter import *
from goose3 import Goose
 
# for getting information
def info():
    article = Goose().extract(e1.get())
    title.set(article.title)
    meta.set(article.meta_description)
    string = article.cleaned_text[:150]
    art_dec.set(string.split("\n"))
     
# object of tkinter
# and background set to grey
master = Tk()
master.configure(bg='light grey')
 
# Variable Classes in tkinter
title = StringVar();
meta = StringVar();
art_dec = StringVar();
 
# Creating label for each information
# name using widget Label
Label(master, text="Website URL : " ,
      bg = "light grey").grid(row=0, sticky=W)
Label(master, text="Title :",
      bg = "light grey").grid(row=3, sticky=W)
Label(master, text="Meta information :",
      bg = "light grey").grid(row=4, sticky=W)
Label(master, text="Article description :",
      bg = "light grey").grid(row=5, sticky=W)
 
# Creating label for class variable
# name using widget Entry
Label(master, text="", textvariable=title,
      bg = "light grey").grid(row=3,column=1, sticky=W)
Label(master, text="", textvariable=meta,
      bg = "light grey").grid(row=4,column=1, sticky=W)
Label(master, text="", textvariable=art_dec,
      bg = "light grey").grid(row=5,column=1, sticky=W)
 
e1 = Entry(master, width = 100)
e1.grid(row=0, column=1)
 
# creating a button using the widget 
# to call the submit function
b = Button(master, text="Show", command=info , bg = "Blue")
b.grid(row=0, column=2,columnspan=2, rowspan=2,padx=5, pady=5,)
 
mainloop()
