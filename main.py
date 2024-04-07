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


# Function to let the user select a PDF file
def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    # Clear any previous entry and insert the selected file path into the entry widget
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)

    