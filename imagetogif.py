from PIL import Image, ImageTk
from tkinter import Tk, Button, filedialog, Label
import os

def upload_image():
    # Open a file dialog to select an image file
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.png")])

    if file_path:
        # Load the original image
        original = Image.open(file_path)

        # Create a new GIF image with the same dimensions as the original image
        gif = Image.new('RGBA', original.size)

        # Create a list of colors for the 8x8 area
        colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255), (255, 255, 255), (0, 0, 0), (128, 128, 128), (255, 165, 0)]

        frames = []

        # Loop 10 times
        for i in range(10):
            # Copy the original image onto the new GIF image
            frame = original.copy()

            # Create a new 8x8 image with a unique color
            color_image = Image.new('RGBA', (8, 8), colors[i])

            # Paste the color image into the bottom right corner of the new GIF image
            frame.paste(color_image, (frame.width - 8, frame.height - 8))

            frames.append(frame)

        # Ask the user to choose where to save the output GIF
        output_path = filedialog.asksaveasfilename(defaultextension=".gif", filetypes=[("GIF Files", "*.gif")])

        if output_path:
            # Save the new GIF image with higher quality to the selected path
            frames[0].save(output_path, save_all=True, append_images=frames[1:], loop=0, duration=500, optimize=False, quality=100)

            # Show a completion message
            completion_label.config(text="Conversion complete!")

def open_output(file_path):
    # Open the output image file
    os.system(f'start {file_path}')

# Create the GUI interface
root = Tk()
root.title("Image Uploader")
root.geometry("300x200")  # Smaller window size

# Create an "Upload Image" button with better styling
upload_button = Button(root, text="Upload Image", command=upload_image, bg="lightblue", relief="solid", borderwidth=2, padx=10, pady=5, font=("Arial", 12), cursor="hand2")
upload_button.pack(pady=20)

# Create a label for the completion message
completion_label = Label(root, text="", fg="green")
completion_label.pack()

# Start the GUI event loop
root.mainloop()
