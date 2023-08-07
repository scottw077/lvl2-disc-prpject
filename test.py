from tkinter import *
from tkinter import ttk
import bcrypt

# example password
password = "password123"
bytes = password.encode("utf-8")
salt = bcrypt.gensalt()
hash = bcrypt.hashpw(bytes, salt)
