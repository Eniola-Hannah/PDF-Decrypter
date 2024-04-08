import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfReader, PdfWriter
from customtkinter import *


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


# Function to initiate PDF decryption process
def decrypt():
    input_path = file_entry.get()
    
    output_path = input_path[:-4] + "_decrypted.pdf"
    
    password = password_entry.get()
    
    decrypt_pdf(input_path, output_path, password)  


# GUI setup using tkinter
# root = tk.Tk()
root = CTk()
root.geometry("500x400")
root.title("GROUP 4 PDF DECRYPTER")
set_appearance_mode("light")


# Label and entry widget for selecting a PDF file
# file_label = tk.Label(root, text="Select PDF File:")
file_label = CTkLabel(master=root, text="Select PDF File: ", font=("Arial", 20))
file_label.pack()
file_entry = CTkEntry(root, width=300)
file_entry.pack(pady=10)


# Button to open file dialog for selecting a PDF file
# browse_button = tk.Button(root, text="Browse", command=select_file)
browse_button = CTkButton(master=root, text="Browse", corner_radius=32, fg_color="#C850C0", hover_color="#4158D0", command=select_file)
browse_button.place(relx=0.5, rely=0.5, anchor="center")
browse_button.pack(pady=20)


# Label and entry widget for entering the password
# password_label = tk.Label(root, text="Enter Password:")
password_label = CTkLabel(root, text="Enter Password: ", font=("Arial", 20), pady=10)
password_label.pack()
password_entry = CTkEntry(root, show="*", width=300, placeholder_text="Enter the password here...")
password_entry.pack(pady=10)


# Button to initiate PDF decryption process
# decrypt_button = tk.Button(root, text="Decrypt", command=decrypt)
decrypt_button = CTkButton(master=root, text="Decrypt", corner_radius=32, hover_color="#4158D0", command=decrypt)
decrypt_button.pack(pady=10)


# Label to display status messages (e.g., success or failure)
# status_label = tk.Label(root, text="")
status_label = CTkLabel(root, text="", font=("Arial", 20))
status_label.pack(pady=10)


# Start the tkinter main event loop
root.mainloop()