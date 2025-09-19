from tkinter import *
from tkinter import messagebox

# Initialize main window
root = Tk()
root.geometry('700x550')
root.config(bg='#d3f3f5')
root.title('PythonGeeks Contact Book')
root.resizable(0, 0)

# Sample contact list
contactlist = [
    ['Siddharth Nigam', '369854712'],
    ['Gaurav Patil', '521155222'],
    ['Abhishek Nikam', '78945614'],
    ['Sakshi Gaikwad', '58745246'],
    ['Mohit Paul', '5846975'],
    ['Karan Patel', '5647892'],
    ['Sam Sharma', '89685320'],
    ['John Maheshwari', '98564785'],
    ['Ganesh Pawar', '85967412']
]

Name = StringVar()
Number = StringVar()

# Functions
def Selected():
    if len(select.curselection()) == 0:
        messagebox.showerror("Error", "Please Select the Name")
        return None
    else:
        return int(select.curselection()[0])

def AddContact():
    if Name.get() != "" and Number.get() != "":
        contactlist.append([Name.get(), Number.get()])
        Select_set()
        EntryReset()
        messagebox.showinfo("Confirmation", "Successfully Added New Contact")
    else:
        messagebox.showerror("Error", "Please fill the information")

def UpdateDetail():
    index = Selected()
    if index is not None:
        if Name.get() and Number.get():
            contactlist[index] = [Name.get(), Number.get()]
            Select_set()
            EntryReset()
            messagebox.showinfo("Confirmation", "Successfully Updated Contact")
        else:
            messagebox.showerror("Error", "Please fill the information")

def Delete_Entry():
    index = Selected()
    if index is not None:
        result = messagebox.askyesno('Confirmation', 'Do you want to delete the selected contact?')
        if result:
            del contactlist[index]
            Select_set()
            EntryReset()

def VIEW():
    index = Selected()
    if index is not None:
        NAME, PHONE = contactlist[index]
        Name.set(NAME)
        Number.set(PHONE)

def EntryReset():
    Name.set("")
    Number.set("")

def EXIT():
    root.destroy()

def Select_set():
    contactlist.sort()
    select.delete(0, END)
    for name, phone in contactlist:
        select.insert(END, name)

# GUI Layout
Label(root, text='Name', font=("Times new roman", 22, "bold"), bg='SlateGray3').place(x=30, y=20)
Entry(root, textvariable=Name, width=30).place(x=200, y=30)
Label(root, text='Contact No.', font=("Times new roman", 20, "bold"), bg='SlateGray3').place(x=30, y=70)
Entry(root, textvariable=Number, width=30).place(x=200, y=80)

Button(root, text="ADD", font='Helvetica 18 bold', bg='#e8c1c7', command=AddContact, padx=20).place(x=50, y=140)
Button(root, text="EDIT", font='Helvetica 18 bold', bg='#e8c1c7', command=UpdateDetail, padx=20).place(x=50, y=200)
Button(root, text="DELETE", font='Helvetica 18 bold', bg='#e8c1c7', command=Delete_Entry, padx=20).place(x=50, y=260)
Button(root, text="VIEW", font='Helvetica 18 bold', bg='#e8c1c7', command=VIEW).place(x=50, y=325)
Button(root, text="RESET", font='Helvetica 18 bold', bg='#e8c1c7', command=EntryReset).place(x=50, y=390)
Button(root, text="EXIT", font='Helvetica 24 bold', bg='tomato', command=EXIT).place(x=250, y=470)

# Listbox and Scrollbar
frame = Frame(root)
frame.pack(side=RIGHT)

scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, font=('Times new roman', 16), bg="#f0fffc", width=20, height=20, borderwidth=3, relief="groove")
scroll.config(command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT, fill=BOTH, expand=1)

Select_set()
root.mainloop()
