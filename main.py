from tkinter import *
from date_mangent import date

apps = Tk()


def main():
    label_fram = date(apps)
    label_fram.creat()
    def add():
        print("==>",label_fram.years_until.get())
    Button(apps, text='Peek', command=add).grid(row=8, column=9)
    


def app_init():
    apps.title("extracting_tweets")
    apps.geometry('1400x1000+50+50')

if __name__=="__main__":
    app_init()
    main()
    apps.mainloop()
