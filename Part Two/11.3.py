import PyPDF2
import os
import string
import time

start = time.time()
file_handle = open('Sense-and-Sensibility-by-Jane-Austen.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(file_handle)
page_number = len(pdfReader.pages) # this tells you total pages
page_object = pdfReader.pages[0] # We just get page 0 as example >>> page_text = page_object.extractText() 

frequency_table = {}

for page_num in range(len(pdfReader.pages)):