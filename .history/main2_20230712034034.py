from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader

def add_image_to_pdf(pdf_path, image_path, output_path):
    # Open the existing PDF file
    pdf = PdfReader(open(pdf_path, 'rb'))
    
    # Create a new PDF canvas
    c = canvas.Canvas(output_path, pagesize=letter)
    
    # Load the image
    img = ImageReader(image_path)
    
    # Get the dimensions of the first page in the PDF
    page = pdf.pages[(0)
    width, height = page.mediaBox.getWidth(), page.mediaBox.getHeight()
    
    # Set the image position and size
    c.drawImage(img, 0, 0, width, height)
    
    # Save the canvas as a new PDF file
    c.save()
    
    # Merge the new PDF file with the existing one
    output_pdf = PdfWriter()
    image_pdf = PdfReader(open(output_path, 'rb'))
    
    # Add the existing PDF content
    for page_num in range(pdf.getNumPages()):
        output_pdf.addPage(pdf.pages[page_num])
    
    # Add the image PDF content
    for page_num in range(image_pdf.getNumPages()):
        output_pdf.addPage(image_pdf.pages[page_num])
    
    # Save the final PDF
    with open(output_path, 'wb') as output_file:
        output_pdf.write(output_file)

# Example usage
pdf_path = 'test.pdf'  # Path to the existing PDF file
image_path = 'new_code.png'   # Path to the image file
output_path = 'output.pdf' # Path to the output PDF file

add_image_to_pdf(pdf_path, image_path, output_path)
