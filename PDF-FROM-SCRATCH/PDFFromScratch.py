from reportlab.pdfgen.canvas import Canvas

canvas = Canvas("NewPdfFromScratch.pdf")

#adding some text to the PDF using .drawString()
canvas.drawString(72, 72, "New pdf")
"""
The first two arguments passed determine the location on the canvas
where the text is writter. The first specifies the distance from th left edge of the canvas, and the 
second specifies the distance from the bottom edge.
"""

canvas.save()

# Setting the Page size usinf .pagesize parameter
canvas = Canvas("NewPdfFromScratch.pdf", pagesize=(612.0, 792.0))

# For some general page size form reportlab.lib.pagesize module
from reportlab.lib.units import inch, cm
from reportlab.lib.pagesizes import LETTER
canvas = Canvas("NewPdfFromScratch.pdf", pagesize=LETTER)

"""
Page Size	Dimensions
A4	        210 mm x 297 mm
LETTER	    8.5 in x 11 in
LEGAL	    8.5 in x 14 in
TABLOID	    11 in x 17 in
"""

# Setting the Font properties using .setFont()
canvas.setFont("Times-Roman", 18)
canvas.drawString(1 * inch, 10 * inch, "Times New Roman (18pt)")
canvas.save()

"""
There are three fonts available by default:

"Courier"
"Helvetica"
"Times-Roman"
Each font has bolded and italicized variants. Here’s a list of all the font variations available in reportlab:

"Courier"
"Courier-Bold
"Courier-BoldOblique"
"Courier-Oblique"
"Helvetica"
"Helvetica-Bold"
"Helvetica-BoldOblique"
"Helvetica-Oblique"
"Times-Bold"
"Times-BoldItalic
"Times-Italic"
"Times-Roman"
"""

# Set font color using .setFillColor()
from reportlab.lib.colors import blue 

canvas = Canvas("NewPdfFromScratchWithColor.pdf", pagesize=LETTER)
canvas.setFont("Times-Roman", 12)
canvas.setFillColor(blue)
canvas.drawString(1 * inch, 10 * inch, "We got a blue color")
canvas.save()