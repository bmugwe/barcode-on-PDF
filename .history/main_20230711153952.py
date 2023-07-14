from PyPDF2 import PdfWriter, PdfReader
import io
from reportlab.pdfgen import canvas

import pandas as pd

barcode_list = pd.read_excel('Bar codes.xlsx', sheet_name='unpivot')

print(barcode_list)

def create_pdf():
    writer = PdfWriter()

    existing_pdf = PdfReader('County Stickers.pdf')

    page1 = existing_pdf.pages[0]

    width = page1.mediabox.width
    height = page1.mediabox.height
    print(f'height: {height}, width: {width}, No. of Pages: {len(existing_pdf.pages)}')

    # writer.add_blank_page(210, 297)

    writer.add_page(page1)

    with open('test.pdf', 'wb') as file:
        writer.write(file)


if __name__ == '__main__':
    create_pdf()

