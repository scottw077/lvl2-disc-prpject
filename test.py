import tkinter as tk
from tkinter import ttk

# Create a dictionary with staff names as keys and tasks as values
staff_tasks = {
    "John": ["Task 1", "Task 2", "Task 3"],
    "Alice": ["Task 2", "Task 4", "Task 5"],
    "Bob": ["Task 1", "Task 3", "Task 6"],
    "Eve": ["Task 4", "Task 5", "Task 6"],
}

# Create the main window
root = tk.Tk()
root.title("Staff Tasks Table")

# Create a Canvas widget
canvas = tk.Canvas(root)
canvas.pack()

# Create a frame inside the Canvas
frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor="nw")

# Create a table by placing labels
for col, staff in enumerate(staff_tasks.keys()):
    tk.Label(frame, text=staff, relief="ridge", width=15).grid(row=0, column=col+1, sticky="nsew")
    for row, task in enumerate(staff_tasks[staff]):
        tk.Label(frame, text=task, relief="ridge", width=15).grid(row=row+1, column=col+1, sticky="nsew")

# Configure row and column weights to allow resizing
for i in range(len(staff_tasks) + 1):
    frame.grid_rowconfigure(i, weight=1)
for i in range(len(staff_tasks[staff]) + 1):
    frame.grid_columnconfigure(i, weight=1)

# Add a vertical scrollbar
vsb = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
vsb.pack(side="right", fill="y")
canvas.configure(yscrollcommand=vsb.set)

# Add a horizontal scrollbar
hsb = ttk.Scrollbar(root, orient="horizontal", command=canvas.xview)
hsb.pack(side="bottom", fill="x")
canvas.configure(xscrollcommand=hsb.set)

# Bind the Canvas to the frame
frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

# Run the main loop
root.mainloop()




# from reportlab.lib.pagesizes import letter
# from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
# from reportlab.lib.styles import getSampleStyleSheet
# from reportlab.lib import colors
# from reportlab.lib.units import inch


# def create_invoice(job_number, client_name, client_address, client_phone, email, date, items, subtotal, total, pdf_file, gst):
#     doc = SimpleDocTemplate(pdf_file, pagesize=letter)

#     # Create a list to hold the invoice elements
#     elements = []

#     # Styles for the invoice
#     styles = getSampleStyleSheet()

#     # Invoice header
#     header = Paragraph("Invoice", styles['Heading1'])
#     elements.append(header)
#     test234 = styles['Heading5']
#     test234.alignment = 2
#     test123 = Paragraph("Date: {}".format(date), test234)
#     elements.append(test123)
#     elements.append(
#         Paragraph("Job Number: {}".format(job_number), test234))
    
#     elements.append(Paragraph("Invoice Billed to:", styles['Heading4']))
#     elements.append(
#         Paragraph("Name: {}".format(client_name), styles['Normal']))
#     elements.append(Paragraph("Address: {}".format(
#         client_address), styles['Normal']))
#     elements.append(Paragraph("Phone: {}".format(
#         client_phone), styles['Normal']))
#     elements.append(Paragraph("Email: {}".format(
#         email), styles['Normal']))

#     # Itemized list
#     spacer = Spacer(1, 40)
#     elements.append(spacer)
    
#     data = [["Description", "Quantity", "Unit Price", "GST", "Total"]]
#     for item in items:
#         data.append([item["description"], item["quantity"],
#                     '${:.2f}'.format(item["unit_price"]), '${:.2f}'.format(item["GST"]), '${:.2f}'.format(item["total"])])

#     # Create a table for the itemized list
#     table = Table(data, colWidths=[4*inch, 1 *
#                   inch, 1*inch, 1*inch, 1.5*inch])
#     table.setStyle(TableStyle([
#         ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
#         ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
#         ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
#         ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
#         ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
#         ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
#         ('GRID', (0, 0), (-1, -1), 1, colors.black)
#     ]))

#     elements.append(table)

#     # Subtotal and Total
#     elements.append(spacer)
    
#     elements.append(
#         Paragraph("Subtotal: ${:.2f}".format(subtotal), styles['Heading4']))
#     elements.append(Paragraph("GST: ${:.2f}".format(gst), styles['Heading4']))

#     elements.append(
#         Paragraph("Total: ${:.2f}".format(total), styles['Heading2']))

#     # Build the PDF
#     doc.build(elements)


# if __name__ == "__main__":
#     job_number = "12345"
#     client_name = "John Doe"
#     client_address = "123 Main Street"
#     client_phone = "555-555-5555"
#     email = "test@gmail.com"
#     date = "2023-09-05"
#     items = [ 
#         {"description": "Description 1", "quantity": 2,
#             "unit_price": 50.00, "GST": 15.00, "total": 115.00},
#         {"description": "Description 2", "quantity": 3,
#             "unit_price": 30.00, "GST": 13.50, "total": 103.50}
#     ]
#     subtotal = sum(item["quantity"] * item["unit_price"] for item in items)

#     gst = sum(item["GST"] for item in items)

#     total = sum(item["total"] for item in items)

#     pdf_file = "invoice_with_items7.pdf"

#     create_invoice(job_number, client_name, client_address,
#                    client_phone, email, date, items, subtotal, total, pdf_file, gst)
