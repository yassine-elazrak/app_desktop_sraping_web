try:
    from tkinter import *
except ImportError:
    from Tkinter import * 

from tkcalendar import Calendar, DateEntry

class Time:
    def __init__(self, app):
        self.master = app
        self.date_since = "2019-12-27"
        self.date_untill = "2020-01-27"
        self.var_since = StringVar()
        self.var_since.set(self.date_since)
        self.var_untill = StringVar()
        self.var_untill.set(self.date_untill)
        self.hour_since = "12"
        self.var_hour_since = StringVar()
        self.var_hour_since.set(self.hour_since)
        self.hour_untill = "12"
        self.var_hour_untill = StringVar()
        self.var_hour_untill.set(self.hour_untill)

    def get_all(self):#"2019-07-01 00:00:00"
        self.date_since = self.date_since + " " + self.hour_since + ":00:00"
        self.date_untill = self.date_untill + " " + self.hour_untill + ":00:00"
        print("data until", self.date_untill)
        print("data since", self.date_since)
        return(self.date_since, self.date_untill)

    def set_since(self):
        self.date_since =  self.cal_since.selection_get()
        self.var_since.set(self.date_since)
        # print("data since", self.date_since)

    def set_untill(self):
        self.date_untill =  self.cal_untill.selection_get()
        self.var_untill.set(self.date_untill)
        # self.cal_untill.close()


    def ft_calendar_since(self):
        top = Toplevel(self.master)
        self.cal_since = Calendar(top, font="Arial 14", selectmode="day", year=2020,month=11,day=22)
        self.cal_since.pack()
        self.butt_cal = Button(self.cal_since, text="ok", command=self.set_since , bg='red', height = 1, width = 14)
        self.butt_cal.pack()

    def ft_decrement_hour_since(self):
        hour = int(self.hour_since)
        if hour > 0:
            hour -= 1
            self.hour_since = str(hour)
        if len(self.hour_since) == 1:
            self.hour_since = "0" + self.hour_since
        self.var_hour_since.set(self.hour_since)

    def ft_increment_hour_since(self):
        hour = int(self.hour_since)
        if hour < 23:
            hour += 1
            self.hour_since = str(hour)
        if len(self.hour_since) == 1:
            self.hour_since = "0" + self.hour_since
        self.var_hour_since.set(self.hour_since)

    def ft_decrement_hour_untill(self):
        hour = int(self.hour_untill)
        if hour > 0:
            hour -= 1
            self.hour_untill = str(hour)
        if len(self.hour_untill) == 1:
            self.hour_untill = "0" + self.hour_untill
        self.var_hour_untill.set(self.hour_untill)

    def ft_increment_hour_untill(self):
        hour = int(self.hour_untill)
        if hour < 23:
            hour += 1
            self.hour_untill = str(hour)
        if len(self.hour_untill) == 1:
            self.hour_untill = "0" + self.hour_untill
        self.var_hour_untill.set(self.hour_untill)
    # def close_window(self, root)
    #     root.destroy()

    def ft_calendar_untill(self):
        top = Toplevel(self.master)
        self.cal_untill = Calendar(top, font="Arial 14", selectmode="day", year=2020,month=11,day=22)
        self.cal_untill.pack()
        self.butt_cal = Button(self.cal_untill, text="ok", bg='red', command=self.set_untill, height = 1, width = 14)
        # self.butt_cal.size(height=10, width=100)
        self.butt_cal.pack()

    def main(self):
        self.fram = LabelFrame(self.master, text="Enter Details On Date :")
        self.fram.grid(row=0, columnspan=10, sticky='W', \
                 padx=5,pady=1, ipadx=5, ipady=5)
        self.butt = Button(self.fram, text="date since", command=self.ft_calendar_since)
        self.butt.grid(row=0, column=2,  padx=5,pady=1, ipadx=5, ipady=5)
        Label(self.fram, textvariable=self.var_since).grid(row=0, column=4,  padx=5, pady=1, ipadx=5, ipady=5)

        self.butt_inc = Button(self.fram, text="increment hour    ", command= self.ft_increment_hour_since)
        self.butt_inc.grid(row=0, column=5,  padx=5,pady=1, ipadx=5, ipady=5)
        self.butt_dec = Button(self.fram, text="decrement hour     ", command=self.ft_decrement_hour_since)
        self.butt_dec.grid(row=0, column=6,  padx=5,pady=1, ipadx=5, ipady=5)
        Label(self.fram, textvariable=self.var_hour_since).grid(row=0, column=8,  padx=5,pady=1, ipadx=5, ipady=5)


        self.butt = Button(self.fram, text="date untill", command=self.ft_calendar_untill)
        self.butt.grid(row=1, column=2, padx=5,pady=1, ipadx=5, ipady=5)
        Label(self.fram, textvariable=self.var_untill).grid(row=1, column=4,  padx=5, pady=1, ipadx=5, ipady=5)
        self.butt_inc_mn = Button(self.fram, text="increment hour     ", command=self.ft_increment_hour_untill)

        self.butt_inc_mn.grid(row=1, column=5,  padx=5,pady=1, ipadx=5, ipady=5)
        self.butt_dec_mn = Button(self.fram, text="decrement hour     ", command=self.ft_decrement_hour_untill)
        self.butt_dec_mn.grid(row=1, column=6,  padx=5,pady=1, ipadx=5, ipady=5)
        Label(self.fram, textvariable=self.var_hour_untill).grid(row=1, column=8,  padx=5,pady=1, ipadx=5, ipady=5)