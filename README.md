
# PDF Upper Half Cropping and Merging Tool

This Python script processes a PDF file by cropping the upper half of each page and combining two half pages into a single A4-sized page. This is useful for creating a condensed, merged PDF from an existing document.

## Features
- Crops the top half of each page in a PDF.
- Combines two cropped half-pages onto a single A4 page in a new PDF.

## Requirements
- Python 3.x
- [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/) (`fitz` module)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/0xr27/pdf-upper-half-cropper.git
   cd pdf-upper-half-cropper
   ```

2. Install dependencies:
   ```bash
   pip3 install -r requirements.txt
   ```

## Usage

1. Place your input PDF file in the same directory as `crop_pdf_upper_half.py`, or specify its path in the script.
2. Run the script:
   ```bash
   python3 crop_pdf_upper_half.py
   ```

The processed PDF will be saved as `output_half_page_combined.pdf`.

## Example
- `input.pdf`: Your original PDF file with multiple pages.
- `output_half_page_combined.pdf`: The generated PDF with each page containing two upper halves combined onto an A4 page.

## Notes
- Ensure `input.pdf` is in the correct format and path.
- Modify the `input_path` and `output_path` variables in the script as needed.

## License
This project is licensed under the MIT License.
