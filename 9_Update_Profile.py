from tkinter import *


def delete():
    user_not_recog_screen.destroy()

def delete2():
    Successful_update_screen.destroy()

def successful_update():

    global Successful_update_screen
    Successful_update_screen = Toplevel(main_screen)
    Successful_update_screen.title("Successful Booking")
    Successful_update_screen.geometry("500x500")

    Label(Successful_update_screen, text=" Welcome to Western Railway", bg="blue", fg="white",
          width="300", height="2", font=("Helvetica", "16", "bold")).pack()
    Label(Successful_update_screen, text="").pack()

    Label(Successful_update_screen, text="Profile Updated Successfully").pack()
    Label(Successful_update_screen, text="").pack()

    Button(Successful_update_screen, text="OK", bg="yellow", height="2",
           width="50", font=(("Times", "12")), command=delete2).pack()

    update_prof_uname = user_name.get()
    update_prof_pas = passWord.get()
    update_prof_fname = first_name.get()
    update_prof_lname = last_name.get()
    update_prof_add = address.get()
    update_prof_ph = phone_no.get()
    update_prof_eid = email_id.get()

    file = open("Registration_info.txt", "a")
    file.write(update_prof_uname)
    file.write(" ")

    file.write(update_prof_pas)
    file.write(" ")

    file.write(update_prof_fname)
    file.write(" ")

    file.write(update_prof_lname)
    file.write(" ")

    file.write(update_prof_add)
    file.write(" ")

    file.write(update_prof_ph)
    file.write(" ")

    file.write(update_prof_eid)
    file.write(" ")
    file.write("\n")

def confirm_update():
    
    user_name_info = userName.get()
    password_info = password.get()
    
    for line in open("Registration_info.txt", "r").readlines():
        login_info = line.split()
        if user_name_info == login_info[0] and password_info == login_info[1]:
            login_success(user_name_info , password_info)
            return TRUE
    user_not_recognised()


def delete_existing(personName):
    temp = list()
    fhand = open("Registration_info.txt", "r")
    data = fhand.read()
    fhand.close()
    records = data.split('\n')
    for record in records:
        if record.startswith(personName):
            continue
        else:
            temp.append(record)
    del temp[-1]

    fhand = open("Registration_info.txt", "w")
    for record in temp:
        fhand.write(record)
        fhand.write('\n')


def login_success(user_name_infoo, password_infoo):
    global login_success_screen
    login_success_screen = Toplevel(main_screen)

    login_success_screen.title('Railway management')
    login_success_screen.geometry('512x512')
    Label(text='').pack()

    Label(login_success_screen, text=" Welcome to Western Railway", bg="blue", fg="white",
          width="300", height="2", font=("Helvetica", "16", "bold")).pack()
    Label(login_success_screen, text="").pack()
    Label(login_success_screen, text='Update Your Profile:',
          font='verdana').pack()
    Label(text='').pack()

    global user_name
    global first_name
    global last_name
    global address
    global phone_no
    global email_id
    global passWord

    user_name = StringVar()
    first_name = StringVar()
    last_name = StringVar()
    address = StringVar()
    phone_no = StringVar()
    email_id = StringVar()
    passWord = StringVar()

    for line in open("Registration_info.txt", "r").readlines():
        login_info = line.split()
        if user_name_infoo == login_info[0] and password_infoo == login_info[1]:
            uName = user_name_infoo
            delete_existing(user_name_infoo)
            
            Label(login_success_screen, text="Enter the User Name: ").pack()
            user_name_entry = Entry( login_success_screen, textvariable=user_name)
            user_name_entry.pack()
            Label(login_success_screen, text="").pack()

            Label(login_success_screen, text="Enter the First Name: ").pack()
            first_name_entry = Entry( login_success_screen, textvariable=first_name)
            first_name_entry.pack()
            Label(login_success_screen, text="").pack()

            Label(login_success_screen, text="Enter the last Name: ").pack()
            last_name_entry = Entry( login_success_screen, textvariable=last_name)
            last_name_entry.pack()
            Label(login_success_screen, text="").pack()

            Label(login_success_screen, text="Enter the address: ").pack()
            address_entry = Entry( login_success_screen, textvariable=address)
            address_entry.pack()
            Label(login_success_screen, text="").pack()

            Label(login_success_screen, text="Enter the phone number: ").pack()
            phone_no_entry = Entry( login_success_screen, textvariable=phone_no)
            phone_no_entry.pack()
            Label(login_success_screen, text="").pack()

            Label(login_success_screen, text="Enter the Email id: ").pack()
            email_id_entry = Entry( login_success_screen, textvariable=email_id)
            email_id_entry.pack()
            Label(login_success_screen, text="").pack()

            Label(login_success_screen, text="Enter the Password: ").pack()
            passWord_entry = Entry( login_success_screen, textvariable=passWord)
            passWord_entry.pack()
            Label(login_success_screen, text="").pack()

            Button(login_success_screen, text="Update Profile", bg="yellow", height="2", width="50", font=(("Times", "12")), command=successful_update).pack()
            Label(login_success_screen, text="").pack()


            


def user_not_recognised():

    global user_not_recog_screen
    user_not_recog_screen = Toplevel(main_screen)
    user_not_recog_screen.title('Railway management')
    user_not_recog_screen.geometry('312x312')

    Label(user_not_recog_screen, text=" Welcome to Western Railway", bg="blue", fg="white",
          width="300", height="2", font=("Helvetica", "16", "bold")).pack()
    Label(user_not_recog_screen, text="").pack()

    Label(user_not_recog_screen,
          text='Invalid Credentials!', font='verdana').pack()

    Button(user_not_recog_screen, text='Please Try Again :)', bg="yellow", height="2", width="50", font=(("Times", "12")),
           command=delete).pack()




def main_page():

    global main_screen
    main_screen = Tk()
    main_screen.geometry("800x600")
    main_screen.title("Railway Managemt System")

    Label(text=" Welcome to Western Railway", bg="blue", fg="white",
          width="300", height="2", font=("Helvetica", "16", "bold")).pack()
    Label(text="").pack()

    Label(text=" Update Profile", bg="grey", width="50",
          height="2", font=("Calibri", 10)).pack()
    Label(text="").pack()
    Label(text="").pack()
    Label(text="").pack()

    global userName
    global userName_entry
    global password
    global password_entry

    userName = StringVar()
    Label(main_screen, text="Enter the User Name: ").pack()

    userName_entry = Entry(main_screen, textvariable=userName)
    userName_entry.pack()
    Label(text="").pack()

    password = StringVar()
    Label(main_screen, text="Enter the password: ").pack()

    password_entry = Entry(main_screen, textvariable=password)
    password_entry.pack()
    Label(text="").pack()
    Label(text="").pack()

    Button(main_screen, text="Update Profile", bg="yellow", height="2",
           width="50", font=(("Times", "12")), command=confirm_update).pack()
    Label(text="").pack()

    main_screen.mainloop()


main_page()
