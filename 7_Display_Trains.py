from tkinter import *
import os


def main_page():
    global main_screen
    main_screen = Tk()
    main_screen.title('Railway Management | View Trains')
    main_screen.geometry('500x500')

    # frame = Frame(main_screen)
    # grid = Frame(frame)

    Label(main_screen, text="Trains Available", bg="grey", width="50",
          height="2", font=("Calibri", 10)).grid(row=0, column=1, columnspan=4)

    Label(main_screen, text='Train ID ', font='verdana').grid(row=1, column=0)
    Label(main_screen, text='       ', font='verdana').grid(row=1, column=1)

    Label(main_screen, text='Boarding Point ', font='verdana').grid(row=1, column=2)
    Label(main_screen, text='       ', font='verdana').grid(row=1, column=3)

    Label(main_screen, text='Destination Point ', font='verdana').grid(row=1, column=4)

    i = 2
    for line in open("Train_details.txt", "r").readlines():
        display = line.split()
        Label(main_screen, text=display[0], font='verdana').grid(row=i, column=0)
        Label(main_screen, text=display[1], font='verdana').grid(row=i, column=2)
        Label(main_screen, text=display[2], font='verdana').grid(row=i, column=4)
        i = i + 1

    main_screen.mainloop()


main_page()
