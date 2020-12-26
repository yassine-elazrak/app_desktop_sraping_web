
from tkinter import *
from class_tools import Input
from functools import reduce
from pprint import pprint

class Check_box(Frame):

    def __init__(self, apps):
        Frame.__init__(self, apps)
        self.vars = []
        self.fieldnames = [[
            "id",
            "conversation_id",
            "created_at",
            "date",
            "time",
            "timezone",
            "user_id",
            "username",
            "name"],
            [
            "place",
            "tweet",
            "language",
            "mentions",
            "urls",
            "photos",
            "replies_count",
            "retweets_count",
            "likes_count"
        ], [
            "hashtags",
            "cashtags",
            "link",
            "retweet",
            "quote_url",
            "video",
            "thumbnail",
            "near",
            "geo"
        ],
            [
            "source",
            "user_rt_id",
            "user_rt",
            "retweet_id",
            "reply_to",
            "retweet_date",
            "translate",
            "trans_src",
            "trans_dest"
        ]
        ]
        self.keys = reduce(lambda i, j: i + j, self.fieldnames)
        self.fields = []

    def creat(self):
        self.field1 = Frame(self.fram)
        self.field1.grid(row=0, columnspan=12, sticky='w', padx=4, pady=3)
        for name in self.fieldnames[0]:
            var = IntVar()
            box = Checkbutton(self.field1, text=str(name) ,variable=var)
            box.pack(side=LEFT)
            self.vars.append(var)

        self.field2 = Frame(self.fram)
        self.field2.grid(row=1, columnspan=12, sticky='w', padx=4, pady=3)
        for name in self.fieldnames[1]:
            var = IntVar()
            box = Checkbutton(self.field2, text=str(name) ,variable=var)
            box.pack(side=LEFT)
            self.vars.append(var)

        self.field3 = Frame(self.fram)
        self.field3.grid(row=2, columnspan=12, sticky='w', padx=4, pady=3)
        for name in self.fieldnames[2]:
            var = IntVar()
            box = Checkbutton(self.field3, text=str(name),variable=var)
            box.pack(side=LEFT)
            self.vars.append(var)

        self.field4 = Frame(self.fram)
        self.field4.grid(row=3, columnspan=12, sticky='w', padx=4, pady=3)
        for name in self.fieldnames[3]:
            var = IntVar()
            box = Checkbutton(self.field4, text=str(name) ,variable=var)
            box.pack(side=LEFT)
            self.vars.append(var)

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
    
    def clear_all(self):
        for var in self.vars:
            var.set(0)
        

    def main(self):
        self.fram = LabelFrame(
            self.master, text="Enter Details For fieldnames :")
        self.fram.grid(row=6, columnspan=8, sticky='W',
                       padx=5, pady=5, ipadx=5, ipady=5)
        self.creat()

##########################
    # def state(self):
    #     return map((lambda var: var.get()), self.vars)

##############################


class List_box:
    def __init__(self, apps=None):
        self.master = apps
        self.Words = []

    def add(self):
        if self.data.get():
            self.Words.append(self.data.get())
            self.list_box.insert(END, self.data.get())
            self.data.delete(0, END)

    def remove(self):
        if self.Words:
            self.list_box.delete(END)
            self.Words.pop()

    def get_all(self):
        return self.Words
        
    def clear_all(self):
        self.Words.clear()
        self.list_box.delete(0,END)
        self.data.delete(0,END)


    def creat(self):
        self.field1 = Frame(self.fram)
        self.field1.grid(row=0, columnspan=8, sticky='w', padx=8, pady=8)
        self.label = Label(self.field1, text="     Search :")
        self.label.grid(row=0, column=0, columnspan=2,
                        sticky='W', padx=5, pady=2)
        self.data = Input(self.field1, "enter key search")
        self.data.grid(row=0, column=1, padx=5, pady=5)
        self.button_add = Button(
            self.field1, text='add element', command=self.add)
        self.button_add.grid(row=1, column=0, padx=5, pady=5)
        self.button_remove = Button(
            self.field1, text='remove element', command=self.remove)
        self.button_remove.grid(row=1, column=1, padx=5, pady=5)

        self.field2 = Frame(self.fram)
        self.field2.grid(row=2, columnspan=8, sticky='w', padx=8, pady=8)
        self.list_box = Listbox(self.field2, height=2,
                                width=50,
                                bg="grey",
                                activestyle='dotbox',
                                font="Helvetica",
                                fg="yellow")
        self.list_box.grid(row=3, column=0)

    def main(self):
        self.fram = LabelFrame(
            self.master, text="Enter Details For Words Search :")
        self.fram.grid(row=10, columnspan=10, sticky='w',
                       padx=5, pady=5, ipadx=5, ipady=5)
        self.creat()
