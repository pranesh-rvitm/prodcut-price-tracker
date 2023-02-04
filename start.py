
from amazon_tracker import *
import PyPDF2
from amazon_tracker import *
import fpdf
a=tracker("welcome ");

pdf= fpdf.FPDF()
a = tracker("welcome");
pdf= fpdf.FPDF()
pdf.add_page()
pdf.set_font("Arial", size =10)
pdf.cell(200,10, txt ="hey this is the pdf that stores our output : ", ln = 1)
a.check_price("www.amazon.com")
pdf.output("output.pdf")

input_file = open("output.pdf", 'rb')
input_pdf = PyPDF2.PdfReader(input_file)
watermark_file = open("watermark.pdf", 'rb')
watermark_pdf = PyPDF2.PdfReader(watermark_file)

pdf_page = input_pdf.pages[0]
watermark_page = watermark_pdf.pages[0]
pdf_page.merge_page(watermark_page)

out = PyPDF2.PdfWriter()
out.add_page(pdf_page)

merged_file = open("final_output.pdf", 'wb')
out.write(merged_file)

merged_file.close()
watermark_file.close()
input_file.close()
