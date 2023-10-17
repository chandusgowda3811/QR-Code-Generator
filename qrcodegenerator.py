import qrcode
from PIL import Image
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk

# Function to generate a QR code
def generate_qr_code(url, save_path):
    qr = qrcode.QRCode(
        version=1,  # Use a lower version (e.g., version 1)
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    qr_code = qr.make_image(fill_color="black", back_color="white")
    qr_code.save(save_path)

# Function to display the QR code using Tkinter
def display_qr_code(url):
    qr = qrcode.QRCode(
        version=1,  # Use a lower version (e.g., version 1)
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    qr_code = qr.make_image(fill_color="black", back_color="white")
    qr_code = qr_code.resize((300, 300))

    qr_photo = ImageTk.PhotoImage(qr_code)

    qr_label.config(image=qr_photo)
    qr_label.image = qr_photo

# Function to save the QR code using Tkinter's file dialog
def save_qr_code(url):
    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
    if save_path:
        try:
            generate_qr_code(url, save_path)
            messagebox.showinfo("QR Code Saved", f"QR Code saved as {save_path}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while generating the QR code: {e}")

# Function to clear the input and QR code
def clear_input():
    url_entry.delete(0, tk.END)
    qr_label.config(image=None)
    qr_label.image = None

# Create a Tkinter window for input
input_window = tk.Tk()
input_window.title("QR Code Generator")
input_window.geometry("450x550")  # Set the window size

font = ('Arial', 14)  # Set the font and font size

menu_bar = tk.Menu(input_window)
input_window.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open")
file_menu.add_command(label="Save", command=lambda: save_qr_code(url_entry.get()))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=input_window.quit)

url_label = tk.Label(input_window, text="Enter a URL:", font=font)
url_label.pack(padx=10, pady=5)

url_entry = tk.Entry(input_window, font=font)
url_entry.pack(padx=10, pady=5)

display_button = tk.Button(input_window, text="Display QR Code", command=lambda: display_qr_code(url_entry.get()), bg="blue", fg="white", font=font)
display_button.pack(padx=10, pady=5)

save_button = tk.Button(input_window, text="Save QR Code", command=lambda: save_qr_code(url_entry.get()), bg="blue", fg="white", font=font)
save_button.pack(padx=10, pady=5)

clear_button = tk.Button(input_window, text="Clear", command=clear_input, bg="blue", fg="white", font=font)
clear_button.pack(padx=10, pady=5)

qr_label = tk.Label(input_window, font=font)
qr_label.pack(padx=10, pady=10)

input_window.mainloop()
