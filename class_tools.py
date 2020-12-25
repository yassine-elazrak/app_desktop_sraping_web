from tkinter import *


class Input(Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey'):
        super().__init__(master)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']
        self.string = ""

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()


class Run:
    def __init__(self, apps=None, date=None,   path=None, box=None, arena=None ):
        self.master = apps
        self.date = date
        self.path=path
        self.box=box
        self.arena=arena

    def get_all(self):
        pass
    
    def clear_all(self):
        pass

    def valide(self):
        pass

    def creat(self):
        self.buton = Frame(self.master)
        self.buton.grid(row=18,columnspan=12, rowspan=3, sticky='SE')
        self.buton_clear = Button(self.buton, text="clear",  width = 10)
        self.buton_clear.grid(row=2, column=12, padx=5, pady=6)
        self.buton_run = Button(self.buton, text="run" , width = 10) 
        self.buton_run.grid(row=2, column=13, padx=5, pady=6)


    def main(self):
        self.creat()
        # self.valide()