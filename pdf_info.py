# importing all the required modules
import PyPDF2
import os
import codecs
import pdfminer.high_level
import sys
import textract

# creating an object
pdf_path = os.path.join(os.path.dirname(__file__), 'data/sf_serman_r2.pdf')
new_file = os.path.join(os.path.dirname(__file__), 'data/text.txt')
file = open(pdf_path, 'rb')
textr_act = textract.process(pdf_path, encode='utf-8')
print(textr_act)


with open(pdf_path, "rb") as fp:
    pdfminer.high_level.extract_text_to_fp(fp, sys.stdout)





# creating a pdf reader object
# pdfReader = PyPDF2.PdfFileReader(file)
#
# pages_num = pdfReader.numPages
# for page_num in range(1, pages_num):
#     print(f'page number {page_num}:')
#     pageObj = pdfReader.getPage(page_num)
#     text = pageObj.extractText()
#     # text_decoded = text.encode('latin').decode('windows-1251')
#     # text_decoded = text.encode('utf-8', errors='replace')#.decode('windows-1251')
#     text_decoded = text.encode('windows-1251', errors='replace')  # .decode('windows-1251')
#     print(text_decoded)