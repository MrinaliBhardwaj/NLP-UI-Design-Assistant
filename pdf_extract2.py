import PyPDF2

print("RUNNING PDF 2")

pdf_file = open("ux2.pdf", "rb")   # second PDF
reader = PyPDF2.PdfReader(pdf_file)

pdf_text2 = ""

for page in reader.pages:
    text = page.extract_text()
    if text:
        pdf_text2 += text

print("Length:", len(pdf_text2))
print(pdf_text2[:500])