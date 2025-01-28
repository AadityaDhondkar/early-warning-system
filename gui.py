import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
from backend import load_data, create_map
import webbrowser

# GUI setup
root = tk.Tk()
root.title("Early Warning System")
root.geometry("500x300")

file_path = None  # Global variable to store the file path

# Function to upload an Excel file
def upload_file():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
    if file_path:
        lbl_file.config(text=f"File Selected: {file_path}")
        messagebox.showinfo("Success", "File successfully loaded!")

# Function to generate the map
def generate_map():
    global file_path
    if not file_path:
        messagebox.showerror("Error", "Please upload an Excel file first!")
        return

    try:
        data = load_data(file_path)
        create_map(data)
        messagebox.showinfo("Success", "Map successfully generated as 'map.html'")
        webbrowser.open("map.html")  # Open the generated map in the browser
    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate map: {e}")

# UI Elements
lbl_title = tk.Label(root, text="Early Warning System", font=("Arial", 16, "bold"))
lbl_title.pack(pady=10)

btn_upload = tk.Button(root, text="Upload Excel File", command=upload_file)
btn_upload.pack(pady=5)

lbl_file = tk.Label(root, text="No file selected", font=("Arial", 10))
lbl_file.pack(pady=5)

btn_generate = tk.Button(root, text="Generate Map", command=generate_map)
btn_generate.pack(pady=10)

root.mainloop()
