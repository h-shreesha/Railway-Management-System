from tkinter import *


def login_verify():

    userName_info = userName.get()
    password_info = password.get()

    for line in open("Registration_info.txt", "r").readlines():
        login_info = line.split()
        if userName_info == login_info[0] and password_info == login_info[1]:
            login_success(userName_info, password_info)
            return TRUE
    credentials_not_recognised()


def credentials_not_recognised():

    global credentials_not_recog_screen
    credentials_not_recog_screen = Toplevel(main_screen)
    credentials_not_recog_screen.title('Login Error | Railway Management')
    credentials_not_recog_screen.geometry('800x600')

    Label(credentials_not_recog_screen, text=" Welcome to Western Railway", bg="blue", fg="white",
          width="300", height="2", font=("Helvetica", "16", "bold")).pack()
    Label(credentials_not_recog_screen, text="").pack()

    Label(credentials_not_recog_screen, text='Invalid Credentials!', font='verdana').pack()
    Button(credentials_not_recog_screen, text='Try Again', bg="yellow",
           height="2", width="50", font=(("Times", "12")), command=delete2).pack()


def delete2():
    credentials_not_recog_screen.destroy()


def login_success(userName_infoo, password_infoo):

    global login_success_screen
    login_success_screen = Toplevel(main_screen)
    login_success_screen.title('Railway Management | Display Profile')
    login_success_screen.geometry('800x700')

    Label(login_success_screen, text=" Welcome to Western Railway", bg="blue", fg="white", width="300", height="2", font=("Helvetica", "16", "bold")).pack()
    Label(login_success_screen, text="").pack()

    Label(login_success_screen, text='Your Details Are:', font='verdana').pack()
    Label(login_success_screen, text='').pack()

    for line in open("Registration_info.txt", "r").readlines():
        login_info = line.split()
        if userName_infoo == login_info[0] and password_infoo == login_info[1]:
            Label(login_success_screen, text='User Name:', font='verdana').pack()
            # Label(login_success_screen, text='').pack()
            # Label(login_success_screen, text='').pack()

            Label(login_success_screen, text=login_info[0], font='verdana').pack()
            Label(login_success_screen, text='').pack()
            Label(login_success_screen, text='').pack()

            Label(login_success_screen, text='First Name:', font='verdana').pack()
            # Label(login_success_screen, text='').pack()
            # Label(login_success_screen, text='').pack()

            Label(login_success_screen, text=login_info[2], font='verdana').pack()
            Label(login_success_screen, text='').pack()
            Label(login_success_screen, text='').pack()

            Label(login_success_screen, text='Last Name:', font='verdana').pack()
            # Label(login_success_screen, text='').pack()
            # Label(login_success_screen, text='').pack()

            Label(login_success_screen, text=login_info[3], font='verdana').pack()
            Label(login_success_screen, text='').pack()
            Label(login_success_screen, text='').pack()

            Label(login_success_screen, text='address:', font='verdana').pack()
            # Label(login_success_screen, text='').pack()
            # Label(login_success_screen, text='').pack()

            Label(login_success_screen, text=login_info[4], font='verdana').pack()
            Label(login_success_screen, text='').pack()
            Label(login_success_screen, text='').pack()

            Label(login_success_screen, text='Phone No:', font='verdana').pack()
            # Label(login_success_screen, text='').pack()
            # Label(login_success_screen, text='').pack()

            Label(login_success_screen, text=login_info[5], font='verdana').pack()
            Label(login_success_screen, text='').pack()
            Label(login_success_screen, text='').pack()

            Label(login_success_screen, text='Email:', font='verdana').pack()
            # Label(login_success_screen, text='').pack()
            # Label(login_success_screen, text='').pack()

            Label(login_success_screen, text=login_info[6], font='verdana').pack()
            Label(login_success_screen, text='').pack()
            Label(login_success_screen, text='').pack()
        else:
            continue

    Button(login_success_screen, text='OK', bg="yellow", height="2",
           width="50", font=(("Times", "12")), command=delete1).pack()


def delete1():
    login_success_screen.destroy()



def main_page():
    global main_screen
    
    main_screen = Tk()
    main_screen.geometry("500x500")

    Label(text=" Welcome to Western Railway", bg="blue", fg="white",
          width="300", height="2", font=("Helvetica", "16", "bold")).pack()
    Label(text="").pack()
    Label(text='').pack()
    Label(text='').pack()

    global userName
    global userName_entry
    global password
    global password_entry

    userName = StringVar()
    password = StringVar()

    Label(main_screen, text="Enter the User Name:",
          font='verdana').pack()
    Label(text='').pack()
    Label(text='').pack()

    userName_entry = Entry(main_screen, textvariable=userName)
    userName_entry.pack()
    Label(text=' ').pack()

    Label(main_screen, text="Enter the Password:",
          font='verdana').pack()
    Label(text='').pack()
    Label(text='').pack()

    password_entry = Entry(main_screen, textvariable=password)
    password_entry.pack()
    Label(text=' ').pack()

    Button(text='Enter', bg="yellow", height="2", width="50", font=(("Times", "12")), command=login_verify).pack()
    Label(text='').pack()

    main_screen.mainloop()


main_page()
