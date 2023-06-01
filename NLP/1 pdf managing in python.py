# Read a PDF File and Print its First Page.
# Required Command/library
# >>> pip install pypdf2


from PyPDF2 import PdfReader
from PyPDF2 import PdfWriter

pdffile = PdfReader("Sample.pdf")
pagecount = len(pdffile.pages)

print(f"\nPdf Page Length - {pagecount}")

page1 = pdffile.pages[0]
text1 = page1.extract_text()
print("\nText Contents Of Page 1 >>\n")

print(text1)

print('\nSaving As "Result.pdf" ')
pdfresult = page1
