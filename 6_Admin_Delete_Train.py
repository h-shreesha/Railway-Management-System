from tkinter import *


def delete():
    train_no_not_recog_screen.destroy()

def confirm_delete():

    train_no_info = trainNumber.get()
    
    for line in open("Train_details.txt", "r").readlines():
        login_info = line.split()
        if train_no_info == login_info[0]:
            login_success(train_no_info)
            return TRUE
    train_not_recognised()


def login_success(train_no_info):

    global login_success_screen
    login_success_screen = Toplevel(main_screen)

    login_success_screen.title('Railway management | Delete Train')
    login_success_screen.geometry('500x500')
    Label(text='').pack()

    Label(login_success_screen, text=" Welcome to Western Railway", bg="blue", fg="white",
          width="300", height="2", font=("Helvetica", "16", "bold")).pack()
    Label(login_success_screen, text="").pack()

    Label(login_success_screen, text='Train Deleted successfully:',
          font='verdana').pack()
    Label(text='').pack()
    temp = list()
    fhand = open("Train_details.txt", "r")
    data = fhand.read()
    fhand.close()
    records = data.split('\n')
    for record in records:
        if record.startswith(train_no_info):
            continue
        else:
            temp.append(record)
    del temp[-1]

    fhand = open("Train_details.txt", "w")
    for record in temp:
        fhand.write(record)
        fhand.write('\n')


def train_not_recognised():
    
    global train_no_not_recog_screen
    train_no_not_recog_screen = Toplevel(main_screen)
    train_no_not_recog_screen.title('Not recognised')
    train_no_not_recog_screen.geometry('312x312')

    Label(train_no_not_recog_screen, text=" Welcome to Western Railway", bg="blue", fg="white",
          width="300", height="2", font=("Helvetica", "16", "bold")).pack()
    Label(train_no_not_recog_screen, text="").pack()

    Label(train_no_not_recog_screen,
          text='Invalid Credentials!', font='verdana').pack()

    Button(train_no_not_recog_screen, text='Please Try Again :)', bg="yellow", height="2", width="50", font=(("Times", "12")), command=delete).pack()

def main_page():

    global main_screen

    main_screen = Tk()
    main_screen.geometry("800x600")
    main_screen.title("Railway Managemt System | Delete train")

    Label(text="").pack()
    Label(text="").pack()
    Label(text="").pack()

    Label(text=" Welcome to Western Railway", bg="blue", fg="white",
          width="300", height="2", font=("Helvetica", "16", "bold")).pack()
    Label(text="").pack()

    Label(text=" Cancel Train", bg="grey", width="50",
          height="2", font=("Calibri", 10)).pack()
    Label(text="").pack()
    Label(text="").pack()
    Label(text="").pack()

    global trainNumber
    global trainNumber_entry

    trainNumber = StringVar()
    Label(main_screen, text="Enter the Id of Train: ").pack()

    trainNumber_entry = Entry(main_screen, textvariable= trainNumber)
    trainNumber_entry.pack()
    Label(text="").pack()
    Label(text="").pack()

    Button(main_screen, text="Delete Train", bg="yellow", height="2",
           width="50", font=(("Times", "12")), command=confirm_delete).pack()
    Label(text="").pack()

    main_screen.mainloop()


main_page()
