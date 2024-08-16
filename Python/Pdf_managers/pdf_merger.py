import PyPDF2
import os

# Directory containing the PDFs
pdf_dir = 'D:\\2nd PUC'

# List of PDF files in the directory
pdf_files = [
    'chapter-1-typical-configuration-of-computer.pdf',
    'chapter-2-boolean-algebra.pdf',
    'chapter-3-logic-gates.pdf',
    'chapter-4-data-structure.pdf',
    'chapter-6-oops.pdf',
    'chapter-7-classes-and-objects.pdf',
    'chapter-8-function-overloading.pdf',
    'chapter-9-constructors.pdf',
    'chapter-10-inheritance.pdf',
    'chapter-11-pointers.pdf',
    'chapter-12-data-file-handling.pdf',
    'chapter-13-database-concepts.pdf',
    'chapter-14-sql-commands.pdf',
    'chapter-15-networking-concepts.pdf',
    'chapter-16-internet-and-open-source-concepts.pdf',
    'chapter-17-web-designing2.pdf',
    'chapter-18-lab-manual.pdf'
]

# Create a PdfMerger object
merger = PyPDF2.PdfMerger()

# Append each PDF file to the merger
for pdf in pdf_files:
    merger.append(os.path.join(pdf_dir, pdf))

# Write out the merged PDF
with open(os.path.join(pdf_dir, 'merged_document.pdf'), 'wb') as output_pdf:
    merger.write(output_pdf)

print("PDFs merged successfully!")
