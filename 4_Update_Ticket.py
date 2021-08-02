from tkinter import *
from tkcalendar import *


def delete2():
    Successful_update_screen.destroy()

def confirm_update():
    global date
    person_name_info = personName.get()
    lable.config(text=cal.get_date())
    date = cal.get_date()

    for line in open("reserve_seat.txt", "r").readlines():
        login_info = line.split()
        if person_name_info == login_info[0] and date == login_info[1]:
            login_success(person_name_info)
            return TRUE
    person_not_recognised()


def Successful_update():

    global Successful_update_screen
    Successful_update_screen = Toplevel(main_screen)
    Successful_update_screen.title("Successful Booking")
    Successful_update_screen.geometry("500x500")

    Label(Successful_update_screen, text=" Welcome to Western Railway", bg="blue", fg="white",
          width="300", height="2", font=("Helvetica", "16", "bold")).pack()
    Label(Successful_update_screen, text="").pack()

    Label(Successful_update_screen, text="Successfully Updated").pack()
    Label(Successful_update_screen, text="").pack()

    Button(Successful_update_screen, text="OK", bg="yellow", height="2",
           width="50", font=(("Times", "12")), command=delete2).pack()

    # Date_of_travel_info=Date_of_travel.get()
    person_name_info = personName.get()
    no_of_tickets_info = no_of_tickets.get()
    compartment_info = clicked.get()
    reservation_info = clicked1.get()

    lable.config(text=cal.get_date())
    date = cal.get_date()
    file = open("reserve_seat.txt", "a")
    file.write(person_name_info)
    file.write(" ")

    file.write(date)
    file.write(" ")

    file.write(no_of_tickets_info)
    file.write(" ")

    file.write(compartment_info)
    file.write(" ")

    file.write(reservation_info)
    file.write("\n")
    file.close()

    # Date_of_travel_entry.delete(0, END)
    no_of_tickets_entry.delete(0, END)
    # compartment_entry.delete(0, END)
    # reservation_entry.delete(0, END)


def person_not_recognised():
    global person_not_recog_screen
    person_not_recog_screen = Toplevel(main_screen)
    person_not_recog_screen.title('Railway management')
    person_not_recog_screen.geometry('500x500')

    Label(person_not_recog_screen, text=" Welcome to Western Railway", bg="blue", fg="white",
          width="300", height="2", font=("Helvetica", "16", "bold")).pack()
    Label(person_not_recog_screen, text="").pack()

    Label(person_not_recog_screen,
          text='Invalid Credentials!', font='verdana').pack()

    Button(person_not_recog_screen, text='Please Try Again :)', bg="yellow", height="2", width="50", font=(("Times", "12")), command=delete).pack()

def delete():
    person_not_recog_screen.destroy()

def delete_existing(personName):
    temp = list()
    fhand = open("reserve_seat.txt", "r")
    data = fhand.read()
    fhand.close()
    records = data.split('\n')
    for record in records:
        if record.startswith(personName):
            continue
        else:
            temp.append(record)
    del temp[-1]

    fhand = open("reserve_seat.txt", "w")
    for record in temp:
        fhand.write(record)
        fhand.write('\n')


def login_success(personName):

    global login_success_screen
    login_success_screen = Toplevel(main_screen)

    login_success_screen.title('Railway management')
    login_success_screen.geometry('512x512')
    Label(text='').pack()

    Label(login_success_screen, text=" Welcome to Western Railway", bg="blue", fg="white",
          width="300", height="2", font=("Helvetica", "16", "bold")).pack()
    Label(login_success_screen, text="").pack()
    Label(login_success_screen, text='Ticket Details are:',
          font='verdana').pack()
    Label(text='').pack()

    global uName
    global no_of_tickets
    global compartment
    global reservation
    global no_of_tickets_entry
    global compartment_entry
    global reservation_entry
    

    no_of_tickets = StringVar()
    compartment = StringVar()
    reservation = StringVar()


    for line in open("reserve_seat.txt", "r").readlines():
        login_info = line.split()
        if personName == login_info[0] and date == login_info[1]:
            uName = personName
            delete_existing(personName)

            Label(text='').pack()
            Label(login_success_screen, text='Name of The Person: ', font='verdana', fg='blue').pack()

            Label(text='').pack()
            Label(text='').pack()
            Label(login_success_screen, text=login_info[0], font='verdana').pack()
            Label(text='').pack()
            Label(text='').pack()

            Label(login_success_screen, text='Enter the date:', font='verdana').pack()
            Label(text='').pack()
            Label(text='').pack()

            cal = Calendar(main_screen, selectmode="day", year=2021, month=5, day=29)
            cal.pack()
            lable = Label(main_screen, text="")
            lable.pack()

            Label(login_success_screen, text="Enter the Number of Seats: ").pack()
            no_of_tickets_entry = Entry(login_success_screen, textvariable=no_of_tickets)
            no_of_tickets_entry.pack()
            Label(login_success_screen, text="").pack()

            Label(login_success_screen, text="Enter the Required Compartment: ").pack()
            Label(login_success_screen, text="Enter the Required Compartment: ").pack()
            global clicked
            clicked = StringVar()
            clicked.set("AC")

            drop = OptionMenu(login_success_screen, clicked, "AC", "Firstclass",
                      "Secondclass", "Thirdclass")
            drop.pack()


            Label(login_success_screen, text="Enter the Reservation Category: ").pack()
            global clicked1
            clicked1 = StringVar()
            clicked1.set("Men")

            drop1 = OptionMenu(login_success_screen, clicked1, "Men", "Women",
                       "Children", "Seniorcitizen", "Handicaped")
            drop1.pack()

            Label(login_success_screen, text="").pack()
            Label(login_success_screen, text="").pack()

            Button(login_success_screen, text="Register", bg="yellow", height="2",
                   width="50", font=(("Times", "12")), command=Successful_update).pack()




def main_page():

    global main_screen
    main_screen = Tk()
    main_screen.geometry("500x600")
    main_screen.title("Railway Managemt System")

    Label(text=" Welcome to Western Railway", bg="blue", fg="white",
          width="300", height="2", font=("Helvetica", "16", "bold")).pack()
    Label(text="").pack()

    Label(text=" Update Tickets", bg="grey", width="50",
          height="2", font=("Calibri", 10)).pack()
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

    Button(main_screen, text="Update Ticket", bg="yellow", height="2",
           width="50", font=(("Times", "12")), command=confirm_update).pack()
    Label(text="").pack()

    main_screen.mainloop()


main_page()
