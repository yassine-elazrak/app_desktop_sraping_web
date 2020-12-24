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



# def ft_label(root,name, y, x, pady=20, padx = 20):
#     # part_text = StringVar() rowspan=6, pady=20, padx=20)
#     part_label = Label(root, text=name, font=('bold', 14), pady=pady, padx=padx)
#     part_label.grid(row=y, column=x, sticky=W)