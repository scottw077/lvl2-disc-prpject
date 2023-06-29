from tkinter import *
from tkinter import messagebox
import json
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
    username_entry = Entry(root, width=20, justify="center")
    username_entry.grid(row=2, column=3)

    spacer1 = Label(root, text="", bg="#5b5b5c")
    spacer1.grid(row=3, column=3)

    pwdtxt = Label(root, text="Create a Password", font=(
        "Arial 12 bold"), fg="white", bg="#5b5b5c")
    pwdtxt.grid(row=4, column=3)
    password = Entry(root, width=20, justify="center", show="*")
    password.grid(row=5, column=3)

    spacer2 = Label(root, text="", bg="#5b5b5c")
    spacer2.grid(row=6, column=3)

    confirmpwdtxt = Label(root, text="Confirm Password", font=(
        "Arial 12 bold"), fg="white", bg="#5b5b5c")
    confirmpwdtxt.grid(row=7, column=3)
    confirmpassword = Entry(root, width=20, justify="center", show="*")
    confirmpassword.grid(row=8, column=3)

    spacer3 = Label(root, text="", bg="#5b5b5c")
    spacer3.grid(row=9, column=3)

    sign_upbutton = Button(root, text="Sign Up", padx=30,
                           pady=10, font=("Arial 12 bold"), borderwidth=6, command=lambda: signup_process
                           (username_entry.get(), password.get(), confirmpassword.get()))
    sign_upbutton.grid(row=10, column=3)


def signup_process(username, pwd, confirmpwd):
    with open("usernames.json") as c:
        userpass = json.load(c)
        users = [user[0]for user in userpass]
    print(userpass)
    print(users)

    if " " in username:
        messagebox.showerror(
            "An error occured", "Error, cannot have spaces in username")

    elif " " in pwd:
        messagebox.showerror(
            "An error occured", "Error, cannot have spaces in password")

    elif "" == username:
        messagebox.showinfo("Entry Box Empty!", "Empty Username box!")

    elif "" == pwd:
        messagebox.showinfo("Entry Box Empty!", "Empty Password box!")

    elif pwd != confirmpwd:
        messagebox.showerror("An error occured",
                             "Error, Passwords must match!")

    elif username in users:
        messagebox.showinfo("Username already Taken!", "The username you have "
                            "inputed is already taken! Please choose a different username")


sign_up()
root.mainloop()
