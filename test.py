from tkinter import *
from tkinter import messagebox, ttk, filedialog
import json
import datetime
import hashlib
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.units import inch

root = Tk()
root.title("Electrical Job Management Software")
root.iconbitmap("ElecTRICIAN JOB MANAGEMENT SOFTWARE (2).ico")
root.geometry("800x450")
root.configure(bg="#5b5b5c")
root.columnconfigure(3, weight=1)


class signup:
    def __init__(self, master):
        self.root = master
        self.signuptxt = Label(
            root, text="Sign Up", font=("Impact 80"), fg="white", bg="#5b5b5c"
        )
        self.signuptxt.grid(row=0, column=3)

        self.usernametxt = Label(
            root,
            text="Create a Username",
            font=("Arial 12 bold"),
            fg="white",
            bg="#5b5b5c",
        )
        self.usernametxt.grid(row=1, column=3)
        self.username_entry = Entry(root, width=20, justify="center")
        self.username_entry.grid(row=2, column=3)

        self.spacer1 = Label(root, text="", bg="#5b5b5c")
        self.spacer1.grid(row=3, column=3)

        self.pwd_txt = Label(
            root,
            text="Create a Password",
            font=("Arial 12 bold"),
            fg="white",
            bg="#5b5b5c",
        )
        self.pwd_txt.grid(row=4, column=3)
        self.password = Entry(root, width=20, justify="center", show="*")
        self.password.grid(row=5, column=3)

        self.spacer2 = Label(root, text="", bg="#5b5b5c")
        self.spacer2.grid(row=6, column=3)

        self.confirmpwdtxt = Label(
            root,
            text="Confirm Password",
            font=("Arial 12 bold"),
            fg="white",
            bg="#5b5b5c",
        )
        self.confirmpwdtxt.grid(row=7, column=3)
        self.confirmpassword = Entry(root, width=20, justify="center", show="*")
        self.confirmpassword.grid(row=8, column=3)

        self.spacer3 = Label(root, text="", bg="#5b5b5c")
        self.spacer3.grid(row=9, column=3)

        self.sign_upbutton = Button(
            root,
            text="Sign Up",
            padx=30,
            pady=10,
            font=("Arial 12 bold"),
            borderwidth=6,
            command=lambda: signup_process(
                self.username_entry.get(),
                self.password.get(),
                self.confirmpassword.get(),
            ),
        )
        self.sign_upbutton.grid(row=10, column=3)

        self.spacer3 = Label(root, text="", bg="#5b5b5c")
        self.spacer3.grid(row=11, column=3)

        self.login_pass_through_btn = Button(
            root,
            text="Already have an account? Press here to Login",
            font=("Arial 12 bold"),
            bg="#5b5b5c",
            fg="#0381ff",
            bd=0,
            command=self.login_pass_through,
        )
        self.login_pass_through_btn.grid(row=12, column=3)

        def signup_process(username, pwd, confirmpwd):

            with open("usernames.json", encoding="UTF-8") as json_usernames:
                userpass = json.load(json_usernames)
                users = [user[0] for user in userpass]
            if " " in username:
                messagebox.showerror(
                    "An error occured", "Error, cannot have spaces in username"
                )

            elif " " in pwd:
                messagebox.showerror(
                    "An error occured", "Error, cannot have spaces in password"
                )

            elif "" == username:
                messagebox.showinfo("Entry Box Empty!", "Empty Username box!")

            elif "" == pwd:
                messagebox.showinfo("Entry Box Empty!", "Empty Password box!")

            elif pwd != confirmpwd:
                messagebox.showerror("An error occured", "Error, Passwords must match!")

            elif username in users:
                messagebox.showinfo(
                    "Username already Taken!",
                    "The username you have "
                    "inputed is already taken! Please choose a different username",
                )
            else:
                encoded_pwd = pwd.encode("utf-8")
                hashed_pwd = hashlib.sha256(encoded_pwd).hexdigest()
                new_user = [username, str(hashed_pwd)]
                userpass.append(new_user)

                with open("usernames.json", "w", encoding="UTF-8") as j:
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
                self.login_pass_through_btn.destroy()
                Login(root)

    def login_pass_through(self):
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
        self.login_pass_through_btn.destroy()
        Login(root)


class Login:
    def __init__(self, master):
        self.root = master
        self.logintxt = Label(
            root, text="Login", font=("Impact 80"), fg="white", bg="#5b5b5c"
        )
        self.logintxt.grid(row=0, column=3)

        self.usertxt = Label(
            root, text="Username:", font=("Arial 12 bold"), fg="white", bg="#5b5b5c"
        )
        self.usertxt.grid(row=1, column=3)
        self.user_entry = Entry(root, width=20, justify="center")
        self.user_entry.grid(row=2, column=3)

        self.spacer1 = Label(root, text="", bg="#5b5b5c")
        self.spacer1.grid(row=3, column=3)

        self.pwdtxt = Label(
            root, text="Password:", font=("Arial 12 bold"), fg="white", bg="#5b5b5c"
        )
        self.pwdtxt.grid(row=4, column=3)
        self.pwd_entry = Entry(root, width=20, justify="center", show="*")
        self.pwd_entry.grid(row=5, column=3)

        self.spacer2 = Label(root, text="", bg="#5b5b5c")
        self.spacer2.grid(row=6, column=3)

        self.login_button = Button(
            root,
            text="Login",
            padx=30,
            pady=10,
            font=("Arial 12 bold"),
            borderwidth=6,
            command=lambda: login_process(self.user_entry.get(), self.pwd_entry.get()),
        )
        self.login_button.grid(row=8, column=3)

        self.spacer3 = Label(root, text="", bg="#5b5b5c")
        self.spacer3.grid(row=9, column=3)

        self.sign_up_pass_btn = Button(
            root,
            text="Don't have an account? Press here to Sign Up",
            font=("Arial 12 bold"),
            bg="#5b5b5c",
            fg="#0381ff",
            bd=0,
            command=self.sign_up_pass_through,
        )
        self.sign_up_pass_btn.grid(row=10, column=3)

        def login_process(username, password):
            with open("usernames.json", encoding="UTF-8") as username_json:
                userpass = json.load(username_json)
                users = [user[0] for user in userpass]

            if "" == username:
                messagebox.showinfo("Entry Box Empty!", "Empty Username box!")

            elif "" == password:
                messagebox.showinfo("Entry Box Empty!", "Empty Password box!")

            elif username in users:
                position = users.index(username)
                passw = str(password).encode("utf-8")
                entry_hashed_pw = hashlib.sha256(passw).hexdigest()

                if entry_hashed_pw == userpass[position][1]:
                    self.logintxt.destroy()
                    self.usertxt.destroy()
                    self.user_entry.destroy()
                    self.spacer1.destroy()
                    self.pwdtxt.destroy()
                    self.pwd_entry.destroy()
                    self.spacer2.destroy()
                    self.login_button.destroy()
                    self.sign_up_pass_btn.destroy()
                    MainMenu(root, username)

                else:
                    messagebox.showerror(
                        "An error occured",
                        "Username or Password is incorrect, please try again",
                    )
            else:
                messagebox.showerror(
                    "An error occured",
                    "Username or Password is incorrect, please try again",
                )

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


class MainMenu:
    def __init__(self, master, username):
        self.root = master
        self.username = username
        self.add_job_btn = Button(
            root,
            text="Add Job",
            padx=30,
            pady=10,
            font=("Arial 14 bold"),
            borderwidth=6,
            command=self.add_job,
        )
        self.add_job_btn.place(x=275, y=22)

        self.staff_tracker_btn = Button(
            root,
            text="Staff Tracker",
            padx=30,
            pady=10,
            font=("Arial 14 bold"),
            borderwidth=6,
            command=self.staff_tracker,
        )
        self.staff_tracker_btn.place(x=20, y=22)

        self.create_invoice_btn = Button(
            root,
            text="Create Invoice or Quote",
            padx=30,
            pady=10,
            font=("Arial 14 bold"),
            borderwidth=6,
            command=self.create_invoice,
        )
        self.create_invoice_btn.place(x=480, y=22)

        self.jobs_frame = Frame(root)
        self.jobs_frame.place(x=20, y=106)

        style = ttk.Style()
        style.configure("Treeview", background="#5b5b5c")

        with open("jobs.json", encoding="UTF-8") as k:
            all_jobs = json.load(k)

        jobs = []

        for job in all_jobs:
            if job[0] == username:
                jobs.append(job[1:])

        self.jobs = ttk.Treeview(self.jobs_frame, height=len(jobs))

        self.jobs["columns"] = (
            "job_num",
            "name",
            "email",
            "phe_num",
            "address",
            "job_type",
            "job_status",
            "staff",
        )

        self.jobs.column("#0", width=0, stretch=NO)
        self.jobs.column("job_num", anchor=CENTER, width=42)
        self.jobs.column("name", anchor=CENTER, width=110)
        self.jobs.column("email", anchor=CENTER, width=120)
        self.jobs.column("phe_num", anchor=CENTER, width=90)
        self.jobs.column("address", anchor=CENTER, width=100)
        self.jobs.column("job_type", anchor=CENTER, width=100)
        self.jobs.column("job_status", anchor=CENTER, width=110)
        self.jobs.column("staff", anchor=CENTER, width=88)

        self.jobs.heading("#0", text="", anchor=CENTER)
        self.jobs.heading("job_num", text="Job #", anchor=CENTER)
        self.jobs.heading("name", text="Client Name", anchor=CENTER)
        self.jobs.heading("email", text="Email", anchor=CENTER)
        self.jobs.heading("phe_num", text="Phone Number", anchor=CENTER)
        self.jobs.heading("address", text="Address", anchor=CENTER)
        self.jobs.heading("job_type", text="Job Type", anchor=CENTER)
        self.jobs.heading("job_status", text="Job Status", anchor=CENTER)
        self.jobs.heading("staff", text="Staff", anchor=CENTER)

        num = 0

        for i in jobs:
            self.jobs.insert(parent="", index="end", iid=num, text="", values=jobs[num])
            num += 1

        self.jobs.grid(row=1, column=3)

    def add_job(self):
        self.add_job_btn.destroy()
        self.staff_tracker_btn.destroy()
        self.create_invoice_btn.destroy()
        self.jobs_frame.destroy()
        add_job(root, self.username)

    def staff_tracker(self):
        self.add_job_btn.destroy()
        self.staff_tracker_btn.destroy()
        self.create_invoice_btn.destroy()
        self.jobs_frame.destroy()
        staff_tracker(root, self.username)

    def create_invoice(self):
        self.add_job_btn.destroy()
        self.staff_tracker_btn.destroy()
        self.create_invoice_btn.destroy()
        self.jobs_frame.destroy()
        invoice_creation(root, self.username)


class add_job:
    def __init__(self, master, username):
        self.root = master
        self.username = username
        self.main_menu_return = Button(
            root,
            text="Return to Main Menu",
            padx=2,
            pady=2,
            font=("Arial 8 bold"),
            command=lambda: main_menu_return(frame, self.main_menu_return),
        )
        self.main_menu_return.place(x=672, y=8)
        frame = LabelFrame(root, padx=5, pady=5, bg="#5b5b5c")
        frame.grid(row=0, column=3)

        addjobtxt = Label(
            frame, text="Add Job", font=("Impact 60"), fg="white", bg="#5b5b5c"
        )
        addjobtxt.grid(row=1, column=3)

        nametxt = Label(
            frame,
            text="Client's Name",
            font=("Arial 13 bold"),
            fg="white",
            bg="#5b5b5c",
        )
        nametxt.grid(row=2, column=3)
        name_entry = Entry(frame, width=20, justify="center")
        name_entry.grid(row=3, column=3)

        spacer1 = Label(frame, text="", bg="#5b5b5c")
        spacer1.grid(row=4, column=3)

        emailtxt = Label(
            frame,
            text="Client's Email Address",
            font=("Arial 13 bold"),
            fg="white",
            bg="#5b5b5c",
        )
        emailtxt.grid(row=5, column=3)
        email_entry = Entry(frame, width=20, justify="center")
        email_entry.grid(row=6, column=3)

        spacer2 = Label(frame, text="", bg="#5b5b5c")
        spacer2.grid(row=7, column=3)

        phnenumtxt = Label(
            frame,
            text="Client's Phone Number",
            font=("Arial 13 bold"),
            fg="white",
            bg="#5b5b5c",
        )
        phnenumtxt.grid(row=8, column=3)
        phnenum_entry = Entry(frame, width=20, justify="center")
        phnenum_entry.grid(row=9, column=3)

        spacer3 = Label(frame, text="", bg="#5b5b5c")
        spacer3.grid(row=10, column=3)

        addresstxt = Label(
            frame,
            text="Client's Site Address",
            font=("Arial 13 bold"),
            fg="white",
            bg="#5b5b5c",
        )
        addresstxt.grid(row=11, column=3)
        address_entry = Entry(frame, width=20, justify="center")
        address_entry.grid(row=12, column=3)

        spacer4 = Label(frame, text="", bg="#5b5b5c")
        spacer4.grid(row=13, column=3)

        next_btn = Button(
            frame,
            text="Next",
            padx=30,
            pady=10,
            font=("Arial 12 bold"),
            command=lambda: add_job2(
                name_entry.get(),
                email_entry.get(),
                phnenum_entry.get(),
                address_entry.get(),
                frame,
            ),
        )
        next_btn.grid(row=14, column=3)

        def add_job2(name, email, phnenum, address, frame):
            if "@" not in email or "." not in email:
                messagebox.showerror(
                    "An error occured", "Email Address is not valid, please try again"
                )

            elif phnenum.isalpha():
                messagebox.showerror(
                    "An error occured", "Phone number cannot contain letters"
                )

            elif name == "":
                messagebox.showinfo(
                    "Entry Box Empty!",
                    "Empty Client's Name Box! Please enter the client's name",
                )

            elif phnenum == "":
                messagebox.showinfo(
                    "Entry Box Empty!",
                    "Empty Client's Phone Number Box! Please enter the client's phone number",
                )

            elif address == "":
                messagebox.showinfo(
                    "Entry Box Empty!",
                    "Empty Client's Address Box! Please enter the client's address",
                )

            else:
                frame.grid_forget()
                self.main_menu_return.destroy()

                frame1 = LabelFrame(root, padx=5, pady=5, bg="#5b5b5c")
                frame1.grid(row=0, column=3)

                main_menu_return1 = Button(
                    root,
                    text="Return to Main Menu",
                    padx=2,
                    pady=2,
                    font=("Arial 8 bold"),
                    command=lambda: main_menu_return(frame1, main_menu_return1),
                )
                main_menu_return1.place(x=672, y=8)

                addjobtxt = Label(
                    frame1, text="Add Job", font=("Impact 60"), fg="white", bg="#5b5b5c"
                )
                addjobtxt.grid(row=1, column=3)

                jobtype_txt = Label(
                    frame1,
                    text="Job Type",
                    font=("Arial 16 bold"),
                    fg="white",
                    bg="#5b5b5c",
                )
                jobtype_txt.grid(row=2, column=3)
                jobtype_default = StringVar()
                jobtype_default.set("Select Job Type")
                job_types = ["monday", "tuesday", "wednesday"]
                jobtype_entry = OptionMenu(frame1, jobtype_default, *job_types)
                jobtype_entry.grid(row=3, column=3)

                spacer1 = Label(frame1, text="", bg="#5b5b5c")
                spacer1.grid(row=4, column=3)

                jobstatus_txt = Label(
                    frame1,
                    text="Job Status",
                    font=("Arial 16 bold"),
                    fg="white",
                    bg="#5b5b5c",
                )
                jobstatus_txt.grid(row=5, column=3)
                jobstatus_default = StringVar()
                jobstatus_default.set("Select Job Status")
                job_statuses = ["started", "half-way through", "finished"]
                jobstatus_entry = OptionMenu(frame1, jobstatus_default, *job_statuses)
                jobstatus_entry.grid(row=6, column=3)

                spacer2 = Label(frame1, text="", bg="#5b5b5c")
                spacer2.grid(row=7, column=3)

                staff_txt = Label(
                    frame1,
                    text="Staff",
                    font=("Arial 16 bold"),
                    fg="white",
                    bg="#5b5b5c",
                )
                staff_txt.grid(row=8, column=3)
                staff_default = StringVar()
                staff_default.set("Select Staff")
                with open("staff.json", encoding="UTF-8") as d:
                    all_staff = json.load(d)

                staff = []

                for indiv_staff in all_staff:
                    if indiv_staff[0] == username:
                        staff.append(indiv_staff[1])

                staff_entry = OptionMenu(frame1, staff_default, *staff)
                staff_entry.grid(row=9, column=3)

                spacer3 = Label(frame1, text="", bg="#5b5b5c")
                spacer3.grid(row=10, column=3)

                add_job_btn = Button(
                    frame1,
                    text="Add New Job",
                    padx=22,
                    pady=10,
                    font=("Arial 12 bold"),
                    command=lambda: add_job_process(
                        name,
                        email,
                        phnenum,
                        address,
                        jobtype_default.get(),
                        jobstatus_default.get(),
                        staff_default.get(),
                        frame1,
                        main_menu_return1,
                    ),
                )

                add_job_btn.grid(row=11, column=3)

        def add_job_process(
            name,
            email,
            phnenum,
            address,
            job_type,
            job_status,
            staff,
            frame,
            return_button,
        ):
            with open("jobs.json", "r", encoding="UTF-8") as json_jobs:
                existing_jobs = json.load(json_jobs)

            job_num = 0
            for job in existing_jobs:
                if job[0] == username:
                    job_num += 1

            new_job = [
                username,
                job_num,
                name,
                email,
                phnenum,
                address,
                job_type,
                job_status,
                staff,
            ]

            existing_jobs.append(new_job)
            with open("jobs.json", "w", encoding="UTF-8") as j:
                json.dump(existing_jobs, j)
            messagebox.showinfo("Success!", "Sucessfully Added Job!")
            frame.grid_forget()
            return_button.destroy()
            MainMenu(root, username)

        def main_menu_return(frame, return_button):
            frame.grid_forget()
            return_button.destroy()
            MainMenu(root, self.username)


class staff_tracker:
    def __init__(self, master, username):
        self.username = username
        self.root = master
        self.main_menu_return = Button(
            root,
            text="Return to Main Menu",
            padx=2,
            pady=2,
            font=("Arial 8 bold"),
            command=self.main_menu_btn,
        )
        self.main_menu_return.place(x=665, y=15)
        self.addstaff = Button(
            root,
            text="Add Staff",
            padx=2,
            pady=2,
            font=("Arial 8 bold"),
            command=self.add_staff,
        )
        self.addstaff.place(x=10, y=15)

        self.staff_frame = Frame(root)
        self.staff_frame.place(x=20, y=80)

        style = ttk.Style()
        style.configure("Treeview", background="#5b5b5c")

        with open("jobs.json", encoding="UTF-8") as k:
            all_jobs = json.load(k)

        jobs = []

        for job in all_jobs:
            if job[0] == self.username:
                jobs.append(job[1:])

        staff = []

        with open("staff.json", encoding="UTF-8") as g:
            all_staff = json.load(g)

        for staff_item in all_staff:
            if staff_item[0] == username:
                staff.append(staff_item[1])

        height_num = 0

        for each_job in jobs:
            if each_job[7] in staff:
                height_num += 1

        self.staff_table = ttk.Treeview(self.staff_frame, height=height_num)

        self.staff_table["columns"] = (
            "staff",
            "job_num",
            "name",
            "email",
            "phe_num",
            "address",
            "job_type",
            "job_status",
        )

        self.staff_table.column("#0", width=0, stretch=NO)
        self.staff_table.column("staff", anchor=CENTER, width=88)
        self.staff_table.column("job_num", anchor=CENTER, width=42)
        self.staff_table.column("name", anchor=CENTER, width=110)
        self.staff_table.column("email", anchor=CENTER, width=120)
        self.staff_table.column("phe_num", anchor=CENTER, width=90)
        self.staff_table.column("address", anchor=CENTER, width=100)
        self.staff_table.column("job_type", anchor=CENTER, width=83)
        self.staff_table.column("job_status", anchor=CENTER, width=110)

        self.staff_table.heading("#0", text="", anchor=CENTER)
        self.staff_table.heading("staff", text="Staff:")
        self.staff_table.heading("job_num", text="Job #", anchor=CENTER)
        self.staff_table.heading("name", text="Client Name", anchor=CENTER)
        self.staff_table.heading("email", text="Email", anchor=CENTER)
        self.staff_table.heading("phe_num", text="Phone Number", anchor=CENTER)
        self.staff_table.heading("address", text="Address", anchor=CENTER)
        self.staff_table.heading("job_type", text="Job Type", anchor=CENTER)
        self.staff_table.heading("job_status", text="Job Status", anchor=CENTER)

        for all_job in jobs:
            if all_job[7] in staff:
                self.staff_table.insert(
                    parent="",
                    index="end",
                    text="",
                    values=(
                        all_job[7],
                        all_job[0],
                        all_job[1],
                        all_job[2],
                        all_job[3],
                        all_job[4],
                        all_job[5],
                        all_job[6],
                    ),
                )

        self.staff_vsb = ttk.Scrollbar(
            root, orient="vertical", command=self.staff_table.yview
        )
        self.staff_table.configure(yscrollcommand=self.staff_vsb.set)
        self.staff_vsb.place(x=764, y=80)

        self.staff_table.grid(row=1, column=3)

    def add_staff(self):
        self.addstaff.destroy()
        self.main_menu_return.destroy()
        self.staff_table.destroy()
        self.staff_frame.destroy()
        self.staff_vsb.destroy()
        self.addstafftxt = Label(
            root, text="Add Staff", font=("Impact 60"), fg="white", bg="#5b5b5c"
        )
        self.addstafftxt.grid(row=0, column=3)

        self.spacer1 = Label(root, text="", bg="#5b5b5c")
        self.spacer1.grid(row=2, column=3)

        self.spacer2 = Label(root, text="", bg="#5b5b5c")
        self.spacer2.grid(row=3, column=3)

        self.stafftxt = Label(
            root,
            text="New Staff Name:",
            font=("Arial 12 bold"),
            fg="white",
            bg="#5b5b5c",
        )
        self.stafftxt.grid(row=4, column=3)
        self.new_staff_entry = Entry(root, width=20, justify="center")
        self.new_staff_entry.grid(row=5, column=3)

        self.spacer3 = Label(root, text="", bg="#5b5b5c")
        self.spacer3.grid(row=6, column=3)

        self.spacer4 = Label(root, text="", bg="#5b5b5c")
        self.spacer4.grid(row=7, column=3)

        self.spacer5 = Label(root, text="", bg="#5b5b5c")
        self.spacer5.grid(row=8, column=3)

        self.next_btn = Button(
            root,
            text="Add Staff",
            padx=30,
            pady=10,
            font=("Arial 12 bold"),
            borderwidth=6,
            command=self.new_staff,
        )
        self.next_btn.grid(row=9, column=3)

    def new_staff(self):
        staff = self.new_staff_entry.get()
        with open("staff.json", "r", encoding="UTF-8") as d:
            current_staff = json.load(d)

        for name in current_staff:
            if name[0] == self.username:
                if name[1] == staff:
                    messagebox.showerror("An error occured", "Staff already exists!")

        if staff == "":
            messagebox.showinfo("Entry Box Empty!", "Empty Add Staff entry box")

        else:
            new_staff = [self.username, staff]
            current_staff.append(new_staff)
            with open("staff.json", "w", encoding="UTF-8") as c:
                json.dump(current_staff, c)
            messagebox.showinfo("Success!", "Successfully added {}!".format(staff))

        self.addstafftxt.destroy()
        self.spacer1.destroy()
        self.spacer2.destroy()
        self.stafftxt.destroy()
        self.new_staff_entry.destroy()
        self.spacer3.destroy()
        self.spacer4.destroy()
        self.spacer5.destroy()
        self.next_btn.destroy()
        staff_tracker(root, self.username)

    def main_menu_btn(self):
        self.addstaff.destroy()
        self.main_menu_return.destroy()
        self.staff_table.destroy()
        self.staff_frame.destroy()
        self.staff_vsb.destroy()
        MainMenu(root, self.username)


class invoice_creation:
    def __init__(self, master, username):
        self.username = username
        self.root = master
        self.main_menu_return = Button(
            root,
            text="Return to Main Menu",
            padx=2,
            pady=2,
            font=("Arial 8 bold"),
            command=self.main_menu_return_passthrough,
        )
        self.main_menu_return.place(x=665, y=15)
        with open("jobs.json", "r", encoding="UTF-8") as d:
            all_jobs = json.load(d)
            users_jobs = []
            display_jobs = []
            for job in all_jobs:
                if job[0] == self.username:
                    users_jobs.append(job[1:])
                    display_jobs.append(job[1:4] + job[6:])

        self.invoicecreationtext = Label(
            root, text="Create Invoice", font=("Impact 60"), fg="white", bg="#5b5b5c"
        )
        self.invoicecreationtext.grid(row=0, column=3)
        self.select_job = StringVar()
        self.select_job.set("Select Job to create invoice for:")

        test_str = ""
        display_jobs2 = []
        for job in display_jobs:
            for item in job:
                test = str(item)
                test_str += " : " + test
            list_job = test_str[2:]
            display_jobs2.append(list_job)
            test_str = ""

        self.jobs_entry = OptionMenu(root, self.select_job, *display_jobs2)
        self.jobs_entry.grid(row=5, column=3)

        self.spacer2 = Label(root, text="", bg="#5b5b5c")
        self.spacer2.grid(row=4, column=3)

        self.r = IntVar()
        self.r.set("3")

        self.gstdroppeddown = False

        self.gsttxt = Label(
            root,
            text="Do you charge GST?",
            font="Arial 12 bold",
            fg="white",
            bg="#5b5b5c",
        )
        self.gsttxt.grid(row=1, column=3)

        self.gstbutton1 = Radiobutton(
            root,
            text="Yes",
            variable=self.r,
            value=1,
            bg="#5b5b5c",
            command=self.gst_dropdown,
        )
        self.gstbutton2 = Radiobutton(
            root,
            text="No",
            variable=self.r,
            value=2,
            bg="#5b5b5c",
            command=self.destroy_gstdropdown,
        )
        self.gstbutton1.grid(row=2, column=3)
        self.gstbutton2.grid(row=3, column=3)

        self.desclabel = Label(root, text="Description", bg="#5b5b5c", font="Arial 11")
        self.desclabel.place(x=8, y=240)

        self.quantitylabel = Label(root, text="Quantity", bg="#5b5b5c", font="Arial 11")
        self.quantitylabel.place(x=550, y=240)

        self.pricelabel = Label(root, text="Price", bg="#5b5b5c", font="Arial 11")
        self.pricelabel.place(x=675, y=240)

        self.descentrybox = Entry(root, width=85)
        self.descentrybox.place(x=8, y=265)

        self.quantityentrybox = Entry(root, width=16, justify="center")
        self.quantityentrybox.place(x=550, y=265)

        self.priceentrybox = Entry(root, width=19, justify="center")
        self.priceentrybox.place(x=675, y=265)

        self.descentrybox1 = Entry(root, width=85)
        self.quantityentrybox1 = Entry(root, width=16, justify="center")
        self.priceentrybox1 = Entry(root, width=19, justify="center")

        self.descentrybox2 = Entry(root, width=85)
        self.quantityentrybox2 = Entry(root, width=16, justify="center")
        self.priceentrybox2 = Entry(root, width=19, justify="center")

        self.descentrybox3 = Entry(root, width=85)
        self.quantityentrybox3 = Entry(root, width=16, justify="center")
        self.priceentrybox3 = Entry(root, width=19, justify="center")

        self.num = 0

        self.addnewline = Button(
            root,
            text="Add New Line",
            padx=2,
            pady=2,
            font=("Arial 8 bold"),
            command=self.newline,
        )
        self.addnewline.place(x=700, y=200)

        self.removeline = Button(
            root,
            text="Remove Line",
            padx=2,
            pady=2,
            font=("Arial 8 bold"),
            command=self.remove_line,
        )
        self.removeline.place(x=600, y=200)

        self.createinvoice_button = Button(
            root,
            text="Create Invoice",
            padx=30,
            pady=10,
            font=("Arial 12 bold"),
            borderwidth=6,
            command=self.invoice_create,
        )
        self.createinvoice_button.place(x=310, y=380)

        self.gstinclexcl = StringVar()
        self.gstinclexcl.set("Is GST Included or Excluded")
        gstoptions = ["GST Included", "GST Excluded"]
        self.gstdrowndown_menu = OptionMenu(root, self.gstinclexcl, *gstoptions)

    def gst_dropdown(self):
        self.gstdroppeddown == True
        self.gstdrowndown_menu.place(x=8, y=150)

    def destroy_gstdropdown(self):
        if self.gstdroppeddown == True:
            self.gstdrowndown_menu.place_forget()
            self.gstdroppeddown = False

    def newline(self):
        if self.num == 0:
            self.descentrybox1.place(x=8, y=290)
            self.quantityentrybox1.place(x=550, y=290)
            self.priceentrybox1.place(x=675, y=290)
            self.num += 1

        elif self.num == 1:
            self.descentrybox2.place(x=8, y=315)
            self.quantityentrybox2.place(x=550, y=315)
            self.priceentrybox2.place(x=675, y=315)
            self.num += 1

        elif self.num == 2:
            self.descentrybox3.place(x=8, y=340)
            self.quantityentrybox3.place(x=550, y=340)
            self.priceentrybox3.place(x=675, y=340)
            self.num += 1

        elif self.num == 3:
            self.num += 1
            self.maxlineerror = Label(
                root,
                text="Max number of lines reached",
                font=("Arial 12 bold"),
                fg="red",
                bg="#5b5b5c",
            )
            self.maxlineerror.place(x=8, y=420)

    def remove_line(self):
        if self.num == 1:
            self.descentrybox1.place_forget()
            self.quantityentrybox1.place_forget()
            self.priceentrybox1.place_forget()
            self.num -= 1

        elif self.num == 2:
            self.descentrybox2.place_forget()
            self.quantityentrybox2.place_forget()
            self.priceentrybox2.place_forget()
            self.num -= 1

        elif self.num == 3:
            self.descentrybox3.place_forget()
            self.quantityentrybox3.place_forget()
            self.priceentrybox3.place_forget()
            self.num -= 1

        elif self.num >= 4:
            self.descentrybox3.place_forget()
            self.quantityentrybox3.place_forget()
            self.priceentrybox3.place_forget()
            self.num = 2
            self.maxlineerror.place_forget()
            self.maxlineerror.place_forget()

    def invoice_create(self):
        self.errorchecknum = 0
        self.invoicelinecheck = 0
        self.invoice_create_error_check(
            self.descentrybox.get(),
            self.quantityentrybox.get(),
            self.priceentrybox.get(),
        )
        self.invoice_create_error_check(
            self.descentrybox1.get(),
            self.quantityentrybox1.get(),
            self.priceentrybox1.get(),
        )
        self.invoice_create_error_check(
            self.descentrybox2.get(),
            self.quantityentrybox2.get(),
            self.priceentrybox2.get(),
        )
        self.invoice_create_error_check(
            self.descentrybox3.get(),
            self.quantityentrybox3.get(),
            self.priceentrybox3.get(),
        )
        if str(self.select_job.get()) == "Select Job to create invoice for:":
            messagebox.showerror(
                "An error occured",
                "Please select a job to create the invoice for. If there is no job, please create one",
            )
            self.errorchecknum += 1

        if self.r.get() == 3:
            messagebox.showerror(
                "An error occured", "Please select whether you charge GST or do not"
            )
            self.errorchecknum += 1

        if self.gstdroppeddown == True:
            if str(self.gstinclexcl.get()) == "Is GST Included or Excluded":
                messagebox.showerror(
                    "An error occured",
                    "Please select whether GST is included in the price or excluded",
                )
                self.errorchecknum += 1

        if self.invoicelinecheck == 4:
            messagebox.showerror(
                "An error occured", "Please write down atleast 1 line for your invoice"
            )

        if self.errorchecknum == 0:
            lines = []
            self.line_check(
                self.descentrybox.get(),
                self.quantityentrybox.get(),
                self.priceentrybox.get(),
                lines,
            )
            self.line_check(
                self.descentrybox1.get(),
                self.quantityentrybox1.get(),
                self.priceentrybox1.get(),
                lines,
            )
            self.line_check(
                self.descentrybox2.get(),
                self.quantityentrybox2.get(),
                self.priceentrybox2.get(),
                lines,
            )
            self.line_check(
                self.descentrybox3.get(),
                self.quantityentrybox3.get(),
                self.priceentrybox3.get(),
                lines,
            )

            with open("jobs.json", "r", encoding="UTF-8") as l:
                all_jobs = json.load(l)
                for job in all_jobs:
                    if job[0] == self.username:
                        if int(job[1]) == int(self.select_job.get()[1]):
                            name = job[2]
                            address = job[5]
                            phone_number = job[4]
                            email = job[3]

            current_datetime = datetime.datetime.now()

            formatted_date = current_datetime.strftime("%d / %m / %Y")

            subtotal = sum(line["quantity"] * line["unit_price"] for line in lines)

            gst = sum(line["GST"] for line in lines)

            total = sum(line["total"] for line in lines)

            pdf_file = filedialog.asksaveasfilename(
                defaultextension=".pdf",
                filetypes=[("PDF files", "*.pdf")],
                initialfile=f"invoice{self.select_job.get()[1]}",
            )

            doc = SimpleDocTemplate(pdf_file, pagesize=letter)

            pdftext = []

            styles = getSampleStyleSheet()

            header = Paragraph("Invoice", styles["Heading1"])
            pdftext.append(header)
            right_align = styles["Heading5"]
            right_align.alignment = 2
            datetext = Paragraph("Date: {}".format(formatted_date), right_align)
            pdftext.append(datetext)
            pdftext.append(
                Paragraph(
                    "Job Number: {}".format(int(self.select_job.get()[1])), right_align
                )
            )

            pdftext.append(Paragraph("Invoice Billed to:", styles["Heading4"]))
            pdftext.append(Paragraph("Name: {}".format(name), styles["Normal"]))
            pdftext.append(Paragraph("Address: {}".format(address), styles["Normal"]))
            pdftext.append(
                Paragraph("Phone: {}".format(phone_number), styles["Normal"])
            )
            pdftext.append(Paragraph("Email: {}".format(email), styles["Normal"]))

            # Itemized list
            spacer = Spacer(1, 40)
            pdftext.append(spacer)

            data = [["Description", "Quantity", "Unit Price", "GST", "Total"]]
            for line in lines:
                data.append(
                    [
                        line["description"],
                        line["quantity"],
                        "${:.2f}".format(line["unit_price"]),
                        "${:.2f}".format(line["GST"]),
                        "${:.2f}".format(line["total"]),
                    ]
                )

            # Create a table for the itemized list
            table = Table(
                data, colWidths=[4 * inch, 1 * inch, 1 * inch, 1 * inch, 1.5 * inch]
            )
            table.setStyle(
                TableStyle(
                    [
                        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
                        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
                        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                        ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
                        ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
                        ("GRID", (0, 0), (-1, -1), 1, colors.black),
                    ]
                )
            )

            pdftext.append(table)

            # Subtotal and Total
            pdftext.append(spacer)

            pdftext.append(
                Paragraph("Subtotal: ${:.2f}".format(subtotal), styles["Heading4"])
            )
            pdftext.append(Paragraph("GST: ${:.2f}".format(gst), styles["Heading4"]))

            pdftext.append(
                Paragraph("Total: ${:.2f}".format(total), styles["Heading2"])
            )

            # Build the PDF
            if pdf_file:
                doc.build(pdftext)
                with open("jobs.json", "r", encoding="UTF-8") as l:
                    all_jobs = json.load(l)
                    for job in all_jobs:
                        if job[0] == self.username:
                            if int(job[1]) == int(self.select_job.get()[1]):
                                test123 = all_jobs.index(job)
                                all_jobs.pop(test123)

                with open("jobs.json", "w", encoding="UTF-8") as p:
                    json.dump(all_jobs, p)

                self.main_menu_return_passthrough()

    def invoice_create_error_check(self, desc, quantity, price):

        if (desc or quantity or price) and not (desc and quantity and price):
            messagebox.showerror(
                "An error occured",
                f"Please input all 3 inputs (Description, quantity, "
                f"and Price) for each line you write. \n Line that caused the Error: \n"
                f"Description: {desc} \n quantity: {quantity} \n Price: {price}",
            )
            self.errorchecknum += 1

        if desc and quantity and price == "":
            self.invoicelinecheck += 1

        if quantity == "":
            pass

        else:
            try:
                float(quantity)

            except ValueError:
                messagebox.showerror(
                    "An error occured",
                    "Please make sure that the quantity is a number and contains no other characters",
                )
                self.errorchecknum += 1

        if price == "":
            pass

        else:
            try:
                if len(price) == 1:
                    if price.isnumeric():
                        pass
                    else:
                        messagebox.showerror(
                            "An error occured",
                            "Please make sure that the price is a"
                            "number and contains no other characters other than $ symbol",
                        )
                else:
                    float(price[1:])
                    if price[0] == "$":
                        pass
                    elif price[0].isnumeric():
                        pass

                    else:
                        messagebox.showerror(
                            "An error occured",
                            "Please make sure that the price is"
                            "a number and contains no other characters other than $ symbol",
                        )
                        self.errorchecknum += 1

            except ValueError:
                messagebox.showerror(
                    "An error occured",
                    "Please make sure that the price is a number and contains no other characters other than $ sym",
                )
                self.errorchecknum += 1

        if len(desc) > 200:
            messagebox.showerror(
                "An error occured",
                "Too many characters in"
                "Description, please shorten it to 200 or under",
            )
            self.errorchecknum += 1

        if len(quantity) > 8:
            messagebox.showerror(
                "An error occured",
                "Too many characters" "in quantity, please shorten it to 8 or under",
            )
            self.errorchecknum += 1

        if len(price) > 12:
            messagebox.showerror(
                "An error occured",
                "Too many characters in" "Price, please shorten it to 12 or under",
            )
            self.errorchecknum += 1

    def line_check(self, desc, quantity, price, lines):
        if desc == "":
            pass
        else:
            fquantity = float(quantity)
            fprice = float(price)
            total1 = fquantity * fprice

            gst = 0
            if self.r.get() == 1:
                if self.gstinclexcl.get() == "GST Excluded":
                    gst = total1 * 0.15
                    total = total1 + gst
                else:
                    gst = total1 - (total1 / 1.15)
                    total = total1
            else:
                gst = 0
                total = total1

            linedict = {
                "description": desc,
                "quantity": float(quantity),
                "unit_price": float(price),
                "GST": float(gst),
                "total": float(total),
            }
            lines.append(linedict)
            return lines

    def main_menu_return_passthrough(self):
        self.main_menu_return.destroy()
        self.quantityentrybox.destroy()
        self.quantityentrybox1.destroy()
        self.quantityentrybox2.destroy()
        self.quantityentrybox3.destroy()
        self.descentrybox.destroy()
        self.descentrybox1.destroy()
        self.descentrybox2.destroy()
        self.descentrybox3.destroy()
        self.priceentrybox.destroy()
        self.priceentrybox1.destroy()
        self.priceentrybox2.destroy()
        self.priceentrybox3.destroy()
        self.desclabel.destroy()
        self.quantitylabel.destroy()
        self.pricelabel.destroy()
        self.createinvoice_button.destroy()
        self.invoicecreationtext.destroy()
        self.gsttxt.destroy()
        self.gstbutton1.destroy()
        self.gstbutton2.destroy()
        self.spacer2.destroy()
        self.jobs_entry.destroy()
        self.addnewline.destroy()
        self.removeline.destroy()

        if self.gstdroppeddown == True:
            self.gstdrowndown_menu.destroy()

        if self.num >= 4:
            self.maxlineerror.destroy()

        MainMenu(root, self.username)


def main():
    Login(root)
    root.mainloop()


if __name__ == "__main__":
    main()
