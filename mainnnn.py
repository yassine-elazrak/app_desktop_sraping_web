from tkinter import *
from tkinter import messagebox

class EntryWithPlaceholder(Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey'):
        super().__init__(master)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

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
# Create window object
app = Tk()
# app['bg']="red"

def ft_label(root,name, y, x, pady=20, padx = 20):
    # part_text = StringVar() rowspan=6, pady=20, padx=20)
    part_label = Label(root, text=name, font=('bold', 14), pady=pady, padx=padx)
    part_label.grid(row=y, column=x, sticky=W)


# Part
def ft_entry(root, y,x):
    part_text = StringVar()
    part_entry = Entry(root, textvariable=part_text)
    part_entry.grid(row=y, column=x, padx=22)

# ft_label(app,"date Since ",1,0)
# ft_label(app,"year ",0,1)
# ft_label(app,"month",0,2)
# ft_label(app,"day",0,3)
# ft_label(app,"heur",0,4)

# ft_entry(app,1,1)
# ft_entry(app,1,2)
# ft_entry(app,1,3)
# ft_entry(app,1,4)

# # ll = EntryWithPlaceholder(app)
# # ll.grid(row=5, column=5, padx=22)
# # ft_label(app,"year ",2,1)
# # ft_label(app,"month",2,2)
# # ft_label(app,"day",2,3)
# # ft_label(app,"heur",2,4)

# ft_label(app,"date Until ",2,0)
# ft_entry(app,2,1)
# ft_entry(app,2,2)
# ft_entry(app,2,3)
# ft_entry(app,2,4)

# ft_label(app,"name file ",4,0)
# ft_entry(app,4,1)
# ft_label(app,"path file ",5,0)
# ft_entry(app,5,1)

# password = EntryWithPlaceholder(app, "password", 'blue')
# password.grid(row=6, column=6, padx=22)

# ll=LabelFrame(app, text="Hello")
# ll.grid(row=6, colum=0, padx=10, pady=10)

stepOne = LabelFrame(app, text=" 1. Enter File Details: ")
stepOne.grid(row=0, columnspan=7, sticky='W', \
                 padx=5, pady=5, ipadx=5, ipady=5)


inFileLbl =   Label(stepOne, text="Select the File:")
inFileLbl.grid(row=0, column=0, sticky='E', padx=5, pady=2)
inFileTxt =   Entry(stepOne)
inFileTxt.grid(row=0, column=1, columnspan=7, sticky="WE", pady=3)
inFileBtn =   Button(stepOne, text="Browse ...")
inFileBtn.grid(row=0, column=8, sticky='W', padx=5, pady=2)
outFileLbl =   Label(stepOne, text="Save File to:")
outFileLbl.grid(row=1, column=0, sticky='E', padx=5, pady=2)
outFileTxt =   Entry(stepOne)
outFileTxt.grid(row=1, column=1, columnspan=7, sticky="WE", pady=2)
outFileBtn =   Button(stepOne, text="Browse ...")
outFileBtn.grid(row=1, column=8, sticky='W', padx=5, pady=2)
inEncLbl =   Label(stepOne, text="Input File Encoding:")
inEncLbl.grid(row=2, column=0, sticky='E', padx=5, pady=2)
inEncTxt =   Entry(stepOne)
inEncTxt.grid(row=2, column=1, sticky='E', pady=2)
outEncLbl =   Label(stepOne, text="Output File Encoding:")
outEncLbl.grid(row=2, column=5, padx=5, pady=2)
outEncTxt =   Entry(stepOne)
outEncTxt.grid(row=2, column=7, pady=2)

helpLf = LabelFrame(app, text=" Quick Help ")
helpLf.grid(row=0, column=9, columnspan=2, rowspan=8, \
                sticky='NS', padx=5, pady=5)
helpLbl = Label(helpLf, text="Help will come - ask for it.")
helpLbl.grid(row=0)


app.title('scraping_twitter')
app.geometry('1200x950+22+33')

# Populate data
# populate_list()

# Start program
app.mainloop()


# To create an executable, install pyinstaller and run
# '''
# pyinstaller --onefile --add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk' --add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' part_manager.py
# '''


























# gui_frame=Frame(app,width=400,height=400)
# gui_frame.grid(row=6, column=1)
# place(x=200,y=200)
# part_text = StringVar()
# part_label = Label(app, text='Part Name', font=('bold', 14), pady=20)
# part_label.grid(row=0, column=0, sticky=W)
# part_entry = Entry(app, textvariable=part_text)
# part_entry.grid(row=0, column=1)
# # Customer
# customer_text = StringVar()
# customer_label = Label(app, text='Customer', font=('bold', 14))
# customer_label.grid(row=0, column=2, sticky=W)
# customer_entry = Entry(app, textvariable=customer_text)
# customer_entry.grid(row=0, column=3)
# # Retailer
# retailer_text = StringVar()
# retailer_label = Label(app, text='Retailer', font=('bold', 14))
# retailer_label.grid(row=1, column=0, sticky=W)
# retailer_entry = Entry(app, textvariable=retailer_text)
# retailer_entry.grid(row=1, column=1)
# # Price
# price_text = StringVar()
# price_label = Label(app, text='Price', font=('bold', 14))
# price_label.grid(row=1, column=2, sticky=W)
# price_entry = Entry(app, textvariable=price_text)
# price_entry.grid(row=1, column=3)
# Parts List (Listbox)

# parts_list = Listbox(app, height=8, width=50, border=0)
# parts_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)
# # Create scrollbar
# scrollbar = Scrollbar(app)
# scrollbar.grid(row=3, column=3)
# # Set scroll to listbox
# parts_list.configure(yscrollcommand=scrollbar.set)
# scrollbar.configure(command=parts_list.yview)
# # Bind select
# parts_list.bind('<<ListboxSelect>>', select_item)

# # Buttons
# add_btn = Button(app, text='Add Part', width=12, command=add_item)
# add_btn.grid(row=2, column=0, pady=20)

# remove_btn = Button(app, text='Remove Part', width=12, command=remove_item)
# remove_btn.grid(row=2, column=1)

# update_btn = Button(app, text='Update Part', width=12, command=update_item)
# update_btn.grid(row=2, column=2)

# clear_btn = Button(app, text='Clear Input', width=12, command=clear_text)
# clear_btn.grid(row=2, column=3)
# ////
# closeButton = Button(app, text="Close")
# closeButton.pack(side=RIGHT, padx=5, pady=5)
# okButton = Button(app, text="OK")
# okButton.pack(side=RIGHT)