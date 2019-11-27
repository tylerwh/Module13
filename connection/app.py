import tkinter
from tkinter import *
from tkinter import messagebox
import create_connection as cc


def create_db_and_tables():
  db_and_table_btn.config(state='disabled')
  global conn
  conn = cc.create_connection('db_files/human.db')
  print('Created human.db database')
  cc.create_tables('db_files/human.db')
  print('Created person and student tables')
  conn.close()


def add_person():
  # Check text fields not blank
  if firstname_text.get() == '' or lastname_text.get() == '':
    messagebox.showerror('Required Fields', 'First and Last name fields must not be left blank.')
    return
  
  global conn
  conn = cc.create_connection('db_files/human.db')
  person = (firstname_text.get(), lastname_text.get())
  cc.create_person(conn, person)


def add_student():
  # Check text fields not blank
  if firstname_text.get() == '' or lastname_text.get() == '' or major_text.get() == '' or startdate_text == '':
    messagebox.showerror('Required Fields', 'First and Last name fields must not be left blank.')
    return

  # Query person table using first and last name to get person_id
  global conn
  conn = cc.create_connection('db_files/human.db')
  print(type(firstname_text.get()))
  # person = (str(firstname_text.get()), str(lastname_text.get()))
  person_id = cc.find_person_id(conn, firstname_text.get(), lastname_text.get())
  print(person_id)


def view_persons():
  pass


def view_students():
  pass


app = Tk()
app.title('DB & GUI')

# Buttons
# Create DB and Tables
db_and_table_btn = Button(app, text='Create DB & Table', width=14, command=create_db_and_tables)
db_and_table_btn.grid(row=2, column=0, pady=3)

# Add Person
add_person_btn = Button(app, text='Add Person', width=14, command=add_person)
add_person_btn.grid(row=3, column=0, pady=3)

# Add Student
add_student_btn = Button(app, text='Add Student', width=14, command=add_student)
add_student_btn.grid(row=4, column=0, pady=3)

# View Person Table
view_pers_tbl_btn = Button(app, text='View Persons', width=14, command=view_persons)
view_pers_tbl_btn.grid(row=5, column=0, pady=3)

# View Student Table
view_student_tbl_btn = Button(app, text='View Students', width=14, command=view_students)
view_student_tbl_btn.grid(row=6, column=0, pady=3)

# Exit
exit_btn = Button(app, text='Exit', bg="red", fg="white", width=14, command=app.destroy)
exit_btn.grid(row=7, column=0, pady=3)

#Labels and Inputs
# First Name
firstname_text = StringVar()
firstname_lbl = Label(app, text='First Name', font=('bold', 12))
firstname_lbl.grid(row=3, column=1, sticky=W)
firstname_entry = Entry(app, textvariable=firstname_text)
firstname_entry.grid(row=3, column=2)

# Last Name
lastname_text = StringVar()
lastname_lbl = Label(app, text='Last Name', font=('bold', 12))
lastname_lbl.grid(row=3, column=3, sticky=W)
lastname_entry = Entry(app, textvariable=lastname_text)
lastname_entry.grid(row=3, column=4)

# Major
major_text = StringVar()
major_lbl = Label(app, text='Major', font=('bold', 12))
major_lbl.grid(row=5, column=1, sticky=W)
major_entry = Entry(app, textvariable=major_text)
major_entry.grid(row=5, column=2)

# Startdate
startdate_text = StringVar()
startdate_lbl = Label(app, text='Start Date', font=('bold', 12))
startdate_lbl.grid(row=5, column=3, sticky=W)
startdate_entry = Entry(app, textvariable=startdate_text)
startdate_entry.grid(row=5, column=4)

# Lists and Their Labels
# Person List Label
pers_list_lbl = Label(app, text='Persons List')
pers_list_lbl.grid(row=8, column=2, columnspan=2)
# Persons List (Listbox)
pers_list = Listbox(app, height=8, width=80)
pers_list.grid(row=9, column=0, columnspan=14, rowspan=4, pady=20, padx=20)
# Scrollbar Create
scroll_bar = Scrollbar(app)
scroll_bar.grid(row=9, column=6)
# Set scroll to listbox
pers_list.configure(yscrollcommand=scroll_bar.set)
scroll_bar.configure(command=pers_list.yview)

# Student List Label
student_list_lbl = Label(app, text='Student List')
student_list_lbl.grid(row=13, column=2, columnspan=2)
# Students List (Listbox)
student_list = Listbox(app, height=8, width=80)
student_list.grid(row=14, column=0, columnspan=14, rowspan=4, pady=20, padx=20)
# Scrollbar Create
scroll_bar = Scrollbar(app)
scroll_bar.grid(row=14, column=6)
# Set scroll to listbox
student_list.configure(yscrollcommand=scroll_bar.set)
scroll_bar.configure(command=student_list.yview)


app.geometry('550x600')
app.mainloop()
