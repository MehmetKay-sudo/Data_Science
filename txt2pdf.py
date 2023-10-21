from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def txt_to_pdf(txt_path, pdf_path):
    c = canvas.Canvas(pdf_path, pagesize=letter)

    with open(txt_path, 'r', encoding='utf-8') as txt_file:
        text = txt_file.read()

    # Define the font and size for the text
    c.setFont("Helvetica", 12)

    # Split the text into lines to fit on the page
    lines = text.split('\n')

    # Start writing the text to the PDF
    for line in lines:
        c.drawString(100, 700, line)
        c.showPage()

    c.save()
    print("TXT converted to PDF successfully!")

# Specify the path to your TXT file
txt_path = 'path/to/input.txt'

# Specify the path to save the PDF file
pdf_path = 'path/to/output.pdf'

# Call the function to convert TXT to PDF
txt_to_pdf(txt_path, pdf_path)
