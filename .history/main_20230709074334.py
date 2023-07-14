from PyPDF2 import PdfWriter, PdfReader
import io
from reportlab.pdfgen import canvas

existing_pdf = PdfReader('County Stickers.pdf')

print(dir(existing_pdf))

print(existing_pdf.pages)

