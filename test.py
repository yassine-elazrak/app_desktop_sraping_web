# from tkinter import filedialog
# from tkinter import *
 
# root = Tk()
# root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
# print (root.filename)

# from  tkinter import *
# import tkinter, tkconstants, tkFileDialog
# root = Tk()
# root.directory = tkFileDialog.askdirectory()
# print (root.directory)


import tkinter as tk
from tkinter import messagebox

from tkinter import *

#On cree une fenetre et un canevas:
tk = Tk()
canvas = Canvas(tk,width = 500, height = 400 , bd=0, bg="white")
canvas.pack(padx=10,pady=10)

#Creation  d'un bouton "Quitter":
Bouton_Quitter=Button(tk, text ='Quitter', command = tk.destroy)
#On ajoute l'affichage du bouton dans la fenêtre tk:
Bouton_Quitter.pack()

#On cree une balle:
balle1 = canvas.create_oval(10,10,30,30,fill='red')

#On lance la boucle principale:
tk.mainloop()