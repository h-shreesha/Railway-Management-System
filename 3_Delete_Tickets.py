from tkinter import *
from tkcalendar import *


def confirm_cancel():
    person_name_info = personName.get()
    lable.config(text=cal.get_date())
    date = cal.get_date()

    for line in open("reserve_seat.txt", "r").readlines():
        login_info = line.split()
        if person_name_info == login_info[0] and date == login_info[1]:
            login_success(person_name_info)
            return TRUE
    person_not_recognised()


def login_success(person_name_info):

    global login_success_screen
    login_success_screen = Toplevel(main_screen)

    login_success_screen.title('Railway management')
    login_success_screen.geometry('512x512')
    Label(text='').pack()

    Label(login_success_screen, text=" Welcome to Western Railway", bg="blue", fg="white",
          width="300", height="2", font=("Helvetica", "16", "bold")).pack()
    Label(login_success_screen, text="").pack()

    Label(login_success_screen, text='Ticket Deleted successfully:' ,font='verdana').pack()
    Label(text='').pack()
    temp = list()
    fhand = open("reserve_seat.txt", "r")
    data = fhand.read()
    fhand.close()
    records = data.split('\n')
    for record in records:
        if record.startswith(person_name_info):
            continue
        else:
            temp.append(record)
    del temp[-1]

    fhand = open("reserve_seat.txt", "w")
    for record in temp:
        fhand.write(record)
        fhand.write('\n')


def person_not_recognised():

    global password_not_recog_screen
    password_not_recog_screen = Toplevel(main_screen)
    password_not_recog_screen.title('Not recognised')
    password_not_recog_screen.geometry('312x312')

    Label(password_not_recog_screen, text=" Welcome to Western Railway", bg="blue", fg="white",
          width="300", height="2", font=("Helvetica", "16", "bold")).pack()
    Label(password_not_recog_screen, text="").pack()

    Label(password_not_recog_screen, text='Invalid Credentials!', font='verdana').pack()

    Button(password_not_recog_screen, text='Please Try Again :)', bg="yellow",
           height="2", width="50", font=(("Times", "12")), command=delete).pack()

def delete():
    password_not_recog_screen.destroy()

def main_page():

    global main_screen

    main_screen = Tk()
    main_screen.geometry("500x700")
    main_screen.title("Railway Managemt System")

    Label(text=" Welcome to Western Railway", bg="blue", fg="white",
          width="300", height="2", font=("Helvetica", "16", "bold")).pack()
    Label(text="").pack()

    Label(text=" Cancel Tickets", bg="grey", width="50", height="2", font=("Calibri", 10)).pack()
    Label(text="").pack()
    Label(text="").pack()
    Label(text="").pack()

    global personName
    global personName_entry

    personName = StringVar()
    Label(main_screen, text="Enter the Name of the person: ").pack()

    personName_entry = Entry(main_screen, textvariable=personName)
    personName_entry.pack()
    Label(text="").pack()
    Label(text="").pack()

    Label(main_screen, text="Enter The Date of Travel (DD/MM/YY): ").pack()

    global cal
    global lable
    cal = Calendar(main_screen, selectmode="day", year=2021, month=5, day=29)
    cal.pack()
    lable = Label(main_screen, text="")
    lable.pack()
    Label(text="").pack()
    Label(text="").pack()

    Button(main_screen, text="Delete Ticket", bg="yellow", height="2",
           width="50", font=(("Times", "12")), command=confirm_cancel).pack()
    Label(text="").pack()

    main_screen.mainloop()


main_page()
