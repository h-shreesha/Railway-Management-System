from tkinter import *
from tkcalendar import *


def delete3():
    failed_booking_screen.destroy()

def delete2():
    Successful_booking_screen.destroy()

def Successful_booking():

    global Successful_booking_screen
    Successful_booking_screen = Toplevel(main_screen)
    Successful_booking_screen.title("Successful Booking")
    Successful_booking_screen.geometry("500x500")

    Label(Successful_booking_screen, text=" Welcome to Western Railway", bg="blue", fg="white",
          width="300", height="2", font=("Helvetica", "16", "bold")).pack()
    Label(Successful_booking_screen, text="").pack()
    Label(Successful_booking_screen, text="Successfully Registered").pack()
    Label(Successful_booking_screen, text="").pack()

    Button(Successful_booking_screen, text="OK", bg="yellow", height="2",
           width="50", font=(("Times", "12")), command=delete2).pack()

    # Date_of_travel_info=Date_of_travel.get()
    person_name_info = person_name.get()
    no_of_tickets_info=no_of_tickets.get()
    compartment_info=clicked.get()
    reservation_info=clicked1.get()

    lable.config(text= cal.get_date())
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

def confirm_train():

    train_no_info=trainNo.get()
    board_point_info=boardingPoint.get()
    dest_point_info=destinationPoint.get()

    file=open("Train_details.txt", "r")
    for line in file:
        login_info=line.split()
        if train_no_info == login_info[0] and board_point_info == login_info[1] and dest_point_info == login_info[2]:
            book_train()
            return TRUE

    train_not_available()
    train_no_entry.delete(0,END)
    board_point_entry.delete(0, END)
    dest_point_entry.delete(0, END)


def book_train():

    global screen1
    screen1=Toplevel(main_screen)
    screen1.title("Book the Seat")
    screen1.geometry("900x900")

    Label(screen1, text=" Welcome to Western Railway", bg="blue", fg="white",
          width="300", height="2", font=("Helvetica", "16", "bold")).pack()
    Label(screen1, text="").pack()

    global person_name
    global Date_of_travel
    global no_of_tickets
    global compartment
    global reservation
    global person_name_entry
    global Date_of_travel_entry
    global no_of_tickets_entry
    global compartment_entry
    global reservation_entry

    person_name = StringVar()
    Date_of_travel=StringVar()
    no_of_tickets=StringVar()
    compartment=StringVar()
    reservation=StringVar()

    Label(screen1, text = "Please enter the details below: ").pack()
    Label(screen1, text = "").pack()
    Label(screen1, text = "").pack()

    Label(screen1, text="Enter the Name of person: ").pack()
    person_name_entry = Entry(screen1, textvariable= person_name)
    person_name_entry.pack()
    Label(screen1, text="").pack()

    Label(screen1, text = "Enter The Date of Travel (DD/MM/YY): ").pack()

    global cal
    global lable
    cal = Calendar(screen1, selectmode="day", year=2021, month=5, day=29)
    cal.pack()
    lable = Label(screen1, text="")
    lable.pack()

    Label(screen1, text = "Enter the Number of Seats: ").pack()
    no_of_tickets_entry=Entry(screen1, textvariable = no_of_tickets)
    no_of_tickets_entry.pack()
    Label(screen1, text = "").pack()

    Label(screen1, text = "Enter the Required Compartment: ").pack()
    global clicked
    clicked = StringVar()
    clicked.set("AC")

    drop = OptionMenu(screen1, clicked, "AC", "Firstclass", "Secondclass", "Thirdclass")
    drop.pack()
    
    Label(screen1, text = "Enter the Reservation Category: ").pack()
    global clicked1
    clicked1 = StringVar()
    clicked1.set("Men")

    drop1 = OptionMenu(screen1, clicked1, "Men", "Women", "Children", "Seniorcitizen", "Handicaped")
    drop1.pack()

    Label(screen1, text="").pack()
    Label(screen1, text="").pack()

    Button(screen1, text="Register", bg="yellow", height="2", width="50",
           font=(("Times", "12")), command=Successful_booking).pack()

def train_not_available():
    
    global failed_booking_screen
    failed_booking_screen = Toplevel(main_screen)
    failed_booking_screen.title("failed Booking")
    failed_booking_screen.geometry("500x500")

    Label(failed_booking_screen, text=" Welcome to Western Railway", bg="blue", fg="white",
          width="300", height="2", font=("Helvetica", "16", "bold")).pack()
    Label(failed_booking_screen, text="").pack()

    Label(failed_booking_screen, text="")
    Label(failed_booking_screen, text="The train is not available for this route").pack()
    Label(failed_booking_screen, text="").pack()

    Button(failed_booking_screen, text="OK", bg="yellow", height="2",
           width="50", font=(("Times", "12")), command=delete3).pack()




    # Label(main_screen, text="Booking success", fg="green", font=("calibri", 11)).pack()



def main_page():

    global main_screen
    global trainNo
    global boardingPoint
    global destinationPoint


    main_screen=Tk()
    main_screen.geometry("500x500")
    main_screen.title("Railway Managemt System")

    Label(text=" Welcome to Western Railway", bg="blue", fg="white",
          width="300", height="2", font=("Helvetica", "16", "bold")).pack()
    Label(text="").pack()

    global train_no_entry
    global board_point_entry
    global dest_point_entry

    Label(text = " Book Tickets", bg = "grey", width = "50",
          height = "2", font = ("Calibri", 10)).pack()
    Label(text = "").pack()
    Label(text = "").pack()
    Label(text = "").pack()

    trainNo=StringVar()
    Label(main_screen, text = "Enter the Train number: ").pack()

    train_no_entry=Entry(main_screen, textvariable = trainNo)
    train_no_entry.pack()
    Label(text = "").pack()
    Label(text = "").pack()

    boardingPoint=StringVar()
    Label(main_screen, text = "Enter the Boarding point: ").pack()

    board_point_entry=Entry(main_screen, textvariable = boardingPoint)
    board_point_entry.pack()
    Label(text = "").pack()
    Label(text = "").pack()

    destinationPoint=StringVar()
    Label(main_screen, text = "Enter the Destination point: ").pack()

    dest_point_entry=Entry(main_screen, textvariable = destinationPoint)
    dest_point_entry.pack()
    Label(text = "").pack()
    Label(text = "").pack()

    Button(main_screen, text="Book", bg="yellow", height="2", width="50", font=(("Times", "12")), command=confirm_train).pack()

    main_screen.mainloop()

main_page()
