from tkinter import *
from tkinter import messagebox, ttk
import json
import datetime
import bcrypt
root = Tk()
root.title("Electrical Job Management Software")
root.iconbitmap("ElecTRICIAN JOB MANAGEMENT SOFTWARE (2).ico")
root.geometry("800x450")
root.configure(bg="#5b5b5c")
root.columnconfigure(3, weight=1)


class signup:
    def __init__(self, master):
        self.root = master
        self.signuptxt = Label(root, text="Sign Up", font=(
            "Impact 80"), fg="white", bg="#5b5b5c")
        self.signuptxt.grid(row=0, column=3)

        self.usernametxt = Label(root, text="Create a Username", font=(
            "Arial 12 bold"), fg="white", bg="#5b5b5c")
        self.usernametxt.grid(row=1, column=3)
        self.username_entry = Entry(root, width=20, justify="center")
        self.username_entry.grid(row=2, column=3)

        self.spacer1 = Label(root, text="", bg="#5b5b5c")
        self.spacer1.grid(row=3, column=3)

        self.pwd_txt = Label(root, text="Create a Password", font=(
            "Arial 12 bold"), fg="white", bg="#5b5b5c")
        self.pwd_txt.grid(row=4, column=3)
        self.password = Entry(root, width=20, justify="center", show="*")
        self.password.grid(row=5, column=3)

        self.spacer2 = Label(root, text="", bg="#5b5b5c")
        self.spacer2.grid(row=6, column=3)

        self.confirmpwdtxt = Label(root, text="Confirm Password", font=(
            "Arial 12 bold"), fg="white", bg="#5b5b5c")
        self.confirmpwdtxt.grid(row=7, column=3)
        self.confirmpassword = Entry(
            root, width=20, justify="center", show="*")
        self.confirmpassword.grid(row=8, column=3)

        self.spacer3 = Label(root, text="", bg="#5b5b5c")
        self.spacer3.grid(row=9, column=3)

        self.sign_upbutton = Button(root, text="Sign Up", padx=30,
                                    pady=10, font=("Arial 12 bold"), borderwidth=6, command=lambda: signup_process
                                    (self.username_entry.get(), self.password.get(), self.confirmpassword.get()))
        self.sign_upbutton.grid(row=10, column=3)

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
                salt = bcrypt.gensalt()
                encoded_pwd = pwd.encode("utf-8")
                hashed_pwd = bcrypt.hashpw(encoded_pwd, salt)
                new_user = [username, str(hashed_pwd)]
                userpass.append(new_user)

                with open("usernames.json", "w") as j:
                    json.dump(userpass, j)
                messagebox.showinfo("Success!", "Sucessfully Signed Up")
                self.signuptxt.destroy()
                self.usernametxt.destroy()
                self.username_entry.destroy()
                self.spacer1.destroy()
                self.pwd_txt.destroy()
                self.password.destroy()
                self.spacer2.destroy()
                self.confirmpwdtxt.destroy()
                self.confirmpassword.destroy()
                self.spacer3.destroy()
                self.sign_upbutton.destroy()
                login(root)


class login:
    def __init__(self, master):
        self.root = master
        self.logintxt = Label(root, text="Login", font=(
            "Impact 80"), fg="white", bg="#5b5b5c")
        self.logintxt.grid(row=0, column=3)

        self.usertxt = Label(root, text="Username:", font=(
            "Arial 12 bold"), fg="white", bg="#5b5b5c")
        self.usertxt.grid(row=1, column=3)
        self.user_entry = Entry(root, width=20, justify="center")
        self.user_entry.grid(row=2, column=3)

        self.spacer1 = Label(root, text="", bg="#5b5b5c")
        self.spacer1.grid(row=3, column=3)

        self.pwdtxt = Label(root, text="Password:", font=(
            "Arial 12 bold"), fg="white", bg="#5b5b5c")
        self.pwdtxt.grid(row=4, column=3)
        self.pwd_entry = Entry(root, width=20, justify="center", show="*")
        self.pwd_entry.grid(row=5, column=3)

        self.spacer2 = Label(root, text="", bg="#5b5b5c")
        self.spacer2.grid(row=6, column=3)

        self.login_button = Button(root, text="Login", padx=30,
                                   pady=10, font=("Arial 12 bold"), borderwidth=6,  command=lambda: login_process
                                   (self.user_entry.get(), self.pwd_entry.get()))
        self.login_button.grid(row=8, column=3)

        self.spacer3 = Label(root, text="", bg="#5b5b5c")
        self.spacer3.grid(row=9, column=3)

        self.sign_up_pass_btn = Button(
            root, text="Don't have an account? Press here to Sign Up", font=("Arial 12 bold"), bg="#5b5b5c", fg="#2E96D1", bd=0, command=self.sign_up_pass_through)
        self.sign_up_pass_btn.grid(row=10, column=3)

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
                    self.logintxt.destroy()
                    self.usertxt.destroy()
                    self.user_entry.destroy()
                    self.spacer1.destroy()
                    self.pwdtxt.destroy()
                    self.pwd_entry.destroy()
                    self.spacer2.destroy()
                    self.login_button.destroy()
                    self.sign_up_pass_btn.destroy()
                    main_menu(root)

                else:
                    messagebox.showerror(
                        "An error occured", "Username or Password is incorrect, please try again")
            else:
                messagebox.showerror(
                    "An error occured", "Username or Password is incorrect, please try again")

    def sign_up_pass_through(self):
        self.logintxt.destroy()
        self.usertxt.destroy()
        self.user_entry.destroy()
        self.spacer1.destroy()
        self.pwdtxt.destroy()
        self.pwd_entry.destroy()
        self.spacer2.destroy()
        self.login_button.destroy()
        self.sign_up_pass_btn.destroy()
        signup(root)


class main_menu:
    def __init__(self, master):
        self.root = master
        self.add_job_btn = Button(root, text="Add Job", padx=30, pady=10, font=(
            "Arial 14 bold"), borderwidth=6, command=self.add_job)
        self.add_job_btn.place(x=275, y=22)

        self.staff_tracker_btn = Button(root, text="Staff Tracker", padx=30, pady=10, font=(
            "Arial 14 bold"), borderwidth=6, command=self.staff_tracker)
        self.staff_tracker_btn.place(x=20, y=22)

        self.create_invoice_btn = Button(root, text="Create Invoice or Quote", padx=30, pady=10, font=(
            "Arial 14 bold"), borderwidth=6, command=self.create_invoice)
        self.create_invoice_btn.place(x=480, y=22)

        self.jobs_frame = Frame(root)
        self.jobs_frame.place(x=20, y=106)

        style = ttk.Style()
        style.configure("Treeview", background="#5b5b5c")

        with open("jobs.json") as k:
            jobs = json.load(k)

        self.jobs = ttk.Treeview(self.jobs_frame, height=len(jobs))

        self.jobs['columns'] = ('job_num', 'name',
                                'email', 'phe_num', 'address', "job_type", "job_status", "staff")

        self.jobs.column("#0", width=0,  stretch=NO)
        self.jobs.column("job_num", anchor=CENTER, width=42)
        self.jobs.column("name", anchor=CENTER, width=110)
        self.jobs.column("email", anchor=CENTER, width=120)
        self.jobs.column("phe_num", anchor=CENTER, width=90)
        self.jobs.column("address", anchor=CENTER, width=100)
        self.jobs.column("job_type", anchor=CENTER, width=100)
        self.jobs.column("job_status", anchor=CENTER, width=110)
        self.jobs.column("staff", anchor=CENTER, width=88)

        self.jobs.heading("#0", text="", anchor=CENTER)
        self.jobs.heading("job_num", text="Job #",
                          anchor=CENTER)
        self.jobs.heading("name", text="Client Name",
                          anchor=CENTER)
        self.jobs.heading("email", text="Email",
                          anchor=CENTER)
        self.jobs.heading("phe_num", text="Phone Number",
                          anchor=CENTER)
        self.jobs.heading("address", text="Address",
                          anchor=CENTER)
        self.jobs.heading("job_type", text="Job Type",
                          anchor=CENTER)
        self.jobs.heading("job_status", text="Job Status",
                          anchor=CENTER)
        self.jobs.heading("staff", text="Staff",
                          anchor=CENTER)

        num = 0

        for i in jobs:
            self.jobs.insert(parent='', index='end', iid=num, text='',
                             values=jobs[num])
            num += 1

        self.jobs.grid(row=1, column=3)

    def add_job(self):
        self.add_job_btn.destroy()
        self.staff_tracker_btn.destroy()
        self.create_invoice_btn.destroy()
        self.jobs_frame.destroy()
        self.app = add_job(root)

    def staff_tracker(self):
        self.add_job_btn.destroy()
        self.staff_tracker_btn.destroy()
        self.create_invoice_btn.destroy()
        self.jobs_frame.destroy()
        self.app = staff_tracker(root)

    def create_invoice(self):
        self.add_job_btn.destroy()
        self.staff_tracker_btn.destroy()
        self.create_invoice_btn.destroy()
        self.jobs_frame.destroy()


class add_job:
    def __init__(self, master):
        self.root = master
        frame = LabelFrame(root, padx=5, pady=5, bg="#5b5b5c")
        frame.grid(row=0, column=3)

        addjobtxt = Label(frame, text="Add Job", font=(
            "Impact 60"), fg="white", bg="#5b5b5c")
        addjobtxt.grid(row=1, column=3)

        nametxt = Label(frame, text="Client's Name", font=(
            "Arial 13 bold"), fg="white", bg="#5b5b5c")
        nametxt.grid(row=2, column=3)
        name_entry = Entry(frame, width=20, justify="center")
        name_entry.grid(row=3, column=3)

        spacer1 = Label(frame, text="", bg="#5b5b5c")
        spacer1.grid(row=4, column=3)

        emailtxt = Label(frame, text="Client's Email Address", font=(
            "Arial 13 bold"), fg="white", bg="#5b5b5c")
        emailtxt.grid(row=5, column=3)
        email_entry = Entry(frame, width=20, justify="center")
        email_entry.grid(row=6, column=3)

        spacer2 = Label(frame, text="", bg="#5b5b5c")
        spacer2.grid(row=7, column=3)

        phnenumtxt = Label(frame, text="Client's Phone Number", font=(
            "Arial 13 bold"), fg="white", bg="#5b5b5c")
        phnenumtxt.grid(row=8, column=3)
        phnenum_entry = Entry(frame, width=20, justify="center")
        phnenum_entry.grid(row=9, column=3)

        spacer3 = Label(frame, text="", bg="#5b5b5c")
        spacer3.grid(row=10, column=3)

        addresstxt = Label(frame, text="Client's Site Address", font=(
            "Arial 13 bold"), fg="white", bg="#5b5b5c")
        addresstxt.grid(row=11, column=3)
        address_entry = Entry(frame, width=20, justify="center")
        address_entry.grid(row=12, column=3)

        spacer4 = Label(frame, text="", bg="#5b5b5c")
        spacer4.grid(row=13, column=3)

        next_btn = Button(frame, text="Next", padx=30, pady=10, font=("Arial 12 bold"), command=lambda: add_job2(
            self, name_entry.get(), email_entry.get(), phnenum_entry.get(), address_entry.get(), frame))
        next_btn.grid(row=14, column=3)

        def add_job2(self, name, email, phnenum, address, frame):
            if "@" not in email or "." not in email:
                messagebox.showerror(
                    "An error occured", "Email Address is not valid, please try again")

            elif phnenum.isalpha():
                messagebox.showerror("An error occured",
                                     "Phone number cannot contain letters")

            elif name == "":
                messagebox.showinfo(
                    "Entry Box Empty!", "Empty Client's Name Box! Please enter the client's name")

            elif phnenum == "":
                messagebox.showinfo(
                    "Entry Box Empty!", "Empty Client's Phone Number Box! Please enter the client's phone number")

            elif address == "":
                messagebox.showinfo(
                    "Entry Box Empty!", "Empty Client's Address Box! Please enter the client's address")

            else:
                frame.grid_forget()

                frame1 = LabelFrame(root, padx=5, pady=5, bg="#5b5b5c")
                frame1.grid(row=0, column=3)

                addjobtxt = Label(frame1, text="Add Job", font=(
                    "Impact 60"), fg="white", bg="#5b5b5c")
                addjobtxt.grid(row=1, column=3)

                jobtype_txt = Label(frame1, text="Job Type", font=(
                    "Arial 16 bold"), fg="white", bg="#5b5b5c")
                jobtype_txt.grid(row=2, column=3)
                jobtype_default = StringVar()
                jobtype_default.set("Select Job Type")
                job_types = ["monday", "tuesday", "wednesday"]
                jobtype_entry = OptionMenu(frame1, jobtype_default, *job_types)
                jobtype_entry.grid(row=3, column=3)

                spacer1 = Label(frame1, text="", bg="#5b5b5c")
                spacer1.grid(row=4, column=3)

                jobstatus_txt = Label(frame1, text="Job Status", font=(
                    "Arial 16 bold"), fg="white", bg="#5b5b5c")
                jobstatus_txt.grid(row=5, column=3)
                jobstatus_default = StringVar()
                jobstatus_default.set("Select Job Status")
                job_statuses = ["started", "half-way through", "finished"]
                jobstatus_entry = OptionMenu(
                    frame1, jobstatus_default, *job_statuses)
                jobstatus_entry.grid(row=6, column=3)

                spacer2 = Label(frame1, text="", bg="#5b5b5c")
                spacer2.grid(row=7, column=3)

                staff_txt = Label(frame1, text="Staff", font=(
                    "Arial 16 bold"), fg="white", bg="#5b5b5c")
                staff_txt.grid(row=8, column=3)
                staff_default = StringVar()
                staff_default.set("Select Staff")
                staff = ["sdfs", "sdfsdf"]
                staff_entry = OptionMenu(frame1, staff_default, *staff)
                staff_entry.grid(row=9, column=3)

                spacer3 = Label(frame1, text="", bg="#5b5b5c")
                spacer3.grid(row=10, column=3)

                add_job_btn = Button(frame1, text="Add New Job", padx=22, pady=10, font=("Arial 12 bold"), command=lambda: add_job_process(
                    name, email, phnenum, address, jobtype_default.get(), jobstatus_default.get(), staff_default.get(), frame1))
                add_job_btn.grid(row=11, column=3)

        def add_job_process(name, email, phnenum, address, job_type, job_status, staff, frame):
            with open("jobs.json", "r") as h:
                existing_jobs = json.load(h)
            job_num = int(existing_jobs[-1][0])
            job_num += 1

            new_job = [job_num, name, email, phnenum,
                       address, job_type, job_status, staff]
            existing_jobs.append(new_job)
            with open("jobs.json", "w") as j:
                json.dump(existing_jobs, j)
            messagebox.showinfo("Success!", "Sucessfully Added Job!")
            frame.grid_forget()
            main_menu(root)


class staff_tracker:
    def __init__(self, master):
        self.root = master
        self.main_menu_return = Button(root, text="Return to Main Menu", padx=2, pady=2, font=(
            "Arial 8 bold"), command=self.main_menu_btn)
        self.main_menu_return.place(x=665, y=15)
        self.addstaff = Button(root, text="Add Staff", padx=2, pady=2, font=(
            "Arial 8 bold"), command=self.addstaff)
        self.addstaff.place(x=10, y=15)

        with open("jobs.json") as d:
            jobs = json.load(d)

        total_rows = len(jobs)
        total_columns = len(jobs[0])

        # for i in range(total_rows):
        # for j in range(total_columns):

        # self.e = Entry(root, width=20, fg='blue',
        # font=('Arial',16,'bold'))

        # self.e.grid(row=i, column=j)
        # self.e.insert(END, jobs[i][j])

    def add_staff(self):
        self.addstaff.destroy()
        self.main_menu_return.destroy()
        self.addstafftxt = Label(root, text="Add Staff", font=(
            "Impact 60"), fg="white", bg="#5b5b5c")
        self.addstafftxt.grid(row=0, column=3)

        self.spacer1 = Label(root, text="", bg="#5b5b5c")
        self.spacer1.grid(row=2, column=3)

        self.spacer2 = Label(root, text="", bg="#5b5b5c")
        self.spacer2.grid(row=3, column=3)

        self.stafftxt = Label(root, text="New Staff Name:", font=(
            "Arial 12 bold"), fg="white", bg="#5b5b5c")
        self.stafftxt.grid(row=4, column=3)
        self.new_staff_entry = Entry(root, width=20, justify="center")
        self.new_staff_entry.grid(row=5, column=3)

        self.spacer3 = Label(root, text="", bg="#5b5b5c")
        self.spacer3.grid(row=6, column=3)

        self.spacer4 = Label(root, text="", bg="#5b5b5c")
        self.spacer4.grid(row=7, column=3)

        self.spacer5 = Label(root, text="", bg="#5b5b5c")
        self.spacer5.grid(row=8, column=3)

        self.next_btn = Button(root, text="Add Staff", padx=30,
                               pady=10, font=("Arial 12 bold"), borderwidth=6,  command=self.new_staff)
        self.next_btn.grid(row=9, column=3)

    def new_staff(self):
        staff = self.new_staff_entry.get()
        with open("staff.json", "r") as d:
            current_staff = json.load(d)

        if staff in current_staff:
            messagebox.showerror("An error occured", "Staff already exists!")

        elif staff == "":
            messagebox.showinfo("Entry Box Empty!",
                                "Empty Add Staff entry box")

        else:
            with open("staff.json", "w") as c:
                json.dump(current_staff, c)

        self.addstafftxt.destroy()
        self.spacer1.destroy()
        self.spacer2.destroy()
        self.stafftxt.destroy()
        self.new_staff_entry.destroy()
        self.spacer3.destroy()
        self.spacer4.destroy()
        self.spacer5.destroy()
        self.next_btn.destroy()
        staff_tracker(root)

    def main_menu_btn(self):
        self.addstaff.destroy()
        self.main_menu_return.destroy()
        main_menu(root)


def main():
    login(root)
    root.mainloop()


if __name__ == '__main__':
    main()
