
from tkinter import *
from class_tools import Input
from functools import reduce
from pprint import pprint
# import tkinter.font 
# import tkinter
# import tkFont
import tkinter.font as TkFont
# import tkinter.font as TkFont

# helv36 = TkFont.Font(family='Helvetica', size=36, weight=TkFont.BOLD)
class Check_box(Frame):

    def __init__(self, apps):
        Frame.__init__(self, apps)
        self.vars = []
        self.font_butt = TkFont.Font(family='Helvetica', size=10, weight=TkFont.BOLD)
        self.fieldnames = [[
            "created_at",
            "date"
        ],
        [
            "time",
            "username"
        ],
        [
            "name",
            "place"
        ],
        [
            "tweet",
            "language"
        ],
        [
            "mentions",
            "urls"
        ],
        [
            
            "likes_count"
            ,"retweet"
        ], [
            "hashtags",
            "cashtags"
        ],
        [
            "retweets_count",
            "link"
            ],
        [
            "thumbnail",
            "near"
            ]
        ,
        [
            "retweet_id",
            "reply_to"
            ],
        [
            "retweet_date",
            "translate"
            ]
        ]

        self.keys = reduce(lambda i, j: i + j, self.fieldnames)
        self.fields = []

    def creat(self):
        index = 0
        for name in self.fieldnames:
            self.field1 = Frame(self.fram,bg="#091833")
            self.field1.grid(row=index, columnspan=2, sticky='w', padx=2, pady=4)  
            var = IntVar()
            box = Checkbutton(self.field1, text=str(name[0]) ,variable=var,bg="#091833", fg = "snow", font =("Courier", 12, "italic"))
            box.pack(side=LEFT)
            self.vars.append(var)
            var = IntVar()
            box = Checkbutton(self.field1, text=str(name[1]) ,variable=var,bg="#091833", fg = "snow", font =("Courier", 12, "italic"))
            box.pack(side=LEFT)
            self.vars.append(var)
            index += 1
        self.butt_set = Button(self.fram, text=  "set all       " ,font=self.font_butt, command=self.set_all, bg = "red" ,width=13)
        self.butt_set.grid(row=15, column=0 , padx=5,pady=5, ipadx=5, ipady=5)
        self.butt_clear = Button(self.fram, text="clear all     ",font=self.font_butt, command=self.clear_all, bg = "red" ,width=13)
        self.butt_clear.grid(row=15, column=1, padx=5,pady=5, ipadx=5, ipady=5)

    def ft_map(self):
        index = 0
        for Variable in self.vars:
            if Variable.get() == 1:
                self.fields.append(self.keys[index])
            index += 1

    def get_all(self):
        self.ft_map()
        pprint(self.vars)
        if not self.fields:
            return self.keys
        return self.fields

    def set_all(self):
         for var in self.vars:
            var.set(1)

    def clear_all(self):
        for var in self.vars:
            var.set(0)
        

    def main(self):
        self.fram = LabelFrame(self.master, text="Enter Fieldnames:" ,bg="#091833" ,fg = "red",
		  font =("Courier",19, "italic"))
        self.fram.grid(row=0, column=9, columnspan=2, rowspan=6, \
                sticky='NS', padx=5, pady=5)

        self.creat()

##########################
    # def state(self):
    #     return map((lambda var: var.get()), self.vars)

##############################


class List_box:
    def __init__(self, apps=None):
        self.master = apps
        self.Words = []
        self.font_butt = TkFont.Font(family='Helvetica', size=10, weight=TkFont.BOLD)


    def add(self):
        if self.data.get() and not "      enter key search" in self.data.get():
            self.Words.append(self.data.get())
            self.list_box.insert(0, self.data.get())
            self.data.ft_delete(0, END)

    def remove(self):
        if self.Words:
            self.list_box.delete(0)
            self.Words.pop()

    def get_all(self):
        print("keys=>>", self.Words)
        return self.Words
        
    def clear_all(self):
        self.Words.clear()
        self.list_box.delete(0,END)
        self.data.ft_delete(0,END)


    def creat(self):
        self.field1 = Frame(self.fram ,bg="#091833")
        self.field1.grid(row=0, columnspan=2, sticky='w', padx=2, pady=2)
        self.field1.configure(background="#091833")
        self.field2 = Frame(self.fram ,bg="#091833")
        self.field2.grid(row=1, columnspan=2, sticky='w', padx=2, pady=2)
        self.field2.configure(background="#091833")

        self.label = Label(self.field1, text="Search :", fg="snow", bg="#f2a343" , font =("Courier", 28, "italic"))
        self.label.grid(row=0, column=0)
        self.label.configure(background="#091833")

        self.data = Input(self.field1, "      enter key search")
        self.data.grid(row=0, column=1, padx=3,pady=5, ipadx=88, ipady=11)
        self.button_add = Button(self.field2, text='   add element  ',font=self.font_butt, bg='red', command=self.add)
        self.button_add.grid(row=0, column=7,sticky='w',  padx=5,pady=1, ipadx=5, ipady=5)###
        self.button_remove = Button(
        self.field2, text=' remove element ',font=self.font_butt, bg='red', command=self.remove)
        self.button_remove.grid(row=0, column=8,sticky='W',  padx=0,pady=1, ipadx=5, ipady=5)####

        self.field2 = Frame(self.fram,bg="#091833")
        self.field2.grid(row=0, column=5, columnspan=2, rowspan=3, \
                sticky='NS', padx=5, pady=5)
        self.list_box = Listbox(self.field2, height=4,
                                width=18,
                                bg="#f2a343",
                                activestyle='dotbox',
                                font="Helvetica",
                                fg="gray44")
        self.list_box.grid(row=0, column=7)

    def main(self):
        self.fram = LabelFrame(
            self.master, text=" Enter Details For Words Search :" ,fg = "red",
		  font =("Courier", 26, "italic"))
        self.fram.grid(row=5, columnspan=7, sticky='W')
                    #    padx=5, pady=5, ipadx=5, ipady=5)
        self.fram.configure(background="#091833")

        self.creat()
