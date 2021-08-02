from tkinter import *


def delete2():
    train_exist_screen.destroy()

def Add_train():
    train_no_info = trainNo.get()
    boarding_point_info = boardingPoint.get()
    destination_point_info = destinationPoint.get()

    train_no_entry.delete(0, END)
    board_point_entry.delete(0, END)
    dest_point_entry.delete(0, END)

    for line in open("Train_details.txt", "r").readlines():
        login_info = line.split()
        if train_no_info == login_info[0]:
            train_exist()
            return TRUE
    insert_new_train(train_no_info, boarding_point_info, destination_point_info)


def train_exist():

    global train_exist_screen
    train_exist_screen = Toplevel(main_screen)
    train_exist_screen.title("Train exist")
    train_exist_screen.geometry("500x500")

    Label(train_exist_screen, text=" Welcome to Western Railway", bg="blue", fg="white",
          width="300", height="2", font=("Helvetica", "16", "bold")).pack()
    Label( train_exist_screen, text="").pack()

    Label(train_exist_screen, text="The train you are trying to add is already exist").pack()
    Label(train_exist_screen, text="").pack()

    Button(train_exist_screen, text="OK", bg="yellow", height="2",
           width="50", font=(("Times", "12")), command=delete2).pack()


def insert_new_train(train_no_infoo, boarding_point_infoo, destination_point_infoo):

    global insert_new_train_screen
    insert_new_train_screen = Toplevel(main_screen)
    insert_new_train_screen.title('Update Train')
    insert_new_train_screen.geometry('400x400')

    Label(insert_new_train_screen, text=" Welcome to Western Railway", bg="blue", fg="white",
          width="300", height="2", font=("Helvetica", "16", "bold")).pack()
    Label(insert_new_train_screen, text="").pack()

    Label(insert_new_train_screen, text='Train Added Succesfully!',
          font='verdana', fg='blue').pack()
    
    file = open('Train_details.txt', 'a')
    file.write(train_no_infoo)
    file.write(" ")
    file.write(boarding_point_infoo)
    file.write(" ")
    file.write(destination_point_infoo)
    file.write(" ")
    file.write("\n")
    


def main_page():

    global main_screen
    global trainNo
    global boardingPoint
    global destinationPoint

    main_screen = Tk()
    main_screen.geometry("500x500")
    main_screen.title("Railway Managemt System")

    Label(text=" Welcome to Western Railway", bg="blue", fg="white",
          width="300", height="2", font=("Helvetica", "16", "bold")).pack()
    Label(text="").pack()

    global train_no_entry
    global board_point_entry
    global dest_point_entry

    Label(text=" Enter the details of the train to be added ", bg="grey", width="50",
          height="2", font=("Calibri", 10)).pack()
    Label(text="").pack()
    Label(text="").pack()
    Label(text="").pack()

    trainNo = StringVar()
    Label(main_screen, text="Enter the Train number: ").pack()

    train_no_entry = Entry(main_screen, textvariable=trainNo)
    train_no_entry.pack()
    Label(text="").pack()
    Label(text="").pack()

    boardingPoint = StringVar()
    Label(main_screen, text="Enter the Boarding point: ").pack()

    board_point_entry = Entry(main_screen, textvariable=boardingPoint)
    board_point_entry.pack()
    Label(text="").pack()
    Label(text="").pack()

    destinationPoint = StringVar()
    Label(main_screen, text="Enter the Destination point: ").pack()

    dest_point_entry = Entry(main_screen, textvariable=destinationPoint)
    dest_point_entry.pack()
    Label(text="").pack()
    Label(text="").pack()

    Button(main_screen, text="Add train", bg="yellow", height="2",
           width="50", font=(("Times", "12")), command=Add_train).pack()

    main_screen.mainloop()


main_page()
