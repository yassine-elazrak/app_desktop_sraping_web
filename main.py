
from tkinter import *
# from date_mangent import date
from date_mangent import DIR
from class_tools import Run
from check_box import Check_box
from check_box import List_box
from time import sleep
from calender import Time
# from ft_twint import Config_twint
from threading import Timer, Thread

from tkinter import font as tkFont


font10="{Courier New} 10 normal"
font11 = {"{U.S. 101} 30 bold"}
font15 = {"{Al-Aramco 11 bold}"}
font16="{Segoe UI} 13 bold"
# fg= "steel blue"  "#f2a343" "bg#d9d9d9" "#c60000"


####key___["Royal Air Maroc" , "@RAM_Maroc",    "@RAM_Maroc", \
#   "royalairmaroc", "الخطوط المغربيه" , "#الخطوط_الملكية_المغربية "\
#  , "الخطوط الملكية المغربية"    , "لارام",  " لارام"\
# ,"الخطوط_الملكية_المغربية" ]

apps = Tk()

def main():
    helv36 = tkFont.Font(family='Helvetica', size=36, weight=tkFont.BOLD)
    clander= Time(apps)
    clander.main()
    path = DIR(apps)
    path.main()
    box = Check_box(apps)
    box.main()
    arena = List_box(apps)
    arena.main()
    run=Run(apps,clander, path, box, arena)
    run.main()
    # btn1 = Button(text='btn1', font=helv36)
    # btn1.grid(row=0, column=0, columnspan=1, sticky='EWNS')

   
  
  

def app_init():
    apps.title("extracting_tweets")
    apps.geometry('1200x590+0+0')#750x580+10+10 bg="#091833"
    apps.configure(background="#091833")


if __name__ == "__main__":
    app_init()
    main()
    apps.mainloop()
