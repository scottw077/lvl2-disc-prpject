from tkinter import *
from tkinter import messagebox
import json
root = Tk()
root.title("Electrical Job Management Software")
root.iconbitmap("ElecTRICIAN JOB MANAGEMENT SOFTWARE (2).ico")
root.geometry("800x450")
root.configure(bg="#5b5b5c")
root.columnconfigure(3, weight=1)

class signup:
    def __init__(self,master):
        self.root = master
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

        self.pwdtxt = Label(root, text="Create a Password", font=(
            "Arial 12 bold"), fg="white", bg="#5b5b5c")
        self.pwdtxt.grid(row=4, column=3)
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


        def signup_process(self,username, pwd, confirmpwd):
        
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

class login:
    def __init__(self,master):
        self.root = master
        logintxt = Label(root, text="Login", font=(
            "Impact 80"), fg="white", bg="#5b5b5c")
        logintxt.grid(row=0, column=3)

        usertxt = Label(root, text="Username:", font=(
            "Arial 12 bold"), fg="white", bg="#5b5b5c")
        usertxt.grid(row=1, column=3)
        
        global user_entry

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
                    main_menu(username)
                else:
                    messagebox.showerror("An error occured", "Username or Password is incorrect, please try again")
            else:
                messagebox.showerror("An error occured", "Username or Password is incorrect, please try again")


class main_menu:
    def __init__(self, master):
        self.root = master
        self.spacer1 = Label(root, text="", bg="#5b5b5c")
        self.spacer1.grid(row=0, column=3)
        
        self.add_job_btn = Button(root, text="Add Job", padx=30, pady=10, font=("Arial 18 bold"), borderwidth=6, command=self.add_job_command)
        self.add_job_btn.grid(row=1, column=3)

        self.staff_tracker_btn = Button(root, text="Staff Tracker", padx=30, pady=10, font=("Arial 18 bold"), borderwidth=6)
        self.staff_tracker_btn.grid(row=1, column=2)
    
    def add_job_command(self):
        self.spacer1.destroy()
        self.add_job_btn.destroy()
        self.staff_tracker_btn.destroy()
        add_job(self.root)


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

        next_btn = Button(frame, text="Next", padx=30, pady=10, font=("Arial 12 bold"), command=lambda: add_job2(self, name_entry.get(), email_entry.get(), phnenum_entry.get(), address_entry.get(), frame))
        next_btn.grid(row=14, column=3)



        def add_job2(self, name, email, phnenum, address, frame):
            if "@" not in email or "." not in email:
                messagebox.showerror("An error occured", "Email Address is not valid, please try again")
            
            elif phnenum.isalpha():
                messagebox.showerror("An error occured", "Phone number cannot contain letters")

            elif name == "":
                messagebox.showinfo("Entry Box Empty!", "Empty Client's Name Box! Please enter the client's name")
            
            elif phnenum == "":
                messagebox.showinfo("Entry Box Empty!", "Empty Client's Phone Number Box! Please enter the client's phone number")
            
            elif address == "":
                messagebox.showinfo("Entry Box Empty!", "Empty Client's Address Box! Please enter the client's address")
            
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


                jobstatus_txt = Label(frame1, text="Job Status", font=("Arial 16 bold"), fg="white", bg="#5b5b5c")
                jobstatus_txt.grid(row=5, column=3)
                jobstatus_default = StringVar()
                jobstatus_default.set("Select Job Status")
                job_statuses = ["started", "half-way through", "finished"]
                jobstatus_entry = OptionMenu(frame1, jobstatus_default, *job_statuses)
                jobstatus_entry.grid(row=6, column=3)

                spacer2 = Label(frame1, text="", bg="#5b5b5c")
                spacer2.grid(row=7, column=3)

                staff_txt = Label(frame1, text="Staff", font=("Arial 16 bold"), fg="white", bg="#5b5b5c")
                staff_txt.grid(row=8, column=3)
                staff_default = StringVar()
                staff_default.set("Select Staff")
                staff = ["sdfs", "sdfsdf"]
                staff_entry = OptionMenu(frame1, staff_default, *staff)
                staff_entry.grid(row=9, column=3)

                spacer3 = Label(frame1, text="", bg="#5b5b5c")
                spacer3.grid(row=10, column=3)

                add_job_btn = Button(frame1, text="Add New Job", padx=22, pady=10, font=("Arial 12 bold"), command= lambda: add_job_process(name, email, phnenum, address, jobtype_default.get(), jobstatus_default.get(), staff_default.get(), frame1))
                add_job_btn.grid(row=11, column=3)

        def add_job_process(name, email, phnenum, address, job_type, job_status, staff, frame):
            new_job = [name, email, phnenum, address, job_type, job_status, staff]
            print(new_job)
            with open("jobs.json", "r") as h:
                existing_jobs = json.load(h)

            existing_jobs.append(new_job)
            
            with open("jobs.json", "w") as j:
                json.dump(existing_jobs, j)
            messagebox.showinfo("Success!", "Sucessfully Added Job!")
            frame.grid_forget()
            main_menu(root)




def main():
    main_menu(root)
    root.mainloop()

if __name__ == '__main__':
    main()