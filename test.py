from tkinter import *
from tkinter import ttk

def invoice_create(desc, amount, price):
    if (desc or amount or price) and not (desc and amount and price):
        print("test", desc + amount)

invoice_create("", "", "")
invoice_create("dd", "", "")
invoice_create("dd", "a", "")
invoice_create("asd", "asdas", "asda")