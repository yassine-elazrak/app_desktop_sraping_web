from tkinter import *
from pprint import pprint
from class_tools import Input
from os import path
import os
# from main import apps

class DIR:
    def __init__(self, apps=None):
        self.master=apps
        self.var_csv = IntVar()
        self.var_json = IntVar()
      


    def ft_name_file(self):#########
        Label(self.fram, text="Name Of File Output  ", bg="#f2a343" , font =("Courier", 15, "italic")).grid(row=0, column=0, columnspan=2 ,sticky='w', padx=5, pady=2)
        self.name_file=Input(self.fram, "      name file")
        self.name_file.grid(row=0, column=7,  padx=3,pady=5, ipadx=88, ipady=11)
    def test_dir(self, data):
        return path.isdir(data)

    def ft_path(self):
        Label(self.fram, text="Path Of File Output  ", bg="#f2a343" , font =("Courier", 15, "italic")).grid(row=1, column=0, columnspan=4 ,sticky='W', padx=5, pady=2)
        self.path_file=Input(self.fram, "       path file", test=self.test_dir)
        self.path_file.grid(row=1, column=7,  padx=3,pady=5, ipadx=88, ipady=11)
        
    def clear_all(self):
        self.name_file.ft_delete(0, END)
        self.path_file.ft_delete(0, END)
        self.var_json.set(0)
        self.var_csv.set(0)

    def change_csv(self):
        if self.var_json.get() == 1:
            self.var_json.set(0)

    def change_json(self):
        if self.var_csv.get() == 1:
            self.var_csv.set(0)

    def box_type_file(self):
        Checkbutton(self.fram, text=str("Format csv ") ,variable=self.var_csv, command=self.change_csv, bg="#091833" , font =("Courier", 14, "italic")).grid(row=2, column=0, padx=0, pady=0)
        Checkbutton(self.fram, text=str("Format josn") ,variable=self.var_json, command=self.change_json, bg="#091833" , font =("Courier", 14, "italic")).grid(row=2, column=5,columnspan=2, padx=0, pady=0)
        self.var_csv.set(1)
        

    def get_all(self):

        path_file = "."
        name_file = "tweets_twitter"
        # print("name ---{",self.name_file.get(),"}")
        # print("path-----{",self.path_file,"}")
        if  self.path_file.get() and os.path.isdir(self.path_file.get()) and self.path_file != "path file":
            path_file = self.path_file.get()
    
        # print("path_file", "|",path_file , "|")
        
        if  self.name_file.get() and  not "name file" in self.name_file.get() :
            name_file = self.name_file.get()

        # print("name_file","|",name_file, "|")
        if self.var_json.get() == 1:
            path_file = path_file + "/" + name_file + ".json"
        else:
            path_file = path_file + "/" + name_file + ".csv"
        # print("path->>", "|",path_file , "|")

        return path_file
        
    def main(self):
        self.fram = LabelFrame(self.master, text=" Enter Details For Output :" ,fg = "red", font =("Courier", 26, "italic"))
		#  font = "Times")
        self.fram.grid(row=2, columnspan=8, sticky='w', \
                 padx=5, pady=5, ipadx=5, ipady=5)
        self.fram.configure(background="#091833")
        
        self.ft_name_file()
        self.ft_path()
        self.box_type_file()


      
