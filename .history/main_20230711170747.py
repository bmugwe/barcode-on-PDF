from PyPDF2 import PdfWriter, PdfReader
import io
from reportlab.pdfgen import canvas
import pandas as pd
from barcode import EAN13, EAN8
from barcode.writer import ImageWriter

from reportlab.pdfgen import canvas
from io import StringIO

from fpdf import FPDF

pdf = FPDF()
pdf.add_page("P", "mm", [99, 226))
pdf.interleaved2of5("4707001", x=50, y=50, w=4, h=20)
pdf.output("interleaved2of5.pdf")

# barcode_list = pd.read_excel('Bar codes.xlsx', sheet_name='unpivot')
# unique_countys = barcode_list['county'].unique()
# file = StringIO()
# def genImage(number):
#     file = EAN8(number, writer=ImageWriter())
#     return file

# face = genImage('4707001')

# print(dir(face))





# def create_pdf():
#     writer = PdfWriter()

#     existing_pdf = PdfReader('County Stickers.pdf')

#     page1 = existing_pdf.pages[0]

#     width = page1.mediabox.width
#     height = page1.mediabox.height
#     print(f'height: {height}, width: {width}, No. of Pages: {len(existing_pdf.pages)}')

#     # writer.add_blank_page(210, 297)

#     writer.add_page(page1)

#     with open('test.pdf', 'wb') as file:
#         writer.write(file)


# if __name__ == '__main__':
#     create_pdf()
#     pass

