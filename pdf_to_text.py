import argparse
import PyPDF2

def pdf_to_txt(pdf_file):
    with open(pdf_file, 'rb') as file:
        pdf = PyPDF2.PdfReader(file)
        text = ''
        for page in range(len(pdf.pages)):
            text += pdf.pages[page].extract_text()
        return text

parser = argparse.ArgumentParser(description='Convert a PDF file to a text file')
parser.add_argument('pdf_file', type=str, help='the input PDF file')
parser.add_argument('txt_file', type=str, help='the output text file')

args = parser.parse_args()

with open(args.txt_file, 'w') as file:
    file.write(pdf_to_txt(args.pdf_file))




# command and args
# python script_name.py input.pdf output.txt
