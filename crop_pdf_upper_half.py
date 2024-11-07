import fitz  # PyMuPDF

# Open the original PDF
input_path = "input.pdf"
output_path = "output_half_page_combined.pdf"
input_pdf = fitz.open(input_path)
output_pdf = fitz.open()  # Used to store the new PDF as a PyMuPDF object

# A4 dimensions
a4_width = 595  # A4 width (pixels, approximately 210mm)
a4_height = 842  # A4 height (pixels, approximately 297mm)

# Crop the upper half of each page and combine into A4 pages
for page_num in range(0, input_pdf.page_count, 2):
    # Create a new A4 page
    new_page = output_pdf.new_page(width=a4_width, height=a4_height)
    
    # Process the upper half of the first page
    page1 = input_pdf.load_page(page_num)
    rect = page1.rect
    half_height = rect.height / 2
    clip_area = fitz.Rect(rect.x0, rect.y0, rect.x1, half_height)
    new_page.show_pdf_page(fitz.Rect(0, a4_height / 2, a4_width, a4_height), input_pdf, page_num, clip=clip_area)
    
    # Process the upper half of the second page (if there is a second page)
    if page_num + 1 < input_pdf.page_count:
        page2 = input_pdf.load_page(page_num + 1)
        new_page.show_pdf_page(fitz.Rect(0, 0, a4_width, a4_height / 2), input_pdf, page_num + 1, clip=clip_area)

# Save the combined pages as a new PDF file
output_pdf.save(output_path)
output_pdf.close()
input_pdf.close()

print("Generated combined A4 PDF:", output_path)
