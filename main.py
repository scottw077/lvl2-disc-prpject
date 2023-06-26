from tkinter import *
root = Tk()
root.title("Electrical Job Management Software")
root.iconbitmap("ElecTRICIAN JOB MANAGEMENT SOFTWARE (2).ico")
root.geometry("800x450")
root.configure(bg="#5b5b5c")
root.columnconfigure(3, weight=1)


def sign_up():
    signuptxt = Label(root, text="Sign Up", font=(
        "Impact 80"), fg="white", bg="#5b5b5c")
    signuptxt.grid(row=0, column=3)

    usernametxt = Label(root, text="Create a Username", font=(
        "Arial 12 bold"), fg="white", bg="#5b5b5c")
    usernametxt.grid(row=1, column=3)
    username = Entry(root, width=20, justify="center")
    username.grid(row=2, column=3)

    pwdtxt = Label(root, text="Create a Password", font=(
        "Arial 12 bold"), fg="white", bg="#5b5b5c")
    pwdtxt.grid(row=4, column=3)
    password = Entry(root, width=20, justify="center")
    password.grid(row=5, column=3)


sign_up()
root.mainloop()
