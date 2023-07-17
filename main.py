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
    else:
        new_user = [username, pwd]
        userpass.append(new_user)

        with open("usernames.json", "w") as j:
            json.dump(userpass, j)
        messagebox.showinfo("Success!", "Sucessfully Signed Up")


def login():
    logintxt = Label(root, text="Login", font=(
        "Impact 80"), fg="white", bg="#5b5b5c")
    logintxt.grid(row=0, column=3)

    usertxt = Label(root, text="Username:", font=(
        "Arial 12 bold"), fg="white", bg="#5b5b5c")
    usertxt.grid(row=1, column=3)
    user_entry = Entry(root, width=20, justify="center")
    user_entry.grid(row=2, column=3)

    spacer1 = Label(root, text="", bg="#5b5b5c")
    spacer1.grid(row=3, column=3)

    pwdtxt = Label(root, text="Password:", font=(
        "Arial 12 bold"), fg="white", bg="#5b5b5c")
    pwdtxt.grid(row=4, column=3)
    pwd_entry = Entry(root, width=20, justify="center", show="*")
    pwd_entry.grid(row=5, column=3)

    spacer2 = Label(root, text="", bg="#5b5b5c")
    spacer2.grid(row=6, column=3)

    login_button = Button(root, text="Login", padx=30,
                          pady=10, font=("Arial 12 bold"), borderwidth=6,  command=lambda: login_process
                           (user_entry.get(), pwd_entry.get()))
    login_button.grid(row=9, column=3)


def login_process(username, password):
    with open("usernames.json") as c:
        userpass = json.load(c)
        users = [user[0]for user in userpass]

    if "" == username:
        messagebox.showinfo("Entry Box Empty!", "Empty Username box!")

    elif "" == password:
        messagebox.showinfo("Entry Box Empty!", "Empty Password box!")
    
    elif username in users:
        position = users.index(username)
        if password == userpass[position][1]:
            print("correct")
        else:
            messagebox.showerror("An error occured", "Username or Password is incorrect, please try again")
    else:
        messagebox.showerror("An error occured", "Username or Password is incorrect, please try again")
          
def main_menu():
    spacer1 = Label(root, text="", bg="#5b5b5c")
    spacer1.grid(row=0, column=3)
    
    add_job_btn = Button(root, text="Add Job", padx=30, pady=10, font=("Arial 18 bold"), borderwidth=6)
    add_job_btn.grid(row=1, column=3)

    staff_tracker_btn = Button(root, text="Staff Tracker", padx=30, pady=10, font=("Arial 18 bold"), borderwidth=6)
    staff_tracker_btn.grid(row=1, column=2)

def add_job():
    addjobtxt = Label(root, text="Add Job", font=(
        "Impact 60"), fg="white", bg="#5b5b5c")
    addjobtxt.grid(row=0, column=3)

    nametxt = Label(root, text="Client's Name", font=(
        "Arial 15 bold"), fg="white", bg="#5b5b5c")
    nametxt.grid(row=2, column=3)
    name_entry = Entry(root, width=20, justify="center")
    name_entry.grid(row=3, column=3)

    spacer1 = Label(root, text="", bg="#5b5b5c")
    spacer1.grid(row=4, column=3)

    emailtxt = Label(root, text="Client's Email Address", font=(
        "Arial 15 bold"), fg="white", bg="#5b5b5c")
    emailtxt.grid(row=5, column=3)
    email_entry = Entry(root, width=20, justify="center")
    email_entry.grid(row=6, column=3)

    spacer2 = Label(root, text="", bg="#5b5b5c")
    spacer2.grid(row=7, column=3)

    phnenumtxt = Label(root, text="Client's Phone Number", font=(
        "Arial 15 bold"), fg="white", bg="#5b5b5c")
    phnenumtxt.grid(row=8, column=3)
    phnenum_entry = Entry(root, width=20, justify="center")
    phnenum_entry.grid(row=9, column=3)

    spacer3 = Label(root, text="", bg="#5b5b5c")
    spacer3.grid(row=10, column=3)

    addresstxt = Label(root, text="Client's Site Address", font=(
        "Arial 15 bold"), fg="white", bg="#5b5b5c")
    addresstxt.grid(row=11, column=3)
    address_entry = Entry(root, width=20, justify="center")
    address_entry.grid(row=12, column=3)

add_job()

root.mainloop()
