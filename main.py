import qrcode
import tkinter as tk
from PIL import Image, ImageTk
import webbrowser

def generate_qr_code():
    input_URL = url_entry.get()
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=15,
        border=4,
    )

    qr.add_data(input_URL)
    qr.make(fit=True)

    img = qr.make_image(fill_color="red", back_color="white")
    img.save("url_qrcode.png")

    # Display the QR code image in the GUI
    qr_image = Image.open("url_qrcode.png")
    qr_image = qr_image.resize((200, 200), Image.LANCZOS)
    qr_photo = ImageTk.PhotoImage(qr_image)
    qr_label.config(image=qr_photo)
    qr_label.image = qr_photo

    # Store the URL to open when the QR code is clicked
    qr_label.url = input_URL

def open_url(event):
    # Open the URL in the default web browser
    webbrowser.open(event.widget.url)

# Create a GUI window
window = tk.Tk()
window.title("QR Code Generator")

# Create and place a label for the URL input
url_label = tk.Label(window, text="Enter the URL:")
url_label.pack()

url_entry = tk.Entry(window)
url_entry.pack()

# Create and place a button to generate the QR code
generate_button = tk.Button(window, text="Generate QR Code", command=generate_qr_code)
generate_button.pack()

# Create a label to display the generated QR code
qr_label = tk.Label(window)
qr_label.pack()

# Bind a click event to the QR code label
qr_label.bind("<Button-1>", open_url)

# Start the GUI main loop
window.mainloop()
