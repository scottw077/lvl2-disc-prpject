from tkinter import *
from tkinter import ttk
import aspose.pdf as ap
document = ap.Document()

# Add page
page = document.pages.add()

# Initialize textfragment object
text_fragment = ap.text.TextFragment("Hello,world!")
title = ap.text.TextFragment("test")

# Add text fragment to new page
page.title.add(title)
page.paragraphs.add(text_fragment)

# Save updated PDF
document.save("output.pdf")
