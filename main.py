from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

# Create a PDF receipt function
def create_receipt(file_name, customer_name, payment_date, amount_paid, payment_method):
    doc = SimpleDocTemplate(file_name, pagesize=letter)
    styles = getSampleStyleSheet()

    # Define a custom paragraph style for the receipt
    receipt_style = ParagraphStyle(
        "receipt",
        parent=styles["Normal"],
        fontSize=20,
        textColor=colors.grey,
        alignment=1,  # Center alignment
        spaceAfter=55,  # Space after each paragraph
    )

    # Create a custom title style
    title_style = ParagraphStyle(
        "title",
        parent=styles["Title"],
        fontSize=55,
        textColor=colors.black,
        alignment=1,  # Center alignment
        spaceAfter=150,  # Space after the title
    )

    story = []

    # Title with underline
    title_text = "<u>Payment Receipt</u>"
    title = Paragraph(title_text, title_style)
    story.append(title)

    # Customer Name
    customer_paragraph = Paragraph(f"Customer Name: {customer_name}", receipt_style)
    story.append(customer_paragraph)

    # Payment Date
    date_paragraph = Paragraph(f"Payment Date: {payment_date}", receipt_style)
    story.append(date_paragraph)

    # Amount Paid
    amount_paragraph = Paragraph(f"Amount Paid: ${amount_paid:.2f}", receipt_style)
    story.append(amount_paragraph)

    # Payment Method
    method_paragraph = Paragraph(f"Payment Method: {payment_method}", receipt_style)
    story.append(method_paragraph)

    doc.build(story)

# Example usage:
file_name = "payment_receipt.pdf"
customer_name = "John Doe"
payment_date = "2023-10-05"
amount_paid = 100.0
payment_method = "Credit Card"

create_receipt(file_name, customer_name, payment_date, amount_paid, payment_method)
