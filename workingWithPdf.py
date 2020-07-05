# Opening a PDF

from PyPDF2 import PdfFileReader
from pathlib import Path 

pdf_path = (
	Path.home()
	/"testpdf.pdf")

# Create the PdfFileReader instance

pdf = PdfFileReader(str(pdf_path))
print(pdf.getNumPages())
print(pdf.documentInfo)
print(pdf.documentInfo.creator)

"""
Extracting text from a page

1. Get a PageObject with PdfFileReader.getPage().
2. Extract the text as string with PageObject instance's.extractText().

"""

# Accessing the first page

first_page = pdf.getPage(0)
print(first_page)

extracted_content = first_page.extractText()
print(extracted_content)




# Putting all together and saving the extracted text from the pdf to a .txt file

pdf_reader = PdfFileReader(str(pdf_path))
output_file_path = Path.home() / "test.txt"
with output_file_path.open(mode="w") as output_file:
	title = pdf_reader.documentInfo.title
	num_pages = pdf_reader.getNumPages
	output_file.write(f"{title} \\n Number of pages: {num_pages} \\n\\n")

	for page in pdf_reader.pages:
		text = page.extractText()
		output_file.write(text)

"""
1. Here we assign a new PdfFileReader instance to the pdf_reader variable.Also a Path object to .txt file and assign it to out_file_path variable.
2. Next we open our output_file_path in write mode and assign the file object returned by .open() to the variable output_file.
3. We uses a with block and inside the with block, you write the PDF title and number of pages to the text file using output_file.write().
4. A final for loop to iterate over all the pages in the PDF and text from each page is extracted using .extractText() and is written to the output_file.
"""



# Creating a new pdf using PdfFileWriter class
from PyPDF2 import PdfFileWriter
pdf_writer = PdfFileWriter()

# Adding a blank page
page = pdf_writer.addBlankPage(width=72, height=72)

# Write the contents of pdf_writer to a pdf file
from pathlib import Path
with Path("newtest.pdf").open(mode="wb") as output_file:
	pdf_writer.write(output_file)

# Extracting Single page from a pdf
from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_path = (
	Path.home()
	/"testpdf.pdf"
	)
input_pdf = PdfFileReader(str(pdf_path))
first_page = input_pdf.getPage(0)

pdf_writer = PdfFileWriter()
pdf_writer.addPage(first_page)

with Path("first.pdf").open(mode="wb") as output_file:
	pdf_writer.write(output_file)


# Try to extract multiple pages and save it into new pdf

for i in range(1, 10):
	page = input_pdf.getPage(i)
	pdf_writer.addPage(page)

with Path("multiple.pdf").open(mode="wb") as output_file:
	pdf_writer.write(output_file)


# We can also use slice notation instead of using range
# for page in input_pdf.pages[1:10]:
#	pdf_writer.addPage(page)


# Concatenate and Merging PDFs
from PyPDF2 import PdfFileMerger
pdf_merger = PdfFileMerger()

"""
Couple of ways to add pages to the pdf_merger
1. .append() - concatenate to the end of the pages currently in the PdfFileMerger
2. .merge() - allow to insert at a specific page
"""

reports_dir = (
	Path.home()
	/"testingFolder"
	)
for path in reports_dir.glob("*.pdf"):
	print(path.name)

testing_folder = list(reports_dir.glob("*.pdf"))
testing_folder.sort()
print("\n")
for path in testing_folder:
	print(path.name)

# Concatenate the 3 pdfs using append()
for path in testing_folder:
	pdf_merger.append(str(path))

with Path("appended_pdf.pdf").open(mode="wb") as output_file:
	pdf_merger.write(output_file)

# Merge using merge()
report_dir = (
	Path.home()
	/ "testMerge"
	)
report_path = report_dir / "first.pdf"
toc_path = report_dir / "newtest.pdf"

pdf_merger.append(str(toc_path))
pdf_merger.merge(1, str(report_path))

with Path("final.pdf").open(mode="wb") as output_file:
	pdf_merger.write(output_file)

# Rotating and cropping Pdfs
pdf_path = (
	Path.home()
	/"rotating-cropping"
	/"first.pdf")

pdf_reader = PdfFileReader(str(pdf_path))
pdf_writer = PdfFileWriter()

"""
For rotation we use rotateClockwise() and rotateCounterClockwise()

"""
for n in range(pdf_reader.getNumPages()):
	page = pdf_reader.getPage(n)
	page.rotateClockwise(90)
	pdf_writer.addPage(page)

with Path("rotating-cropping/rotated.pdf").open(mode="wb") as output_file:
	pdf_writer.write(output_file)

# Cropping
first_page = pdf_reader.getPage(0)
print(first_page.mediaBox)

"""
Rectangle object has 4 attributes that return the coordinates of the rectangles corners: lowerLeft, lowerRight, upperLeft, upperRight 
"""

# Just altering the upperLeft
first_page.mediaBox.upperLeft = (0, 300)
with Path("rotating-cropping/cropped.pdf").open(mode="wb") as output_file:
	pdf_writer.write(output_file)

# Encrypting and Decrypting
# Encrypting
"""
You can add password protection using .encrypt()
1. user_pwd sets the user password.
2. owner_pwd sets the owner password.
"""

pdf_path = (
	Path.home()
	/"encrypt-and-decrypt"
	/"first.pdf"
	)
pdf_reader = PdfFileReader(str(pdf_path))

# Create a new PdfFileWriter instance and add the pages from pdf_reader
pdf_writer = PdfFileWriter()
pdf_writer.appendPagesFromReader(pdf_reader)

# Adding the user password
pdf_writer.encrypt(user_pwd="1234")

with Path("encrypt-and-decrypt/encrypted.pdf").open(mode="wb") as output_file:
	pdf_writer.write(output_file)

# Here both user and owner password is set to 1234
# To give a second one, just pass a second parameter

user_pwd = "1234"
owner_pwd = "5678"
pdf_writer.encrypt(user_pwd=user_pwd, owner_pwd=owner_pwd)

with Path("encrypt-and-decrypt/encrypted2.pdf").open(mode="wb") as output_file:
	pdf_writer.write(output_file)

# Decrypting Pdfs
"""
We use decrypt() method.It has a single parameter called password that you can use to provide the password for decryption.
"""

pdf_path = (
	Path.home()
	/"encrypt-and-decrypt"
	/"encrypted.pdf")
pdf_reader = PdfFileReader(str(pdf_path))

pdf_reader.decrypt(password="1234")

"""
.decrypt() returns an integer representing the success of the decryption:

0 indicates that the password is incorrect.
1 indicates that the user password was matched.
2 indicates that the owner password was matched.
"""

print(pdf_reader.getPage(0))