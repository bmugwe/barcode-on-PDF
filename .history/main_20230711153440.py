from PyPDF2 import PdfWriter, PdfReader
import io
from reportlab.pdfgen import canvas

import pandas as pd

barcode_list = pd.read_excel('Bar codes.xlsx', sheet_name='')

def create_pdf():
    writer = PdfWriter()

    existing_pdf = PdfReader('County Stickers.pdf')

    page1 = existing_pdf.pages[0]

    print(dir(page1))

    # writer.add_blank_page(210, 297)

    writer.add_page(page1)

    with open('test.pdf', 'wb') as file:
        writer.write(file)


if __name__ == '__main__':
    create_pdf()

