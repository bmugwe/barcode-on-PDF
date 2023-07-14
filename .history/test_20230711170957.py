from fpdf import FPDF

pdf = FPDF()
pdf.set_font("Helvetica")
# pdf.set_page_background((252,212,255))
for i in range(9):
    # if i == 6:
        # pdf.set_page_background('new_code.png')
    pdf.add_page(format=(210 * (1 - i/10), 297 * (1 - i/10)))
    pdf.cell(txt=str(i))
# pdf.set_page_background(None)
pdf.add_page(same=True)
pdf.cell(txt="9")
pdf.output("varying_format.pdf")