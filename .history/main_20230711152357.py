from PyPDF2 import PdfWriter, PdfReader
import io
from reportlab.pdfgen import canvas

writer = PdfReader()

existing_pdf = PdfReader('County Stickers.pdf')

page1 = existing_pdf[0]

writer.add_blank_pagge(210, 297)

writer.add_page(page)



