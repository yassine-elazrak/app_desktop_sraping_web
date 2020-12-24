# import tkinter as tk

# class EntryWithPlaceholder(tk.Entry):
#     def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey'):
#         super().__init__(master)

#         self.placeholder = placeholder
#         self.placeholder_color = color
#         self.default_fg_color = self['fg']

#         self.bind("<FocusIn>", self.foc_in)
#         self.bind("<FocusOut>", self.foc_out)

#         self.put_placeholder()

#     def put_placeholder(self):
#         self.insert(0, self.placeholder)
#         self['fg'] = self.placeholder_color

#     def foc_in(self, *args):
#         if self['fg'] == self.placeholder_color:
#             self.delete('0', 'end')
#             self['fg'] = self.default_fg_color

#     def foc_out(self, *args):
#         if not self.get():
#             self.put_placeholder()

# if __name__ == "__main__": 
#     root = tk.Tk() 
#     username = EntryWithPlaceholder(root, "username")
#     password = EntryWithPlaceholder(root, "password", 'blue')
#     username.pack()
#     password.pack()  
#     root.mainloop()




from tkinter import *
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
if __name__ == '__main__':
   root = Tk()
   lng = Checkbar(root, ['Python', 'Ruby', 'Perl', 'C++'])
#    tgl = Checkbar(root, ['English','German'])
   lng.pack(side=TOP,  fill=X)
#    tgl.pack(side=LEFT)
   lng.config(relief=GROOVE, bd=2)

   def allstates(): 
      print(list(lng.state()))
    #   , list(tgl.state()))
   Button(root, text='Quit', command=root.quit).pack(side=RIGHT)
   Button(root, text='Peek', command=allstates).pack(side=RIGHT)
   root.mainloop()

    



# from tkinter import *
# from tkinter import messagebox
# gui=Tk()
# ##gui.state("zoomed")
# gui.geometry("1080x1080")
# gui.title("GUI2")
# gui['bg']="red"
# gui_frame=Frame(gui,width=700,height=700)
# gui_frame.place(x=200,y=200)

# label=Label(gui_frame,text="Student Login Page",font=("arial","20","bold"),bg="blue").place(x=250,y=10)
# label_user_id=Label(gui_frame,text="User Id:",font=("arial","12","bold")).place(x=100,y=200)
# label_password=Label(gui_frame,text="Password:",font=("arial","12","bold")).place(x=100,y=300)

# entry_user_id=Entry(gui_frame,font=("arial","12","bold")).place(x=200,y=200)
# entry_password=Entry(gui_frame,show="*",font=("arial","12","bold")).place(x=200,y=300)


# def verify():
# ##    x=entry_user_id
# ##    y=entry_password
# ##    
# ##    if(x=="User" and y=="12345"):
#         messagebox.showinfo(title="Welcome",message="Welcome User")
# ##    else:
# ##        messagebox.showinfo(title="Sorry",message="Try again!!")



# btn_login=Button(gui_frame,text='Login',font=("arial","12","bold"),command=verify)
# btn_login.place(x=400,y=400)


# gui.mainloop()