from tkinter import *
from ft_twint import Config_twint
from pprint import pprint
from threading import Timer, Thread
from tkinter.messagebox import *
import os

class Input(Entry):
    def __init__(
        self,
        master=None,
        placeholder="PLACEHOLDER",
        color="grey",
        color_error="red3",
        test=None ,
    ):
        super().__init__(master)
        self["bg"] = "#091833"
        self["fg"] = "blue"
        # height=100)
        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self["fg"]
        self.color_error = color_error
        self.func_test = test
        self.data_is_valid = False
        self.cursor = False
        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)
        self.bind("<KeyRelease>", self.release)
        self.put_placeholder()


    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self["fg"] = self.placeholder_color

    def foc_in(self, *args):
        self.cursor = True
        if self["fg"] == self.placeholder_color:
            self.delete("0", "end")
            self["fg"] = self.default_fg_color

    def ft_delete(self, *args):
        self.delete(*args)
        if not self.cursor:
            self.put_placeholder()

    def release(self, *args):
        if self.func_test is not None:
            if not self.func_test(self.get()):
                self["fg"] = self.color_error
                self.data_is_valid = False
            else:
                self["fg"] = self.default_fg_color
                self.data_is_valid = True

    def foc_out(self, *args):
        self.cursor = False
        if not self.get():
            self.put_placeholder()
       
# class BUTTON(Button):
#     def __init__(self, *args):
#         super.__init__(*args)


class Run:
    def __init__(self, apps=None, date=None, path=None, box=None, arena=None):
        self.master = apps
        self.date = date
        self.path = path
        self.box = box
        self.arena = arena
        self.keys = []
        self.custom = []
        self.since = ""
        self.until = ""
        self.name_file = ""
        self.list_thread = []
        self.list_file = []
        self.list_time = []
       
      

    def get_all(self):
       self.since, self.until =  self.date.get_all()
       self.name_file =  self.path.get_all()
       self.custom =  self.box.get_all()
       self.keys =  self.arena.get_all()
    #    self.clear_all()



    def clear_all(self):
        self.date.clear_all()
        self.path.clear_all()
        self.box.clear_all()
        self.arena.clear_all()

    def exec(self):
        for thread in self.list_thread:
            thread.start()

    def my_job(self, keys, since, until , outfile , custom):
        print("my_job keys=>", keys)
        print("my_job since=>", since)
        print("my_job until=>", until)
        print("my_job outfile=>", outfile)
        print("my_job custom=>", custom)
        self.twint = Config_twint(keys=keys , since=since , \
            until=until, outfile=outfile , custom=custom)
        self.twint.run()

    def update_time(self):
        self.list_time.append(self.since)
        since, self.since = self.since.split("-", 1)
        until , _ = self.until.split("-", 1)
        self.diff_time = int(until) - int(since)
        for i in range(1 , self.diff_time):
            self.list_time.append(str(int(since) + i) + "-" + self.since)
        self.list_time.append(self.until)
        print("list_time",  self.list_time)


    def run(self):
        self.get_all()
        self.update_time()
        print("run keys", self.keys)
        # os.makedirs("./.data",  0o755)
        for i in range(0, len(self.list_time) - 1):
            self.since = self.list_time[i]
            self.until = self.list_time[i + 1]
            print("year", self.since, "----", self.until, self.keys)
            for key in self.keys:
                # name_file=key
                name_file = "./."  +self.since + key + ".csv"
                print(name_file)
                # self.list_file.append(name_file)
                # self.list_thread.append(Thread(target=self.my_job, args=[[key] , self.since , \
                #     self.until, name_file , [1,2,3, key]]))
        # self.exec()
        # self.list_time.clear()

            

    def creat(self):
        self.buton = Frame(self.master, bg="#091833")
        self.buton.grid(row=18, columnspan=13, rowspan=3, sticky="SE")
        self.buton_clear = Button(
            self.buton, text="clear", command=self.clear_all, width=16
        )
        self.buton_clear.grid(row=2, column=12, padx=5,pady=2, ipadx=5, ipady=5)
        self.buton_run = Button(self.buton, text="run", command=self.run, width=16)
        self.buton_run.grid(row=2, column=14, padx=5, pady=2, ipadx=5, ipady=5)

    def main(self):
        # Error("hello error test")
        self.creat()

# class Error:
#     def __init__(self, message="error try again"):
#         # root = Tk()
#         # root.withdraw()
#         # showerror(title = "Error", message=message)
#         # import tkMessageBox
 
#        messagebox.showinfo("Title", "a Tk MessageBox")
        # root.destroy()

