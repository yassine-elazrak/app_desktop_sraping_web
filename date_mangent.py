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
        self.hours = Input(self.fram, "hour")
        self.hours.grid(row=0, column=5, padx=5, pady=5)

    def date_until(self):
        Label(self.fram, text="Date Until").grid(row=2, column=0, columnspan=2 ,sticky='E', padx=5, pady=2)
        self.years_until=Input(self.fram, "year")
        self.years_until.grid(row=2, column=2, padx=5, pady=5)
        self.months_until=Input(self.fram, "month")
        self.months_until.grid(row=2, column=3, padx=5, pady=5)
        self.days_until=Input(self.fram, "day")
        self.days_until.grid(row=2, column=4, padx=5, pady=5)
        self.hours_until=Input(self.fram, "hour")
        self.hours_until.grid(row=2, column=5, padx=5, pady=5)

    def valide(self):
        pass







    def get_all(self):

        # self.vars[0].append(self.years.get())
        # self.vars[0].append(self.months.get())
        # self.vars[0].append(self.days.get())
        # self.vars[0].append(self.hours.get())
        # self.vars[1].append(self.years_until.get())
        # self.vars[1].append(self.months_until.get())
        # self.vars[1].append(self.days_until.get())
        # self.vars[1].append(self.hours_until.get())
        since = self.years.get() + "-" + self.months.get() + "-" + self.days.get() + " " + self.hours.get() + ":00:00"
        until = self.years_until.get() + "-" + self.months_until.get() +  "-" + self.days_until.get() + " " + self.hours_until.get() + ":00:00"
        print("since = ", since)
        print("until = ", until)
        return self.vars

    def clear_all(self):
        self.years.ft_delete(0, END)
        self.months.ft_delete(0, END)
        self.days.ft_delete(0, END)
        self.hours.ft_delete(0, END)
        self.years_until.ft_delete(0, END)
        self.months_until.ft_delete(0, END)
        self.days_until.ft_delete(0, END)
        self.hours_until.ft_delete(0, END)



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

    def ft_name_file(self):
        Label(self.fram, text="Name File Output").grid(row=0, column=0, columnspan=2 ,sticky='w', padx=5, pady=2)
        self.name_file=Input(self.fram, "name file")
        self.name_file.grid(row=0, column=2,columnspan=2, padx=5, pady=5)
        
    def ft_path(self):
        Label(self.fram, text="Path of File Output").grid(row=0, column=4, columnspan=4 ,sticky='W', padx=5, pady=2)
        self.path_file=Input(self.fram, "path file")
        self.path_file.grid(row=0, column=11, padx=5, pady=5)

    def clear_all(self):
        self.name_file.ft_delete(0, END)
        self.path_file.ft_delete(0, END)
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
        self.ft_name_file()
        self.ft_path()


      
