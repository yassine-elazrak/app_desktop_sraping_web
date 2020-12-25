from tkinter import *
from pprint import pprint
from class_tools import Input
# from main import apps


class date:
    def __init__(self, apps=None):
        self.master = apps
        self.vars= [[], []]

    def date_since(self):
        Label(self.fram, text="Date Sine").grid(
            row=0, column=0, columnspan=2, sticky='E', padx=5, pady=2)
        self.years = Input(self.fram, "year")
        self.years.grid(row=0, column=2, padx=5, pady=5)
        self.months = Input(self.fram, "month")
        self.months.grid(row=0, column=3, padx=5, pady=5)
        self.days = Input(self.fram, "day")
        self.days.grid(row=0, column=4, padx=5, pady=5)
        self.heurs = Input(self.fram, "heur")
        self.heurs.grid(row=0, column=5, padx=5, pady=5)

    def date_until(self):
        Label(self.fram, text="Date Until").grid(row=2, column=0, columnspan=2 ,sticky='E', padx=5, pady=2)
        self.years_until=Input(self.fram, "year")
        self.years_until.grid(row=2, column=2, padx=5, pady=5)
        self.months_until=Input(self.fram, "month")
        self.months_until.grid(row=2, column=3, padx=5, pady=5)
        self.days_until=Input(self.fram, "day")
        self.days_until.grid(row=2, column=4, padx=5, pady=5)
        self.heurs_until=Input(self.fram, "heur")
        self.heurs_until.grid(row=2, column=5, padx=5, pady=5)


    def creat(self):
        self.fram = LabelFrame(self.master, text="Enter Details On Date :")
        self.fram.grid(row=0, columnspan=7, sticky='W', \
                 padx=5, pady=5, ipadx=5, ipady=5)
        self.date_since()
        self.date_until()



class DIR:
    def __init__(self, apps=None):
        self.master=apps
        self.vars={}
        self.vars["name"] = "tweets_twitter"
        self.vars["path"]=  "."

    def name_file(self):
        Label(self.fram, text="Name File Output").grid(row=0, column=0, columnspan=2 ,sticky='w', padx=5, pady=2)
        self.name_file=Input(self.fram, "name file")
        self.name_file.grid(row=0, column=2,columnspan=2, padx=5, pady=5)
        
    def ft_path(self):
        Label(self.fram, text="Path of File Output").grid(row=0, column=4, columnspan=4 ,sticky='W', padx=5, pady=2)
        self.path_file=Input(self.fram, "path file")
        self.path_file.grid(row=0, column=11, padx=5, pady=5)

    def clear_all(self):
        self.name_file.delete(0, END)
        self.path_file.delete(0, END)
        self.vars["name"] = "tweets_twitter"
        self.vars["path"]=  "."
    
    def get_all(self):
        if self.name_file:
            self.vars["name"]= self.name_file.get()
        if self.path_file:
            self.vars["path"]= self.path_file.get()
        return self.vars
        
    def main(self):
        self.fram = LabelFrame(self.master, text="Enter Details For Output :")
        self.fram.grid(row=2, columnspan=10, sticky='w', \
                 padx=5, pady=5, ipadx=5, ipady=5)
        self.name_file()
        self.ft_path()


      
