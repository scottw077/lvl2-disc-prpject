from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.units import inch


def create_invoice(job_number, client_name, client_address, client_phone, date, items, subtotal, total, pdf_file, gst):
    doc = SimpleDocTemplate(pdf_file, pagesize=letter)

    # Create a list to hold the invoice elements
    elements = []

    # Styles for the invoice
    styles = getSampleStyleSheet()

    # Invoice header
    header = Paragraph("Invoice", styles['Heading1'])
    elements.append(header)
    elements.append(
        Paragraph("Job Number: {}".format(job_number), styles['Normal']))
    elements.append(Paragraph("Date: {}".format(date), styles['Normal']))
    elements.append(
        Paragraph("Client Name: {}".format(client_name), styles['Normal']))
    elements.append(Paragraph("Client Address: {}".format(
        client_address), styles['Normal']))
    elements.append(Paragraph("Client Phone: {}".format(
        client_phone), styles['Normal']))

    # Itemized list
    data = [["Description", "Quantity", "Unit Price", "GST", "Total"]]
    for item in items:
        data.append([item["description"], item["quantity"],
                    '${:.2f}'.format(item["unit_price"]), '${:.2f}'.format(item["GST"]), '${:.2f}'.format(item["total"])])

    # Create a table for the itemized list
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

    elements.append(table)

    # Subtotal and Total
    elements.append(
        Paragraph("Subtotal: ${:.2f}".format(subtotal), styles['Heading4']))
    elements.append(Paragraph("GST: ${:.2f}".format(gst), styles['Heading4']))

    elements.append(
        Paragraph("Total: ${:.2f}".format(total), styles['Heading2']))

    # Build the PDF
    doc.build(elements)


if __name__ == "__main__":
    job_number = "12345"
    client_name = "John Doe"
    client_address = "123 Main Street"
    client_phone = "555-555-5555"
    date = "2023-09-05"
    items = [
        {"description": "Description 1", "quantity": 2,
            "unit_price": 50.00, "GST": 15.00, "total": 115.00},
        {"description": "Description 2", "quantity": 3,
            "unit_price": 30.00, "GST": 13.50, "total": 103.50}
    ]
    subtotal = sum(item["quantity"] * item["unit_price"] for item in items)

    gst = sum(item["GST"] for item in items)

    total = sum(item["total"] for item in items)

    pdf_file = "invoice_with_items5.pdf"

    create_invoice(job_number, client_name, client_address,
                   client_phone, date, items, subtotal, total, pdf_file, gst)
