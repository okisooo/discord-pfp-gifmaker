from PIL import Image, ImageTk
from tkinter import Tk, Button, filedialog, Label

def upload_image():
    # Open a file dialog to select an image file
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.png")])

    if file_path:
        # Load the original image
        original = Image.open(file_path)

        # Resize the original image for visualization in the GUI
        resized_original = original.resize((300, 300))

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

            # Resize the output image for visualization in the GUI
            resized_output = Image.open(output_path).resize((300, 300))

            # Show the resized uploaded image
            uploaded_image = ImageTk.PhotoImage(resized_original)
            uploaded_label.configure(image=uploaded_image)
            uploaded_label.image = uploaded_image

            # Show the resized output image
            output_image = ImageTk.PhotoImage(resized_output)
            output_label.configure(image=output_image)
            output_label.image = output_image

            # Enable the button to open the output image file
            open_button.configure(state="normal", command=lambda: open_output(output_path))

def open_output(file_path):
    # Open the output image file
    import os
    os.system(f'start {file_path}')

# Create the GUI interface
root = Tk()
root.title("Image Uploader")
root.geometry("700x400")

# Create a label to display the resized uploaded image
uploaded_label = Label(root)
uploaded_label.pack(side="left")

# Create a label to display the resized output image
output_label = Label(root)
output_label.pack(side="right")

# Create an "Upload Image" button
upload_button = Button(root, text="Upload Image", command=upload_image)
upload_button.pack()

# Create a button to open the output image file
open_button = Button(root, text="Open Output", state="disabled")
open_button.pack()

# Start the GUI event loop
root.mainloop()
