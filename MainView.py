from tkinter import *
# from date_mangent import date
from date_mangent import DIR
from class_tools import Run
from check_box import Check_box
from check_box import List_box
from time import sleep
from calender import Time
import tkinter
# from ft_twint import Config_twint
from threading import Timer, Thread

from tkinter import font as tkFont
import tkinter as tk
from pprint import pprint

class Page(Frame):
    def __init__(self, *args, **kwargs):
        # print(args,"================================]n]n]n\n\n\n\n\n\n\n\n",kwargs)
        super().__init__( *args, **kwargs)
        # self['bg'] = "#091833"
        # self['fg'] = 'green'
        print("w = ",self.winfo_width())
        print("h = ",self.winfo_height())
    

    def load(self):
        self.lift()

class Home(Frame):
    def __init__(self,parent, controller):
        super().__init__(parent)
        # self['bg'] = "#091833"
        # self.main()
    # def main(self):
        helv36 = tkFont.Font(family='Helvetica', size=36, weight=tkFont.BOLD)
        clander= Time(parent)
        clander.main()
        path = DIR(parent)
        path.main()
        box = Check_box(parent)
        box.main()
        arena = List_box(parent)
        arena.main()
        run=Run(parent,clander, path, box, arena)
        print("run")
        Thread(target=run.main).start()
        print("end _run")
    
        # Label(self , text="home    page").grid(row=3, column=2)
        # button_home = Button(self, text="Dowload", command= lambda : controller.load_page(Download))
        # button_home.grid(row = 2, column = 1, padx = 10, pady = 10) 

class Download(Frame):
    def __init__(self,parent, controller):
        super().__init__(parent)
        self['bg'] = "#091833"
    
        Label(self , text="domload  kdk   page").grid(row=5, column=2)
        button_home = Button(self, text="statistics", command= lambda : controller.load_page(Statistics))
        button_home.grid(row = 7, column = 1, padx = 10, pady = 10) 


class Statistics(Frame):
    def __init__(self,parent, controller):
        super().__init__(parent)
        self['bg'] = "#091833"
    
        Label(self , text="static   page").grid(row=8, column=2)
        button_home = Button(self, text="home", command= lambda : controller.load_page(Home))
        button_home.grid(row = 2, column = 1, padx = 10, pady = 10) 

class MainView(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fram = {}
        # self.header = Frame(self)
        # # self.container.grid(row=2, rowspan=10 ,column=0, columnspan=10)
        # self.header.pack(side = "top", fill = "both", expand = False)
        # self.header.grid_rowconfigure(0, weight = 2)
        # self.header.grid_columnconfigure(0, weight = 1)
        # self['rowspan'] = 13
        # button_home = Button(self,text="tes55t").grid(row=9,column=6)
        # self.head = Frame(self)
        # self.head.grid(row=0,rowspan=2 ,column=0, columnspan = 5)
        self.container = Frame(self)
        # self.container.grid(row=2, rowspan=10 ,column=0, columnspan=10)
        self.container.pack(side = "top", fill = "both", expand = True)
        self.container.grid_rowconfigure(0, weight = 1)
        self.container.grid_columnconfigure(0, weight = 1)
        
        # Label(self.container,text="main").grid(row=0, column=0)
        

        # self.page_home = Home(self.container,bg="#091833")
        # self.page_home.grid(row=2,rowspan=4 ,column=0, columnspan=10)
        # self.page_download = Download(self.container)
        # self.page_download.grid(row=3, column=0)
        # self.page_statistics = Statistics(self.container)
        # self.page_statistics.grid(row=3, column=0)

        # self.button_home = Button(self.header,text="home" ,command= lambda : self.load_page(Home))
        # self.button_home.grid(row=0, column=0)
        # self.button_download = Button(self.header,text="download",command= lambda : self.load_page(Download))
        # self.button_download.grid(row=0, column=1)
        # self.button_statistics = Button(self.header,text="statistics", command= lambda : self.load_page(Statistics))
        # self.button_statistics.grid(row=0, column=2)
        for F in (Home, Download, Statistics):
            fram = F(self.container , self)
            self.fram[F] = fram
            fram.grid(row=0, column=0,sticky='nsew')
        self.load_page(Home)
    def load_page(self, obj):
        fram = self.fram[obj]
        fram.tkraise()

# if __name__=='__main__':
    
#     # print("appw = ",apps.winfo_width())
#     # print("apph = ",apps.winfo_height())

#     obj = MainView()
#     obj.title('test')
#     obj.geometry('555x600+0+0')
#     obj.mainloop()