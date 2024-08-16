from fpdf import FPDF

# Create instance of FPDF class
pdf = FPDF()

# Add a page
pdf.add_page()

# Set font
pdf.set_font("Arial", size=12)

# Open the text file in read mode with UTF-8 encoding
with open("yourfile.txt", "r", encoding="utf-8") as file:
    # Insert the texts in the PDF
    for line in file:
        pdf.cell(200, 10, txt=line.encode('latin-1', 'replace').decode('latin-1'), ln=True)

# Save the PDF with name .pdf
pdf.output("output.pdf")
