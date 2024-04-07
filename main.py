import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfReader, PdfWriter

# Function to decrypt a PDF file
def decrypt_pdf(input_path, output_path, password):

    with open(input_path, 'rb') as file:
        reader = PdfReader(file)

        if reader.is_encrypted:
            reader.decrypt(password)
            
            writer = PdfWriter()
            
            for page in reader.pages:
                writer.add_page(page)
            
            with open(output_path, 'wb') as output_file:
                writer.write(output_file)
            
            status_label.config(text="PDF decrypted successfully.")
        else:
            status_label.config(text="PDF is not encrypted.")