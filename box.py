from tkinter import *
  
  
# create a root window. 
app = Tk() 
  
# create listbox object 
listbox = Listbox(app, height = 10,  
                  width = 15,  
                  bg = "grey", 
                  activestyle = 'dotbox',  
                  font = "Helvetica", 
                  fg = "yellow") 
  
# Define the size of the window. 
app.geometry("300x250")   
  
# Define a label for the list.   
label = Label(app, text = " FOOD ITEMS")  
i = 0
  
# insert elements by their 
# index and names. 
listbox.insert(1, "Nachos") 
listbox.insert(2, "Sandwich") 
listbox.insert(3, "Burger") 
listbox.insert(4, "Pizza") 
listbox.insert(5, "Burrito") 
  
def remove():
    listbox.delete(END)
def add():
    # print(i)
    global i
    listbox.insert(END,str(i))
    i = i + 1
    # customer_entry.get)

# customer_text = StringVar()
# customer_entry = Entry(app, textvariable=customer_text)
# customer_entry.grid(row=0, column=3)

remove_btnc = Button(app, text='Remove word', width=12, command=remove)
remove_btnc.pack()
remove_btn = Button(app, text='add Part', width=12, command=add)
remove_btn.pack()
Button(app, text='Quit').pack(side=RIGHT)
Button(app, text='Peek').pack(side=RIGHT)
  
# pack the widgets 
label.pack() 
listbox.pack() 
  
  
# Display untill User  
# exits themselves. 
app.mainloop() 