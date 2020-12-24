from tkinter import *
from pprint import pprint
from class_tools import Input
# from main import apps


class date:
    def __init__(self, apps=None):
        self.master = apps
        # print(apps)

    def date_since(self):
        Label(self.fram, text="Date Sine").grid(
            row=0, column=0, columnspan=2, sticky='E', padx=5, pady=2)
        self.years = Entry(self.fram)
        self.years.grid(row=0, column=2, padx=5, pady=5)
        self.months = Entry(self.fram)
        self.months.grid(row=0, column=3, padx=5, pady=5)
        self.days = Entry(self.fram)
        self.days.grid(row=0, column=4, padx=5, pady=5)
        self.heurs = Entry(self.fram)
        self.heurs.grid(row=0, column=5, padx=5, pady=5)

    def date_until(self):
        Label(self.fram, text="Date Until").grid(row=2, column=0, columnspan=2 ,sticky='E', padx=5, pady=2)
        self.years_until=Input(self.fram)
        self.years_until.grid(row=2, column=2, padx=5, pady=5)
        # self.months_until=Entry(self.fram)
        # self.months_until.grid(row=2, column=3, padx=5, pady=5)
        # self.days_until=Entry(self.fram)
        # self.days_until.grid(row=2, column=4, padx=5, pady=5)
        # self.heurs_until=Entry(self.fram)
        # self.heurs_until.grid(row=2, column=5, padx=5, pady=5)

    def creat(self):
        self.fram = LabelFrame(self.master, text="Enter Details On Date :")
        self.fram.grid(row=0, columnspan=7, sticky='W', \
                 padx=5, pady=5, ipadx=5, ipady=5)
        self.date_since()
        self.date_until()
      
