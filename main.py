from tkinter import *
from date_mangent import date
from date_mangent import DIR
from class_tools import Run
from check_box import Check_box
from check_box import List_box
from time import sleep

class Checkbar(Frame):
    def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
        Frame.__init__(self, parent)
        self.vars = []
        for pick in picks:
            var = IntVar()
            chk = Checkbutton(self, text=pick, variable=var)
            chk.pack(side=side, anchor=anchor, expand=YES)
            self.vars.append(var)

    def state(self):
        return map((lambda var: var.get()), self.vars)


apps = Tk()


def main():
    label_date = date(apps)
    label_date.creat()
    path = DIR(apps)
    path.main()
    box = Check_box(apps)
    box.main()
    arena = List_box(apps)
    arena.main()
    run=Run(apps, label_date, path, box, arena)
    run.main()
  

def app_init():
    apps.title("extracting_tweets")
    apps.geometry('950x850+50+50')


if __name__ == "__main__":
    app_init()
    main()
    apps.mainloop()
