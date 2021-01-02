
# from nltk.corpus import stopwords  
# from nltk.tokenize import word_tokenize  

# stop_words = stopwords.words('english')  
# from nltk.stem import SnowballStemmer
# snowball_stemmer = SnowballStemmer('english')
# # snowball_stemmer.stem(word)
# print(dir(snowball_stemmer)) 
# example_sent = """This is a sample sentence, 
#                   showing off the stop words filtration."""
  
  
# word_tokens = word_tokenize(example_sent)  
  
# filtered_sentence = [w for w in word_tokens if not w in stop_words]  
  
# filtered_sentence = []  
  
# for w in word_tokens:  
#     if w not in stop_words:  
#         filtered_sentence.append(w)  
  
# print(word_tokens)  
# print(filtered_sentence)
name = ".files/aaadodo2 2"
open(name, 'a+')

































































# # from tkinter import filedialog
# # from tkinter import *
 
# # root = Tk()
# # name =  filedialog.askdirectory(initialdir = "/",title = "Select file")
# # print (name)
# # try:  # Python-2
# #     from Tkinter import *
# #     import tkFont
# # except ImportError:  # Python-3
# from tkinter import *
# from tkinter import font as tkFont
# # using grid
# # +------+-------------+
# # | btn1 |    btn2     |
# # +------+------+------+
# # | btn3 | btn3 | btn4 |
# # +-------------+------+
# root = Tk()
# # tkFont.BOLD == 'bold'
# helv36 = tkFont.Font(family='Helvetica', size=36, weight=tkFont.BOLD)
# btn1 = Button(text='btn1', font=helv36)
# btn2 = Button(text='btn2', font=helv36)
# btn3 = Button(text='btn3', font=helv36)
# btn4 = Button(text='btn4', font=helv36)
# btn5 = Button(text='btn5', font=helv36)
# root.rowconfigure((0,1), weight=1)  # make buttons stretch when
# root.columnconfigure((0,2), weight=1)  # when window is resized
# btn1.grid(row=0, column=0, columnspan=1, sticky='EWNS')
# btn2.grid(row=0, column=1, columnspan=2, sticky='EWNS')
# btn3.grid(row=1, column=0, columnspan=1, sticky='EWNS')
# btn4.grid(row=1, column=1, columnspan=1, sticky='EWNS')
# btn5.grid(row=1, column=2, columnspan=1, sticky='EWNS')
# root.mainloop()
# # from  tkinter import *
# # import   tkinter
# # # , tkconstants,
# # root = Tk()
# # root.directory = tkinter.filedialog.askdirectory
# # # tkFileDialog.askdirectory()
# # print (root.directory)


# # import tkinter as tk
# # from tkinter import messagebox

# # from tkinter import *

# # #On cree une fenetre et un canevas:
# # tk = Tk()
# # canvas = Canvas(tk,width = 500, height = 400 , bd=0, bg="white")
# # canvas.pack(padx=10,pady=10)

# # #Creation  d'un bouton "Quitter":
# # Bouton_Quitter=Button(tk, text ='Quitter', command = tk.destroy)
# # #On ajoute l'affichage du bouton dans la fenêtre tk:
# # Bouton_Quitter.pack()

# # #On cree une balle:
# # balle1 = canvas.create_oval(10,10,30,30,fill='red')

# # #On lance la boucle principale:
# # tk.mainloop()