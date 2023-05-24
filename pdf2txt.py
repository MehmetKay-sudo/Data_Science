import PyPDF2

def pdf_to_txt(pdf_path, txt_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        num_pages = len(pdf_reader.pages)

        with open(txt_path, 'w') as txt_file:
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                txt_file.write(text)

    print("PDF converted to TXT successfully!")

# Specify the path to your PDF file
pdf_path = 'path/to/input.pdf'

# Specify the path to save the TXT file
txt_path = 'path/to/output.txt'

# Call the function to convert PDF to TXT
pdf_to_txt(pdf_path, txt_path)
