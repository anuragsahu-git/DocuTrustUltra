from pypdf import PdfReader

reader = PdfReader("data/uploads/ANNEXURE_VII_A.pdf")

print("Pages:", len(reader.pages))
print()

text = reader.pages[0].extract_text()

print(repr(text))