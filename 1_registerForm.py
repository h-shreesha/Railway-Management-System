from tkinter import * 
from PIL import ImageTk, Image
import os


def delete3():
    admin_user_not_found_screen.destroy()


def login_success():
    global login_success_screen
    login_success_screen = Toplevel(screen2)
    login_success_screen.title("Success")
    login_success_screen.geometry("800x600")

    Label(login_success_screen, text=" Welcome to Western Railway", bg="blue", fg="white",
          width="300", height="2", font=("Helvetica", "16", "bold")).pack()
    Label(login_success_screen, text="").pack()

    Label(login_success_screen, text="Login is success").pack()
    Button(login_success_screen, text="OK", command=User_operation).pack()

# OPERATIONS TO BE PERFORMED BY USER

def User_operation():

    Label(login_success_screen, text=" ").pack()
    Label(login_success_screen, text=" ").pack()

    Button(login_success_screen, text='Check details of available trains', bg="yellow", height="2", width="50", font=(("Times", "12")), command=disp_train).pack()
    Label(login_success_screen, text='').pack()

    Button(login_success_screen, text='Book the tickets', bg="yellow", height="2", width="50", font=(("Times", "12")), command=book_tkts).pack()
    Label(login_success_screen, text='').pack()

    Button(login_success_screen, text='Delete ticket', bg="yellow", height="2", width="50", font=(("Times", "12")), command=delete_tkts).pack()
    Label(login_success_screen, text='').pack()

    Button(login_success_screen, text='Update tickets', bg="yellow", height="2", width="50", font=(("Times", "12")), command=update_tkts).pack()
    Label(login_success_screen, text='').pack()

    Button(login_success_screen, text='Display Profile', bg="yellow", height="2", width="50", font=(("Times", "12")), command=disp_profile).pack()
    Label(login_success_screen, text='').pack()

    Button(login_success_screen, text='Update profile', bg="yellow", height="2", width="50", font=(("Times", "12")), command=update_prof).pack()
    Label(login_success_screen, text='').pack()



def user_not_found():
    global screen4
    screen4 = Toplevel(screen2)
    screen4.title("Failed")
    screen4.geometry("400x400")

    Label(screen4, text=" Welcome to Western Railway", bg="blue", fg="white",
          width="300", height="2", font=("Helvetica", "16", "bold")).pack()
    Label(screen4, text="").pack()

    Label(screen4, text="Login failed. Please try again").pack()
    Button(screen4, text="OK", bg="yellow", height="2", width="50",
           font=(("Times", "12")), command=delete3).pack()

# WRITING TO FILE

def registerUser():
    username_info = userName.get()
    password_info = password.get()
    firstname_info = firstName.get()
    lastname_info = lastName.get()
    address_info = address.get()
    phoneno_info = phoneNo.get()
    emailid_info = emailId.get()

    file = open("Registration_info.txt", "a")
    file.write(username_info)
    file.write(" ")

    file.write(password_info)
    file.write(" ")

    file.write(firstname_info)
    file.write(" ")

    file.write(lastname_info)
    file.write(" ")

    file.write(address_info)
    file.write(" ")

    file.write(phoneno_info)
    file.write(" ")

    file.write(emailid_info)
    file.write("\n")
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)
    firstName_entry.delete(0, END)
    lastName_entry.delete(0, END)
    address_entry.delete(0, END)
    phoneNo_entry.delete(0, END)
    emailId_entry.delete(0, END)

    Label(screen1, text="Registration success", fg="green", font=("calibri", 11) ).pack()


def login_verify():
    
    username_login = username_verify.get()
    password_login = password_verify.get()

    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    for line in open("Registration_info.txt", "r").readlines():
        login_info = line.split()
        if username_login == login_info[0] and password_login == login_info[1]:
            login_success()
            return True
        
    user_not_found()


# STUDENT REGISTER

def register():
    
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("400x400")

    Label(screen1, text=" Welcome to Western Railway", bg="blue", fg="white",
          width="300", height="2", font=("Helvetica", "16", "bold")).pack()
    Label(screen1, text="").pack()

    global userName
    global password
    global firstName
    global lastName
    global address
    global phoneNo
    global emailId
    global username_entry
    global password_entry 
    global firstName_entry
    global lastName_entry
    global address_entry
    global phoneNo_entry
    global emailId_entry

    userName = StringVar()
    password = StringVar()
    firstName = StringVar()
    lastName = StringVar()
    address = StringVar()
    phoneNo = StringVar()
    emailId = StringVar()

    Label(screen1, text="Please enter the details below: ").pack()
    Label(screen1, text="").pack()

    Label(screen1, text="Username: ").pack()
    username_entry = Entry(screen1, textvariable=userName)
    username_entry.pack()
    
    Label(screen1, text="Password: ").pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()

    Label(screen1, text="First Name: ").pack()
    firstName_entry = Entry(screen1, textvariable=firstName)
    firstName_entry.pack()
    
    Label(screen1, text="Last Name: ").pack()
    lastName_entry = Entry(screen1, textvariable=lastName)
    lastName_entry.pack()

    Label(screen1, text="Address: ").pack()
    address_entry = Entry(screen1, textvariable=address)
    address_entry.pack()

    Label(screen1, text="Phone Number: ").pack()
    phoneNo_entry = Entry(screen1, textvariable=phoneNo)
    phoneNo_entry.pack()

    Label(screen1, text="Email Id: ").pack()
    emailId_entry = Entry(screen1, textvariable=emailId)
    emailId_entry.pack()
    Label(screen1, text="").pack()

    Button(screen1, text="Register", bg="yellow", height="2",
           width="50", font=(("Times", "12")), command=registerUser).pack()

# STUDENT LOGIN

def login_as_student():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("400x400")

    Label(screen2, text=" Welcome to Western Railway", bg="blue", fg="white",
          width="300", height="2", font=("Helvetica", "16", "bold")).pack()
    Label(screen2, text="").pack()

    Label(screen2, text="Please enter the details below to login ").pack()
    Label(screen2, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(screen2, text="Username: ").pack()
    username_login_entry = Entry(screen2, textvariable=username_verify)
    username_login_entry.pack()
    Label(screen2, text="").pack()

    Label(screen2, text="Password: ").pack()
    password_login_entry = Entry(screen2, textvariable=password_verify)
    password_login_entry.pack()
    Label(screen2, text="").pack()

    Button(screen2, text="Login", bg="yellow", height="2", width="50",
           font=(("Times", "12")), command=login_verify).pack()

# ADMIN OPERATIONS

def login_as_admin():
    global login_as_admin_screen
    login_as_admin_screen = Toplevel(screen)
    login_as_admin_screen.title("Login")
    login_as_admin_screen.geometry("500x500")

    Label(login_as_admin_screen, text=" Welcome to Western Railway", bg="blue", fg="white",
          width="300", height="2", font=("Helvetica", "16", "bold")).pack()
    Label(login_as_admin_screen, text="").pack()


    Label(login_as_admin_screen, text="Please enter the details below to login ").pack()
    Label(login_as_admin_screen, text="").pack()

    global admin_username_verify
    global admin_password_verify

    admin_username_verify = StringVar()
    admin_password_verify = StringVar()

    global admin_username_login_entry
    global admin_password_login_entry

    Label(login_as_admin_screen, text="Username: ").pack()
    admin_username_login_entry = Entry(
        login_as_admin_screen, textvariable=admin_username_verify)
    admin_username_login_entry.pack()
    Label(login_as_admin_screen, text="").pack()

    Label(login_as_admin_screen, text="Password: ").pack()
    admin_password_login_entry = Entry(
        login_as_admin_screen, textvariable=admin_password_verify)
    admin_password_login_entry.pack()
    Label(login_as_admin_screen, text="").pack()

    Button(login_as_admin_screen, text="Login", bg="yellow", height="2",
           width="50", font=(("Times", "12")), command=admin_login_verify).pack()


def admin_login_verify():

    admin_username_login = admin_username_verify.get()
    admin_password_login = admin_password_verify.get()

    admin_username_login_entry.delete(0, END)
    admin_password_login_entry.delete(0, END)

    for line in open("Admin_login.txt", "r").readlines():
        login_info = line.split()
        if admin_username_login == login_info[0] and admin_password_login == login_info[1]:
            admin_login_success()
            return True

    admin_user_not_found()


def admin_login_success():

    global admin_login_success_screen
    admin_login_success_screen = Toplevel(login_as_admin_screen)
    admin_login_success_screen.title("Success")
    admin_login_success_screen.geometry("500x500")

    Label(admin_login_success_screen, text=" Welcome to Western Railway", bg="blue", fg="white",
          width="300", height="2", font=("Helvetica", "16", "bold")).pack()
    Label( admin_login_success_screen, text="").pack()


    Label(admin_login_success_screen, text="Login is success").pack()
    Button(admin_login_success_screen, text="ok", command=admin_options).pack()


def admin_options():

    Label(admin_login_success_screen, text='').pack()
    Label(admin_login_success_screen, text='').pack()

    Button(admin_login_success_screen, admin_login_success_screen, text='Add new train', bg="yellow",
           height="2", width="50", font=(("Times", "12")), command=add_train).pack()
    Label(admin_login_success_screen, text='').pack()
    
    Button(admin_login_success_screen, text='Delete Existing train', bg="yellow",
           height="2", width="50", font=(("Times", "12")), command=delete_train).pack()
    Label(admin_login_success_screen, text='').pack()
    
# LINKING TO DIFFERENT FILES

def add_train():
    os.system('python 5_Admin_Add_Train.py')

def delete_train():
    os.system('python 6_Admin_Delete_Train.py')


def disp_train():
    os.system('python 7_Display_Trains.py')


def book_tkts():
    os.system('python 2_Book_Tickets.py')


def delete_tkts():
    os.system('python 3_Delete_Tickets.py')


def update_tkts():
    os.system('python 4_Update_Ticket.py')


def disp_profile():
    os.system('python 8_Display_Profile.py')


def update_prof():
    os.system('python 9_Update_Profile.py')


def admin_user_not_found():

    
    global admin_user_not_found_screen
    admin_user_not_found_screen = Toplevel(login_as_admin_screen)
    admin_user_not_found_screen.title("Failed")
    admin_user_not_found_screen.geometry("800x600")

    Label(admin_user_not_found_screen, text=" Welcome to Western Railway", bg="blue", fg="white", width="300", height="2", font=("Helvetica", "16", "bold")).pack()
    Label(admin_user_not_found_screen, text="").pack()

    Label(admin_user_not_found_screen, text="Login failed. Please try again").pack()

    Button(admin_user_not_found_screen, text="OK", bg="yellow", height="2", width="50", font=(("Times", "12")), command=delete3).pack()


# MAIN FUNCTION

def main_screen():

    global screen
    screen = Tk()
    screen.geometry("800x600")
    screen.title("Railway Managemt System")

    global image
    global photo
    global lable
    image = Image.open("Images/bckgrnd.jpg")
    photo = ImageTk.PhotoImage(image)
    lable = Label(image=photo)
    lable.place(x=0, y=0)
    
    
    Label(text=" Welcome to Western Railway", bg= "blue", fg="white", width="300", height="2", font=("Helvetica", "16", "bold")).pack()
    Label(text="").pack()

    Button(screen, text="Login As User", bg="yellow", height="2", width="50", font=(("Times", "12")), command=login_as_student).pack(side=TOP, padx=30, pady=20)
    
    Button(text="Register As User", bg="yellow", height="2", width="50", font=(("Times", "12")), command=register).pack()
    Label(text="").pack()
    Label(text="").pack()
    Label(text="").pack()
    Label(text="").pack()

    Button(screen, text="Login As Admin", bg="yellow", height="2", width="50", font=(("Times", "12")), command=login_as_admin).pack(side=TOP, padx=30, pady=50)


    screen.mainloop()

main_screen()
