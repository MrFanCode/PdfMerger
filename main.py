from pypdf import PdfWriter

# Create a PdfWriter object
merger = PdfWriter()

file1 = "/home/john/Desktop/KPTM/ITNS TNW2283/topic 7/topic7_part1.pdf"
file2 = "/home/john/Desktop/KPTM/ITNS TNW2283/topic 7/topic7_part2.pdf"
file3 = "/home/john/Desktop/KPTM/ITNS TNW2283/topic 7/topic7_part3.pdf"

# List of PDF files to merge 
pdfs = [file1, file2, file3]


# Append each PDF file to the merger 
for pdf in pdfs:
    merger.append(pdf)


# Write the merged PDF to a new file 
merger.write("merged-pdf.pdf")

# Close the merger object
merger.close()






