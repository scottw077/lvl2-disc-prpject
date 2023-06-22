from tkinter import *
root = Tk()
root.title("Electrical Job Management Software")
root.iconbitmap("ElecTRICIAN JOB MANAGEMENT SOFTWARE (2).ico")
root.geometry("1600x900")
root.configure(bg="#5b5b5c")


def sign_up():
    signuptxt = Label(root, text="Sign Up")
    signuptxt.grid(row=0, column=0)


sign_up()
root.mainloop()
