"""This progam provides features that help electrians manage their jobs and to create invoices"""
#Importing everything needed to run the program
from tkinter import messagebox, ttk, filedialog, Tk, Entry, Label, Button
from tkinter import Frame, CENTER, LabelFrame, StringVar, OptionMenu, NO, IntVar, Radiobutton
import json
import datetime
import hashlib
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.units import inch
#Configuring the GUI
root = Tk()
root.title("Electrical Job Management Software")
root.iconbitmap("ElecTRICIAN JOB MANAGEMENT SOFTWARE (2).ico")
root.geometry("800x450")
root.configure(bg="#5b5b5c")
root.columnconfigure(3, weight=1)


class SignUp:
    """This GUI creates an account for the user"""

    def __init__(self, master):
        self.root = master
        #Creates the GUI
        self.sign_up_txt = Label(root, text="Sign Up", font=(
            "Impact 80"), fg="white", bg="#5b5b5c")
        self.sign_up_txt.grid(row=0, column=3)

        self.username_txt = Label(root, text="Create a Username", font=(
            "Arial 12 bold"), fg="white", bg="#5b5b5c")
        self.username_txt.grid(row=1, column=3)
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

        self.confirm_pwd_txt = Label(root, text="Confirm Password", font=(
            "Arial 12 bold"), fg="white", bg="#5b5b5c")
        self.confirm_pwd_txt.grid(row=7, column=3)
        self.confirm_password = Entry(
            root, width=20, justify="center", show="*")
        self.confirm_password.grid(row=8, column=3)

        self.spacer3 = Label(root, text="", bg="#5b5b5c")
        self.spacer3.grid(row=9, column=3)

        self.sign_up_button = Button(root, text="Sign Up", padx=30,
                                    pady=10, font=("Arial 12 bold"),
                                    borderwidth=6, command=lambda: signup_process
                                    (self.username_entry.get(), self.password.get(),
                                     self.confirm_password.get()))
        self.sign_up_button.grid(row=10, column=3)

        self.spacer3 = Label(root, text="", bg="#5b5b5c")
        self.spacer3.grid(row=11, column=3)

        self.login_pass_through_btn = Button(
            root, text="Already have an account? Press here to Login", font=("Arial 12 bold"),
            bg="#5b5b5c", fg="#0381ff", bd=0, command=self.login_pass_through)
        self.login_pass_through_btn.grid(row=12, column=3)

        #Checks for errors if none, creates the account for the user
        def signup_process(username, pwd, confirm_pwd):
            with open("usernames.json", encoding="UTF-8") as json_usernames:
                user_pass = json.load(json_usernames)
                users = [user[0]for user in user_pass]
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

            elif pwd != confirm_pwd:
                messagebox.showerror("An error occured",
                                     "Error, Passwords must match!")

            elif username in users:
                messagebox.showinfo("Username already Taken!", "The username you have "
                                    "inputed is already taken! Please choose a different username")
            else:
                #Hashs the password
                encoded_pwd = pwd.encode("utf-8")
                hashed_pwd = hashlib.sha256(encoded_pwd).hexdigest()
                new_user = [username, str(hashed_pwd)]
                user_pass.append(new_user)

                #Writes the new user's username and password to the usernames json
                with open("usernames.json", "w", encoding="UTF-8") as j:
                    json.dump(user_pass, j)
                messagebox.showinfo("Success!", "Sucessfully Signed Up")
                self.sign_up_txt.destroy()
                self.username_txt.destroy()
                self.username_entry.destroy()
                self.spacer1.destroy()
                self.pwd_txt.destroy()
                self.password.destroy()
                self.spacer2.destroy()
                self.confirm_pwd_txt.destroy()
                self.confirm_password.destroy()
                self.spacer3.destroy()
                self.sign_up_button.destroy()
                self.login_pass_through_btn.destroy()
                Login(root)

    def login_pass_through(self):
        """Sends the user from the Sign Up page to the Login page"""
        self.sign_up_txt.destroy()
        self.username_txt.destroy()
        self.username_entry.destroy()
        self.spacer1.destroy()
        self.pwd_txt.destroy()
        self.password.destroy()
        self.spacer2.destroy()
        self.confirm_pwd_txt.destroy()
        self.confirm_password.destroy()
        self.spacer3.destroy()
        self.sign_up_button.destroy()
        self.login_pass_through_btn.destroy()
        Login(root)


class Login:
    """Logins the user into their account"""

    def __init__(self, master):
        self.root = master
        #Creates the GUI
        self.login_txt = Label(root, text="Login", font=(
            "Impact 80"), fg="white", bg="#5b5b5c")
        self.login_txt.grid(row=0, column=3)

        self.user_txt = Label(root, text="Username:", font=(
            "Arial 12 bold"), fg="white", bg="#5b5b5c")
        self.user_txt.grid(row=1, column=3)
        self.user_entry = Entry(root, width=20, justify="center")
        self.user_entry.grid(row=2, column=3)

        self.spacer1 = Label(root, text="", bg="#5b5b5c")
        self.spacer1.grid(row=3, column=3)

        self.pwd_txt = Label(root, text="Password:", font=(
            "Arial 12 bold"), fg="white", bg="#5b5b5c")
        self.pwd_txt.grid(row=4, column=3)
        self.pwd_entry = Entry(root, width=20, justify="center", show="*")
        self.pwd_entry.grid(row=5, column=3)

        self.spacer2 = Label(root, text="", bg="#5b5b5c")
        self.spacer2.grid(row=6, column=3)

        self.login_button = Button(root, text="Login", padx=30,
                                   pady=10, font=("Arial 12 bold"), borderwidth=6,
                                   command=lambda: login_process
                                   (self.user_entry.get(), self.pwd_entry.get()))
        self.login_button.grid(row=8, column=3)

        self.spacer3 = Label(root, text="", bg="#5b5b5c")
        self.spacer3.grid(row=9, column=3)

        self.sign_up_pass_btn = Button(
            root, text="Don't have an account? Press here to Sign Up", font=("Arial 12 bold"),
            bg="#5b5b5c", fg="#0381ff", bd=0, command=self.sign_up_pass_through)
        self.sign_up_pass_btn.grid(row=10, column=3)

        def login_process(username, password):
            #Opens the usernames json and loads it to a variable
            with open("usernames.json", encoding="UTF-8") as username_json:
                user_pass = json.load(username_json)
                users = [user[0]for user in user_pass]

            if "" == username:
                messagebox.showinfo("Entry Box Empty!", "Empty Username box!")

            elif "" == password:
                messagebox.showinfo("Entry Box Empty!", "Empty Password box!")

            elif username in users:
                #Checks if the password entered matches the username's password
                position = users.index(username)
                passw = str(password).encode("utf-8")
                entry_hashed_pw = hashlib.sha256(passw).hexdigest()

                if entry_hashed_pw == user_pass[position][1]:
                    self.login_txt.destroy()
                    self.user_txt.destroy()
                    self.user_entry.destroy()
                    self.spacer1.destroy()
                    self.pwd_txt.destroy()
                    self.pwd_entry.destroy()
                    self.spacer2.destroy()
                    self.login_button.destroy()
                    self.sign_up_pass_btn.destroy()
                    MainMenu(root, username)

                else:
                    messagebox.showerror(
                        "An error occured", "Username or Password is incorrect, please try again")
            else:
                messagebox.showerror(
                    "An error occured", "Username or Password is incorrect, please try again")

    def sign_up_pass_through(self):
        """Sends the user to the Sign Up page from the Login Page"""
        self.login_txt.destroy()
        self.user_txt.destroy()
        self.user_entry.destroy()
        self.spacer1.destroy()
        self.pwd_txt.destroy()
        self.pwd_entry.destroy()
        self.spacer2.destroy()
        self.login_button.destroy()
        self.sign_up_pass_btn.destroy()
        SignUp(root)


class MainMenu:
    """This is the Main Menu of the GUI"""

    def __init__(self, master, username):
        self.root = master
        self.username = username
        #Creating the GUI
        self.add_job_btn = Button(root, text="Add Job", padx=30, pady=10, font=(
            "Arial 14 bold"), borderwidth=6, command=self.add_job)
        self.add_job_btn.place(x=275, y=22)

        self.staff_tracker_btn = Button(root, text="Staff Tracker", padx=30, pady=10, font=(
            "Arial 14 bold"), borderwidth=6, command=self.staff_tracker)
        self.staff_tracker_btn.place(x=20, y=22)

        self.create_invoice_btn = Button(root, text="Create Invoice or Quote",
                                         padx=30, pady=10, font=("Arial 14 bold")
                                         , borderwidth=6, command=self.create_invoice)
        self.create_invoice_btn.place(x=480, y=22)

        #Making the jobs table
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
        self.jobs.heading("job_num", text="Job #",anchor=CENTER)
        self.jobs.heading("name", text="Client Name",anchor=CENTER)
        self.jobs.heading("email", text="Email",anchor=CENTER)
        self.jobs.heading("phe_num", text="Phone Number",anchor=CENTER)
        self.jobs.heading("address", text="Address",anchor=CENTER)
        self.jobs.heading("job_type", text="Job Type",anchor=CENTER)
        self.jobs.heading("job_status", text="Job Status",anchor=CENTER)
        self.jobs.heading("staff", text="Staff",anchor=CENTER)

        num = 0

        for i in jobs:
            self.jobs.insert(parent='', index='end', iid=num, text='',
                             values=jobs[num])
            num += 1

        self.jobs.grid(row=1, column=3)

    def add_job(self):
        """Sends the user from Main Menu to Add Job and checks if the user can create a job"""

        #Checks if the user has staff
        with open("staff.json", encoding="UTF-8") as filed_staff:
            all_staff = json.load(filed_staff)
            staff = []
            for indiv_staff in all_staff:
                if indiv_staff[0] == self.username:
                    staff.append(indiv_staff[1])
        if len(staff) == 0:
            messagebox.showinfo("No staff found!", "You must have staff before you create a "
                                "job! Please navigate to 'Staff Tracker' to create new staff")
        else:
            self.add_job_btn.destroy()
            self.staff_tracker_btn.destroy()
            self.create_invoice_btn.destroy()
            self.jobs_frame.destroy()
            AddJob(root, self.username)

    def staff_tracker(self):
        """Sends the user from the Main Menu to the Staff Tracker"""
        self.add_job_btn.destroy()
        self.staff_tracker_btn.destroy()
        self.create_invoice_btn.destroy()
        self.jobs_frame.destroy()
        StaffTracker(root, self.username)

    def create_invoice(self):
        """Sends the user from the Main Menu to 
        Create Invoice and checks if they can create an invoice"""

        #Checks if the user has Jobs to create the invoice
        with open("jobs.json", "r", encoding="UTF-8") as json_jobs:
            all_jobs = json.load(json_jobs)
            users_jobs = []
            for job in all_jobs:
                if job[0] == self.username:
                    users_jobs.append(job[1:])

        if len(users_jobs) == 0:
            messagebox.showinfo("No jobs found!", 'You must have jobs before '
                                'you create an invoice, please naviagate to "Add Job"' )

        else:
            self.add_job_btn.destroy()
            self.staff_tracker_btn.destroy()
            self.create_invoice_btn.destroy()
            self.jobs_frame.destroy()
            InvoiceCreation(root, self.username)


class AddJob:
    """Creates a new job for the user"""

    def __init__(self, master, username):
        self.root = master
        self.username = username
        #Creating the GUI
        self.main_menu_return = Button(
            root, text="Return to Main Menu", padx=2, pady=2, font=(
            "Arial 8 bold"), command=lambda: main_menu_return(frame, self.main_menu_return))
        self.main_menu_return.place(x=672, y=8)
        frame = LabelFrame(root, padx=5, pady=5, bg="#5b5b5c")
        frame.grid(row=0, column=3)

        add_job_txt = Label(frame, text="Add Job", font=(
            "Impact 60"), fg="white", bg="#5b5b5c")
        add_job_txt.grid(row=1, column=3)

        name_txt = Label(frame, text="Client's Name", font=(
            "Arial 13 bold"), fg="white", bg="#5b5b5c")
        name_txt.grid(row=2, column=3)
        name_entry = Entry(frame, width=20, justify="center")
        name_entry.grid(row=3, column=3)

        spacer1 = Label(frame, text="", bg="#5b5b5c")
        spacer1.grid(row=4, column=3)

        email_txt = Label(frame, text="Client's Email Address", font=(
            "Arial 13 bold"), fg="white", bg="#5b5b5c")
        email_txt.grid(row=5, column=3)
        email_entry = Entry(frame, width=20, justify="center")
        email_entry.grid(row=6, column=3)

        spacer2 = Label(frame, text="", bg="#5b5b5c")
        spacer2.grid(row=7, column=3)

        phne_num_txt = Label(frame, text="Client's Phone Number", font=(
            "Arial 13 bold"), fg="white", bg="#5b5b5c")
        phne_num_txt.grid(row=8, column=3)
        phnenum_entry = Entry(frame, width=20, justify="center")
        phnenum_entry.grid(row=9, column=3)

        spacer3 = Label(frame, text="", bg="#5b5b5c")
        spacer3.grid(row=10, column=3)

        address_txt = Label(frame, text="Client's Site Address", font=(
            "Arial 13 bold"), fg="white", bg="#5b5b5c")
        address_txt.grid(row=11, column=3)
        address_entry = Entry(frame, width=20, justify="center")
        address_entry.grid(row=12, column=3)

        spacer4 = Label(frame, text="", bg="#5b5b5c")
        spacer4.grid(row=13, column=3)

        next_btn = Button(frame, text="Next", padx=30, pady=10,
                          font=("Arial 12 bold"), command=lambda: add_job2(
                          name_entry.get(), email_entry.get(),
                          phnenum_entry.get(), address_entry.get(), frame))
        next_btn.grid(row=14, column=3)

        def add_job2(name, email, phnenum, address, frame):
            #Checking for errors
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
                    "Entry Box Empty!", "Empty Client's Phone "
                    "Number Box! Please enter the client's phone number")

            elif address == "":
                messagebox.showinfo(
                    "Entry Box Empty!", "Empty Client's "
                    "Address Box! Please enter the client's address")

            else:
                #Creating the next GUI
                frame.grid_forget()
                self.main_menu_return.destroy()

                frame1 = LabelFrame(root, padx=5, pady=5, bg="#5b5b5c")
                frame1.grid(row=0, column=3)

                main_menu_return1 = Button(
                    root, text="Return to Main Menu", padx=2, pady=2, font=(
            "Arial 8 bold"),command=lambda: main_menu_return(frame1, main_menu_return1))
                main_menu_return1.place(x=672, y=8)

                add_job_txt = Label(frame1, text="Add Job", font=(
                    "Impact 60"), fg="white", bg="#5b5b5c")
                add_job_txt.grid(row=1, column=3)

                job_type_txt = Label(frame1, text="Job Type", font=(
                    "Arial 16 bold"), fg="white", bg="#5b5b5c")
                job_type_txt.grid(row=2, column=3)
                job_type_default = StringVar()
                job_type_default.set("Select Job Type")
                job_types = ["Charge Up", "Quote", "Estimate"]
                job_type_entry = OptionMenu(frame1, job_type_default, *job_types)
                job_type_entry.grid(row=3, column=3)

                spacer1 = Label(frame1, text="", bg="#5b5b5c")
                spacer1.grid(row=4, column=3)

                job_status_txt = Label(frame1, text="Job Status", font=(
                    "Arial 16 bold"), fg="white", bg="#5b5b5c")
                job_status_txt.grid(row=5, column=3)
                job_status_default = StringVar()
                job_status_default.set("Select Job Status")
                job_statuses = ["In Progress", "Scheduled", "Pending", "On Hold", "Completed"]
                job_status_entry = OptionMenu(
                    frame1, job_status_default, *job_statuses)
                job_status_entry.grid(row=6, column=3)

                spacer2 = Label(frame1, text="", bg="#5b5b5c")
                spacer2.grid(row=7, column=3)

                staff_txt = Label(frame1, text="Staff", font=(
                    "Arial 16 bold"), fg="white", bg="#5b5b5c")
                staff_txt.grid(row=8, column=3)
                staff_default = StringVar()
                staff_default.set("Select Staff")
                with open("staff.json", encoding="UTF-8") as json_staff:
                    all_staff = json.load(json_staff)

                staff = ["temp"]
                staff.pop(0)
                for indiv_staff in all_staff:
                    if indiv_staff[0] == username:
                        staff.append(indiv_staff[1])

                staff_entry = OptionMenu(frame1, staff_default, *staff)
                staff_entry.grid(row=9, column=3)

                spacer3 = Label(frame1, text="", bg="#5b5b5c")
                spacer3.grid(row=10, column=3)

                add_job_btn = Button(frame1, text="Add New Job", padx=22, pady=10,
                    font=("Arial 12 bold"), command=lambda: add_job_process(
                    name, email, phnenum, address, job_type_default.get(), job_status_default.get(),
                    staff_default.get(), frame1, main_menu_return1))

                add_job_btn.grid(row=11, column=3)

        def add_job_process(name, email, phnenum, address, job_type,
                            job_status, staff, frame, return_button):
            #Checking for errors
            if job_type == "Select Job Type":
                messagebox.showerror("An error occured", "You must select a job type")

            elif job_status == "Select Job Status":
                messagebox.showerror("An error occured", "You must select a job status")

            elif staff == "Select Staff":
                messagebox.showerror("An error occured", "You must select a staff member")

            else:
                #Adding the new job to the jobs json file
                with open("jobs.json", "r", encoding="UTF-8") as json_jobs:
                    existing_jobs = json.load(json_jobs)

                job_num = 0
                for job in existing_jobs:
                    if job[0] == username:
                        job_num += 1

                for i in range(0, len(existing_jobs)+1):
                    for indiv_job in existing_jobs:
                        if indiv_job[0] == username and indiv_job[1] == job_num:
                            job_num += 1

                new_job = [username, job_num, name, email, phnenum,
                        address, job_type, job_status, staff]

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


class StaffTracker:
    """Tracks the individual staff's job's"""

    def __init__(self, master, username):
        self.username = username
        self.root = master
        #Variables for the Add Staff GUI
        self.staff_tracker = Button(root, text="Return to Staff Tracker", padx=2, pady=2, font=(
            "Arial 8 bold"), command=self.destroy_new_staff)
        self.next_btn = Button(root, text="Add Staff", padx=30,
                               pady=10, font=("Arial 12 bold"),
                               borderwidth=6,  command=self.new_staff)
        self.spacer1 = Label(root, text="", bg="#5b5b5c")
        self.spacer2 = Label(root, text="", bg="#5b5b5c")
        self.spacer3 = Label(root, text="", bg="#5b5b5c")
        self.spacer4 = Label(root, text="", bg="#5b5b5c")
        self.spacer5 = Label(root, text="", bg="#5b5b5c")
        self.new_staff_entry = Entry(root, width=20, justify="center")
        self.staff_txt = Label(root, text="New Staff Name:", font=(
            "Arial 12 bold"), fg="white", bg="#5b5b5c")
        self.add_staff_txt = Label(root, text="Add Staff", font=(
            "Impact 60"), fg="white", bg="#5b5b5c")

        #Creating the main staff tracker GUI
        self.main_menu_return = Button(root, text="Return to Main Menu", padx=2, pady=2, font=(
            "Arial 8 bold"), command=self.main_menu_btn)
        self.main_menu_return.place(x=665, y=15)
        self.add_staff_btn = Button(root, text="Add Staff", padx=2, pady=2, font=(
            "Arial 8 bold"), command=self.add_staff)
        self.add_staff_btn.place(x=10, y=15)

        #Creating the staff tracker table
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

        with open("staff.json", encoding="UTF-8") as staff_json:
            all_staff = json.load(staff_json)

        for staff_item in all_staff:
            if staff_item[0] == username:
                staff.append(staff_item[1])

        height_num = 0

        for each_job in jobs:
            if each_job[7] in staff:
                height_num += 1

        self.staff_table = ttk.Treeview(self.staff_frame, height=height_num)

        self.staff_table['columns'] = ("staff",'job_num', 'name',
                                'email', 'phe_num', 'address', "job_type", "job_status")

        self.staff_table.column("#0", width=0,  stretch=NO)
        self.staff_table.column("staff", anchor=CENTER, width= 88)
        self.staff_table.column("job_num", anchor=CENTER, width=42)
        self.staff_table.column("name", anchor=CENTER, width=110)
        self.staff_table.column("email", anchor=CENTER, width=120)
        self.staff_table.column("phe_num", anchor=CENTER, width=90)
        self.staff_table.column("address", anchor=CENTER, width=100)
        self.staff_table.column("job_type", anchor=CENTER, width=83)
        self.staff_table.column("job_status", anchor=CENTER, width=110)

        self.staff_table.heading("#0", text="", anchor=CENTER)
        self.staff_table.heading("staff", text="Staff:")
        self.staff_table.heading("job_num", text="Job #",
                          anchor=CENTER)
        self.staff_table.heading("name", text="Client Name",
                          anchor=CENTER)
        self.staff_table.heading("email", text="Email",
                          anchor=CENTER)
        self.staff_table.heading("phe_num", text="Phone Number",
                          anchor=CENTER)
        self.staff_table.heading("address", text="Address",
                          anchor=CENTER)
        self.staff_table.heading("job_type", text="Job Type",
                          anchor=CENTER)
        self.staff_table.heading("job_status", text="Job Status",
                          anchor=CENTER)

        for all_job in jobs:
            if all_job[7] in staff:
                self.staff_table.insert(parent='', index='end', text='',
                                        values=(all_job[7], all_job[0], all_job[1],
                                                all_job[2], all_job[3], all_job[4],
                                                all_job[5], all_job[6]))

        self.staff_vsb = ttk.Scrollbar(root, orient="vertical", command=self.staff_table.yview)
        self.staff_table.configure(yscrollcommand=self.staff_vsb.set)
        self.staff_vsb.place(x=764, y=80)
        self.staff_table.grid(row=1, column=3)


    def add_staff(self):
        """Sends the user to the Add Staff GUI"""
        self.add_staff_btn.destroy()
        self.main_menu_return.destroy()
        self.staff_table.destroy()
        self.staff_frame.destroy()
        self.staff_vsb.destroy()
        self.add_staff_txt.grid(row=0, column=3)
        self.spacer1.grid(row=2, column=3)
        self.spacer2.grid(row=3, column=3)
        self.staff_txt.grid(row=4, column=3)
        self.new_staff_entry.grid(row=5, column=3)
        self.spacer3.grid(row=6, column=3)
        self.spacer4.grid(row=7, column=3)
        self.spacer5.grid(row=8, column=3)
        self.next_btn.grid(row=9, column=3)
        self.staff_tracker.place(x=658, y=15)


    def new_staff(self):
        """Adds the new staff to the file and error checks"""
        staff = self.new_staff_entry.get()
        with open("staff.json", "r", encoding="UTF-8") as staff_file:
            current_staff = json.load(staff_file)

        for name in current_staff:
            if name[0] == self.username:
                if name[1] == staff:
                    messagebox.showerror(
                        "An error occured", "Staff already exists!")

        if staff == "":
            messagebox.showinfo("Entry Box Empty!",
                                "Empty Add Staff entry box")

        else:
            new_staff = [self.username, staff]
            current_staff.append(new_staff)
            with open("staff.json", "w", encoding="UTF-8") as file_staff:
                json.dump(current_staff, file_staff)
            messagebox.showinfo(
                "Success!", f"Successfully added {staff}!")
            self.destroy_new_staff()


    def destroy_new_staff(self):
        """Sends the user back to the staff tracker"""
        self.add_staff_txt.destroy()
        self.spacer1.destroy()
        self.spacer2.destroy()
        self.staff_txt.destroy()
        self.new_staff_entry.destroy()
        self.spacer3.destroy()
        self.spacer4.destroy()
        self.spacer5.destroy()
        self.next_btn.destroy()
        self.staff_tracker.destroy()
        StaffTracker(root, self.username)

    def main_menu_btn(self):
        """Sends the user back to the Main Menu"""
        self.add_staff_btn.destroy()
        self.main_menu_return.destroy()
        self.staff_table.destroy()
        self.staff_frame.destroy()
        self.staff_vsb.destroy()
        MainMenu(root, self.username)


class InvoiceCreation:
    """Displays the invoice creation GUI and creates the invoice"""

    def __init__(self, master, username):
        self.username = username
        self.root = master
        self.error_check_num = 0
        self.invoice_line_check = 0
        #Creating the Invoice Creation GUI
        self.max_line_error = Label(root, text="Max number of lines reached", font=(
                "Arial 12 bold"), fg="red", bg="#5b5b5c")
        self.main_menu_return = Button(root, text="Return to Main Menu", padx=2, pady=2, font=(
            "Arial 8 bold"), command=self.main_menu_return_passthrough)
        self.main_menu_return.place(x=665, y=15)
        with open("jobs.json", "r", encoding="UTF-8") as file_jobs:
            all_jobs = json.load(file_jobs)
            users_jobs = []
            display_jobs = []
            for job in all_jobs:
                if job[0] == self.username:
                    users_jobs.append(job[1:])
                    display_jobs.append(job[1:4] + job[6:])

        self.invoice_creation_text = Label(root, text="Create Invoice", font=(
            "Impact 60"), fg="white", bg="#5b5b5c")
        self.invoice_creation_text.grid(row=0, column=3)
        self.select_job = StringVar()
        self.select_job.set("Select Job to create invoice for:")

        job_str = ""
        display_jobs2 = ["temp"]
        display_jobs2.pop(0)
        for job in display_jobs:
            for item in job:
                str_job = str(item)
                job_str += (" : " + str_job)
            list_job = job_str[2:]
            display_jobs2.append(list_job)
            job_str = ""

        self.jobs_entry = OptionMenu(root, self.select_job,
                                     *display_jobs2)
        self.jobs_entry.grid(row=5, column=3)

        self.spacer2 = Label(root, text="", bg="#5b5b5c")
        self.spacer2.grid(row=4, column=3)

        self.gst_num = IntVar()
        self.gst_num.set("3")

        self.gst_dropped_down = False

        self.gst_txt = Label(root, text="Do you charge GST?", font=
            "Arial 12 bold", fg="white", bg="#5b5b5c")
        self.gst_txt.grid(row=1, column=3)

        self.gst_button1 = Radiobutton(
            root, text="Yes", variable=self.gst_num, value=1,
            bg="#5b5b5c", command=self.gst_dropdown)
        self.gst_button2 = Radiobutton(
            root, text="No", variable=self.gst_num, value=2,
            bg="#5b5b5c", command=self.destroy_gstdropdown)
        self.gst_button1.grid(row=2, column=3)
        self.gst_button2.grid(row=3, column=3)

        self.desc_label = Label(root, text="Description",
                               bg="#5b5b5c", font="Arial 11")
        self.desc_label.place(x=8, y=240)

        self.quantity_label = Label(
            root, text="Quantity", bg="#5b5b5c", font="Arial 11")
        self.quantity_label.place(x=550, y=240)

        self.price_label = Label(
            root, text="Price", bg="#5b5b5c", font="Arial 11")
        self.price_label.place(x=675, y=240)

        self.desc_entry_box = Entry(root, width=85)
        self.desc_entry_box.place(x=8, y=265)

        self.quantity_entry_box = Entry(root, width=16, justify="center")
        self.quantity_entry_box.place(x=550, y=265)

        self.price_entry_box = Entry(root, width=19, justify="center")
        self.price_entry_box.place(x=675, y=265)

        self.desc_entry_box1 = Entry(root, width=85)
        self.quantity_entry_box1 = Entry(root, width=16, justify="center")
        self.price_entry_box1 = Entry(root, width=19, justify="center")

        self.desc_entry_box2 = Entry(root, width=85)
        self.quantity_entry_box2 = Entry(root, width=16, justify="center")
        self.price_entry_box2 = Entry(root, width=19, justify="center")

        self.desc_entry_box3 = Entry(root, width=85)
        self.quantity_entry_box3 = Entry(root, width=16, justify="center")
        self.price_entry_box3 = Entry(root, width=19, justify="center")

        self.num = 0

        self.add_new_line = Button(root, text="Add New Line", padx=2, pady=2, font=(
            "Arial 8 bold"), command=self.newline)
        self.add_new_line.place(x=700, y=200)

        self.remove_line_btn = Button(root, text="Remove Line", padx=2, pady=2, font=(
            "Arial 8 bold"), command=self.remove_line)
        self.remove_line_btn.place(x=600, y=200)

        self.create_inovice_button = Button(root, text="Create Invoice", padx=30,
                                           pady=10, font="Arial 12 bold",
                                           borderwidth=6, command=self.invoice_create)
        self.create_inovice_button.place(x=310, y=380)

        self.gst_incl_excl = StringVar()
        self.gst_incl_excl.set("Is GST Included or Excluded")
        gst_options = ["GST Included", "GST Excluded"]
        self.gst_dropdown_menu = OptionMenu(
            root, self.gst_incl_excl, *gst_options)

    def gst_dropdown(self):
        """Displays the GST included/excluded menu"""
        self.gst_dropped_down = True
        self.gst_dropdown_menu.place(x=8, y=150)

    def destroy_gstdropdown(self):
        """Destroys the GST included/excluded dropdown 
        menu if the user selects Yes, then switches to NO"""
        if self.gst_dropped_down is True:
            self.gst_dropdown_menu.place_forget()
            self.gst_dropped_down = False

    def newline(self):
        """Displays a new line in the GUI"""
        if self.num == 0:
            self.desc_entry_box1.place(x=8, y=290)
            self.quantity_entry_box1.place(x=550, y=290)
            self.price_entry_box1.place(x=675, y=290)
            self.num += 1

        elif self.num == 1:
            self.desc_entry_box2.place(x=8, y=315)
            self.quantity_entry_box2.place(x=550, y=315)
            self.price_entry_box2.place(x=675, y=315)
            self.num += 1

        elif self.num == 2:
            self.desc_entry_box3.place(x=8, y=340)
            self.quantity_entry_box3.place(x=550, y=340)
            self.price_entry_box3.place(x=675, y=340)
            self.num += 1

        elif self.num == 3:
            self.num += 1
            self.max_line_error.place(x=8, y=420)

    def remove_line(self):
        """Removes the line in the GUI"""
        if self.num == 1:
            self.desc_entry_box1.place_forget()
            self.quantity_entry_box1.place_forget()
            self.price_entry_box1.place_forget()
            self.num -= 1

        elif self.num == 2:
            self.desc_entry_box2.place_forget()
            self.quantity_entry_box2.place_forget()
            self.price_entry_box2.place_forget()
            self.num -= 1

        elif self.num == 3:
            self.desc_entry_box3.place_forget()
            self.quantity_entry_box3.place_forget()
            self.price_entry_box3.place_forget()
            self.num -= 1

        elif self.num >= 4:
            self.desc_entry_box3.place_forget()
            self.quantity_entry_box3.place_forget()
            self.price_entry_box3.place_forget()
            self.num = 2
            self.max_line_error.place_forget()
            self.max_line_error.place_forget()

    def invoice_create(self):
        """Starts the invoice creation process"""
        self.error_check_num = 0
        self.invoice_line_check = 0
        #Checking for errors
        self.invoice_create_error_check(self.desc_entry_box.get(
        ), self.quantity_entry_box.get(), self.price_entry_box.get())
        self.invoice_create_error_check(self.desc_entry_box1.get(
        ), self.quantity_entry_box1.get(), self.price_entry_box1.get())
        self.invoice_create_error_check(self.desc_entry_box2.get(
        ), self.quantity_entry_box2.get(), self.price_entry_box2.get())
        self.invoice_create_error_check(self.desc_entry_box3.get(
        ), self.quantity_entry_box3.get(), self.price_entry_box3.get())
        if str(self.select_job.get()) == "Select Job to create invoice for:":
            messagebox.showerror(
                "An error occured", "Please select a job to create the "
                "invoice for. If there is no job, please create one")
            self.error_check_num += 1

        if self.gst_num.get() == 3:
            messagebox.showerror(
                "An error occured", "Please select whether you charge GST or do not")
            self.error_check_num += 1

        if self.gst_dropped_down is True:
            if str(self.gst_incl_excl.get()) == "Is GST Included or Excluded":
                messagebox.showerror(
                    "An error occured", "Please select whether GST "
                    "is included in the price or excluded")
                self.error_check_num += 1

        if self.invoice_line_check == 4:
            messagebox.showerror(
                "An error occured", "Please write down atleast 1 line for your invoice")

        if self.error_check_num == 0:
            lines = []
            self.line_check(self.desc_entry_box.get(), self.quantity_entry_box.get(),
                            self.price_entry_box.get(), lines)
            self.line_check(self.desc_entry_box1.get(), self.quantity_entry_box1.get(),
                             self.price_entry_box1.get(), lines)
            self.line_check(self.desc_entry_box2.get(), self.quantity_entry_box2.get(),
                            self.price_entry_box2.get(), lines)
            self.line_check(self.desc_entry_box3.get(), self.quantity_entry_box3.get(),
                            self.price_entry_box3.get(), lines)

            #Getting the information about the job
            with open("jobs.json", "r", encoding="UTF-8") as jobs_filed:
                all_jobs = json.load(jobs_filed)
                for job in all_jobs:
                    if job[0] == self.username:
                        if int(job[1]) == int(self.select_job.get()[1]):
                            name = job[2]
                            address = job[5]
                            phone_number = job[4]
                            email = job[3]

            current_date_time = datetime.datetime.now()

            formatted_date = current_date_time.strftime("%d / %m / %Y")

            subtotal = sum(line["quantity"] * line["unit_price"] for line in lines)

            gst = sum(line["GST"] for line in lines)

            total = sum(line["total"] for line in lines)

            pdf_file = filedialog.asksaveasfilename(defaultextension=".pdf",
                                                    filetypes=[("PDF files", "*.pdf")],
                                                    initialfile =
                                                    f"invoice{self.select_job.get()[1]}")

            doc = SimpleDocTemplate(pdf_file, pagesize=letter)

            pdf_text = []

            styles = getSampleStyleSheet()

            #Building the PDF file
            header = Paragraph("Invoice", styles['Heading1'])
            pdf_text.append(header)
            right_align = styles['Heading5']
            right_align.alignment = 2
            datetext = Paragraph(f"Date: {formatted_date}", right_align)
            pdf_text.append(datetext)
            pdf_text.append(Paragraph(f"Job Number: {int(self.select_job.get()[1])}", right_align))
            pdf_text.append(Paragraph("Invoice Billed to:", styles['Heading4']))
            pdf_text.append(Paragraph(f"Name: {name}", styles['Normal']))
            pdf_text.append(Paragraph(f"Address: {address}", styles['Normal']))
            pdf_text.append(Paragraph(f"Phone: {phone_number}", styles['Normal']))
            pdf_text.append(Paragraph(f"Email: {email}", styles['Normal']))

            spacer = Spacer(1, 40)
            pdf_text.append(spacer)

            data = [["Description", "Quantity", "Unit Price", "GST", "Total"]]
            for line in lines:
                data.append([line["description"], line["quantity"], f'${line["unit_price"]:.2f}',
                             f'${line["GST"]:.2f}', f'${line["total"]:.2f}'])

            table = Table(data, colWidths=[4*inch, 1 *
                        inch, 1*inch, 1*inch, 1.5*inch])
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))

            pdf_text.append(table)
            pdf_text.append(spacer)
            pdf_text.append(
                Paragraph(f"Subtotal: ${subtotal:.2f}", styles['Heading4']))
            pdf_text.append(Paragraph(f"GST: ${gst:.2f}", styles['Heading4']))
            pdf_text.append(Paragraph(f"Total: ${total:.2f}", styles['Heading2']))

            if pdf_file:
                doc.build(pdf_text)
                with open("jobs.json", "r", encoding="UTF-8") as filed_jobs:
                    all_jobs = json.load(filed_jobs)
                    for job in all_jobs:
                        if job[0] == self.username:
                            if int(job[1]) == int(self.select_job.get()[1]):
                                test123 = all_jobs.index(job)
                                all_jobs.pop(test123)

                with open("jobs.json", "w", encoding="UTF-8") as job_file:
                    json.dump(all_jobs, job_file)

                self.main_menu_return_passthrough()

    def invoice_create_error_check(self, desc, quantity, price):
        """Checks for errors in the invoices creation"""
        if (desc or quantity or price) and not (desc and quantity and price):
            messagebox.showerror(
                "An error occured", f"Please enter inputs in all 3 entryboxes (Description, "
                F"Quantity, and Price) for each line you write. \n\nLine that caused the Error: \n" 
                f"Description: {desc} \nQuantity: {quantity} \nPrice: {price}")
            self.error_check_num += 1

        if desc and quantity and price == "":
            self.invoice_line_check += 1

        if quantity == "":
            pass

        else:
            try:
                if float(quantity) < 0:
                    messagebox.showerror("An error occured", "Quantity cannot be "
                                         "negative and must be positive")
                    self.error_check_num += 1
                else:
                    float(quantity)

            except ValueError:
                messagebox.showerror(
                    "An error occured", "Please make sure that "
                    "the quantity is a number and contains no other characters")
                self.error_check_num += 1

        if price == "":
            pass

        else:
            try:
                if len(price) == 1:
                    if price.isnumeric():
                        pass
                    else:
                        messagebox.showerror(
                        "An error occured", "Please make sure that the price is a"
                        "number and contains no other characters other "
                        "than $ symbol. The price cannot be negative")
                else:
                    float(price[1:])
                    if price[0] == "$":
                        pass
                    elif price[0].isnumeric():
                        pass

                    else:
                        messagebox.showerror(
                            "An error occured", "Please make sure that the price is" 
                            "a number and contains no other characters other than $ symbol")
                        self.error_check_num += 1

            except ValueError:
                messagebox.showerror(
                    "An error occured", "Please make sure that the " 
                    "price is a number and contains no other characters other than $ sym")
                self.error_check_num += 1

        if len(desc) > 200:
            messagebox.showerror(
                "An error occured", "Too many characters in" 
                "Description, please shorten it to 200 or under")
            self.error_check_num += 1

        if len(quantity) > 8:
            messagebox.showerror(
                "An error occured", "Too many characters" 
                "in quantity, please shorten it to 8 or under")
            self.error_check_num += 1

        if len(price) > 12:
            messagebox.showerror(
                "An error occured", "Too many characters in" 
                "Price, please shorten it to 12 or under")
            self.error_check_num += 1


    def line_check(self, desc, quantity, price, lines):
        """Checks the lines of the invoice to make the numbers right"""
        if desc == "":
            pass
        else:
            fquantity = float(quantity)
            fprice = float(price)
            total1 = fquantity * fprice

            gst = 0
            if self.gst_num.get() == 1:
                if self.gst_incl_excl.get() == "GST Excluded":
                    gst = total1 * .15
                    total = total1 + gst
                else:
                    gst = total1 - (total1/1.15)
                    total = total1
            else:
                gst = 0
                total = total1

            linedict = {"description": desc, "quantity": float(quantity),
            "unit_price": float(price), "GST": float(gst), "total": float(total)}
            lines.append(linedict)
            return lines

    def main_menu_return_passthrough(self):
        """Function destroys everything in create invoice and then runs MainMenu"""
        self.main_menu_return.destroy()
        self.quantity_entry_box.destroy()
        self.quantity_entry_box1.destroy()
        self.quantity_entry_box2.destroy()
        self.quantity_entry_box3.destroy()
        self.desc_entry_box.destroy()
        self.desc_entry_box1.destroy()
        self.desc_entry_box2.destroy()
        self.desc_entry_box3.destroy()
        self.price_entry_box.destroy()
        self.price_entry_box1.destroy()
        self.price_entry_box2.destroy()
        self.price_entry_box3.destroy()
        self.desc_label.destroy()
        self.quantity_label.destroy()
        self.price_label.destroy()
        self.create_inovice_button.destroy()
        self.invoice_creation_text.destroy()
        self.gst_txt.destroy()
        self.gst_button1.destroy()
        self.gst_button2.destroy()
        self.spacer2.destroy()
        self.jobs_entry.destroy()
        self.add_new_line.destroy()
        self.remove_line_btn.destroy()


        if self.gst_dropped_down is True:
            self.gst_dropdown_menu.destroy()

        if self.num >= 4:
            self.max_line_error.destroy()

        MainMenu(root, self.username)

#What needs to run when the program gets ran
def main():
    """Function Runs the program"""
    Login(root)
    root.mainloop()

#Runs the program
if __name__ == '__main__':
    main()
