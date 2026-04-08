import PyPDF2

print("RUNNING PDF 1")

pdf_file = open("ux1.pdf", "rb")   # first PDF
reader = PyPDF2.PdfReader(pdf_file)

pdf_text = ""

for page in reader.pages:
    text = page.extract_text()
    if text:
        pdf_text += text

print("Length:", len(pdf_text))
print(pdf_text[:500])