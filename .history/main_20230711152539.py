from PyPDF2 import PdfWriter, PdfReader
import io
from reportlab.pdfgen import canvas

def create_pdf(filepath):

writer = PdfReader()

existing_pdf = PdfReader('County Stickers.pdf')

page1 = existing_pdf[0]

writer.add_blank_pagge(210, 297)

writer.add_page(page1)

with open('test.pdf', 'wb') as file:
    writer.write(file)




