from tkinter import *
from tkinter import filedialog, ttk, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont
from typing import Any

root = Tk()
root.title("Image Watermarking Application")
root.config(padx=20, pady=20)
root.minsize(420, 340)

options_frame = Frame(root)
options_frame.pack(side="top", pady=5)
button_frame = Frame(root)
button_frame.pack(side="top", pady=(10, 5))

img_path = None
final_image: Any = None

#------------------------ Functions -------------------------#
def select_image():
    global img_path
    # Define the allowed image formats
    image_formats = [
        (
            "Image Files",
            "*.jpg; *.jpeg; *.png; *.gif; *.bmp; *.webp",
        ),  # Groups all formats together
    ]

    #Open the file dialog and captures the selected file path
    img_path = filedialog.askopenfilename(
        title="Select an Image", filetypes=image_formats
    )

    # Display or process the selected file path
    if img_path:
        #Captures the returned PhotoImage object
        img_to_display = process_image(img_path)

        label_result.config(text="", image=img_to_display)

        #Anchor the image to prevent Python from deleting it
        label_result.image = img_to_display

        style_dropdown.config(state="readonly")
        style_dropdown.pack(side="top", pady=5)
    else:
        label_result.config(text="No file selected.")

def process_image(path_string):
    pil_image = Image.open(path_string)
    fit_size = (500, 350)

    #Modifies pil_image directly in-place
    pil_image.thumbnail(fit_size)

    #Now pil_image is perfectly resized
    tk_image = ImageTk.PhotoImage(pil_image)
    return tk_image

def handle_watermark_choice(event):
    #Grab the current string selection from the dropdown
    choice = style_dropdown.get()

    #Show or hide widgets based on choice made
    #Reveal all three position options and opacity slider
    rad_left.pack(side="left", padx=10)
    rad_center.pack(side="left", padx=10)
    rad_right.pack(side="left", padx=10)
    opacity_scale.pack(side="top", pady=(5, 10))

    if choice == "Text Watermark":
        watermark_entry.pack(side="top", pady=5) # Reveal the text field!
        btn_watermark.pack(side="left", padx=5)   # Reveal the button also

        #Hide Logo Widgets
        btn_select_logo.pack_forget()

    elif choice == "Logo Watermark":
        #Hide Text Widgets
        watermark_entry.pack_forget()
        btn_watermark.pack_forget()

        #Show Logo Widgets
        btn_select_logo.pack(side="top", pady=5)

def create_text_watermark():
    global img_path, final_image

    #Open original image file and convert to RGBA
    im = Image.open(img_path).convert("RGBA")
    # Grab the dimensions of the original full-res image
    img_w, img_h = im.size

    #Calculate dynamic font size (5% of height)
    dynamic_font_size = int(img_h * 0.05)

    #Keep the watermark string text and the new image layer completely separate!
    user_text = watermark_entry.get()
    text_layer = Image.new("RGBA", im.size, (255, 255, 255, 0))  # Clean transparent slate

    #Reads from Radio Buttons
    position_choice = position_var.get()

    #Loads font using calculated dynamic scale!
    try:
        font = ImageFont.truetype("arial.ttf", dynamic_font_size)
    except IOError:
        font = ImageFont.load_default()

    #Fix: Tie the drawing sheet to the text_layer, NOT the main image
    draw = ImageDraw.Draw(text_layer)

    # Virtual Measuring Tape: How wide and tall the text frame is
    bbox = draw.textbbox((0, 0), text=user_text, font=font)
    # From the tuple in draw.textbbox() module; bbox = (left, top, right, bottom)
    text_w = bbox[2] - bbox[0]  # Right edge minus Left edge = Width
    text_h = bbox[3] - bbox[1]  # Bottom edge minus Top edge = Height

    #Safety Margins: Keep text 3% away from the very edges of the photo
    margin_x = int(img_w * 0.03)
    margin_y = int(img_h * 0.03)

    #Calculates starting coordinates (x, y)
    if position_choice == "Center":
        x = (img_w - text_w) // 2
        y = (img_h - text_h) // 2
    elif position_choice == "Bottom-Right":
        x = img_w - text_w - margin_x
        y = img_h - text_h - margin_y
    else:
        x = margin_x
        y = margin_y

    #Grab the slider value
    alpha_value = opacity_scale.get()

    # Draws text onto the transparent layer with alpha_value
    draw.text((x, y), text=user_text, fill=(255, 255, 255, alpha_value), font=font)

    #Fix: Smash the base image and the text layer together!
    out = Image.alpha_composite(im, text_layer)

    final_image = out

    #Fix: Converting it also to Tkinter by sending the combined result 'out' to the preview helper
    preview_image(out)

def create_logo_watermark():
    global img_path, final_image

    #Open the main base photograph
    im = Image.open(img_path).convert("RGBA")
    img_w, img_h = im.size

    #File browser dialog to select the logo file
    logo_formats = [("Image Files", "*.jpg; *.jpeg; *.png; *.gif; *.bmp; *.webp")]
    logo_path = filedialog.askopenfilename(title="Select Logo", filetypes=logo_formats)

    #If the user cancels the file browser, exit gracefully without crashing
    if not logo_path:
        return

    #Open the logo image file and assign it to a variable
    logo_img = Image.open(logo_path).convert("RGBA")

    #Calculates dynamic logo size (15% of the base image's width)
    target_logo_width = int(img_w * 0.15)

    #The use of a massive height number like img_h as a placeholder.
    # .thumbnail() will ignore it and scale down perfectly based on the width alone
    logo_img.thumbnail((target_logo_width, img_h))
    logo_w, logo_h = logo_img.size

    #Grab the user's position preference from your Radio Buttons variable
    position_choice = position_var.get()

    #Safety Margins (3% of image dimensions)
    margin_x = int(img_w * 0.03)
    margin_y = int(img_h * 0.03)

    #Calculates starting coordinates (x, y) using logo width/height
    if position_choice == "Center":
        x = (img_w - logo_w) // 2
        y = (img_h - logo_h) // 2
    elif position_choice == "Bottom-Right":
        x = img_w - logo_w - margin_x
        y = img_h - logo_h - margin_y
    else:  # Default to Top-Left
        x = margin_x
        y = margin_y

    #Grab the user's chosen opacity value
    alpha_value = opacity_scale.get()

    #Converts the slider scale (0-255) into a clean percentage float (0.0 to 1.0)
    alpha_percentage = alpha_value / 255.0

    #Creates a blank transparent sheet matching the exact size of scaled logo
    transparent_matte = Image.new("RGBA", logo_img.size, (0, 0, 0, 0))

    #Fix: Blend the logo toward transparency without destroying its shape profile
    # A percentage of 1.0 keeps the logo fully intact; 0.5 makes it half transparent.
    faded_logo = Image.blend(transparent_matte, logo_img, alpha_percentage)

    #Pastes the newly faded logo using itself as the stencil mask layer!
    im.paste(faded_logo, (x, y), mask=faded_logo)

    final_image = im

    # Sends the finished composite out to your preview layout helper
    preview_image(im)

def preview_image(pil_img_object):
    #Fix: Makes a temporary clone so the original master file maintains it's resolution
    gui_preview_copy = pil_img_object.copy()

    #Resize ONLY the temporary copy for the desktop display window
    fit_size = (500, 350)
    gui_preview_copy.thumbnail(fit_size)

    #Converts and display it
    tk_image = ImageTk.PhotoImage(gui_preview_copy)
    label_result.config(image=tk_image)
    label_result.image = tk_image  # Anchor reference


def save_image():
    global final_image

    #Safety check: If the user clicks save before creating a watermark, exit quietly
    if final_image is None:
        return

    #Open the OS save dialog box
    save_formats = [
        ("PNG Image", "*.png"),
        ("JPEG Image", "*.jpg;*.jpeg"),
        ("All Files", "*.*")
    ]

    file_destination = filedialog.asksaveasfilename(
        title="Save Watermarked Image",
        defaultextension=".png",  # Automatically appends .png if the user forgets to type it
        filetypes=save_formats
    )

    #If the user picked a location, execute the export
    if file_destination:
        # If saving as JPEG, drop the Alpha channel since JPEG doesn't support transparency
        #Flatten the image back to standard RGB (Deletes the heavy alpha layer data!)
        rgb_output = final_image.convert("RGB")

        #Save with an explicit compression quality and optimize=True
        rgb_output.save(file_destination, "JPEG", quality=80, optimize=True)

    else:
        #If they chose PNG, add the optimize tag alongside compression
        final_image.save(file_destination, "PNG", compress_level=6, optimize=True)

    messagebox.showinfo("Success", "Your watermarked image has been saved successfully!")

#---------------------- Widgets -----------------------------#

    #------------------- Label Section ----------------#
#A label to display the result
label_result = Label(root, text="No file selected yet.", wraplength=350)
label_result.pack(side="top", pady=10, fill="both", expand=True)

    #------------------- Button Section ----------------#
#Implement Image Selection
# Creates a button to trigger the filedialog
btn_select = Button(button_frame, text="Choose Image", command=select_image)
btn_select.pack(side="left", padx=5)

#Select logo
btn_select_logo = Button(button_frame, text="Select Image", command=select_image)

#Apply Watermark
btn_watermark = Button(button_frame, text="Apply", command=create_text_watermark)

#Save Image
btn_save = Button(button_frame, text="Save Image", command=save_image)
btn_save.pack(side="left", padx=5)

    #------------------- Entry / Input Section ----------------#
#Watermark text entry / input
watermark_entry = Entry(root, width=40, bg="white")

    #------------------- Dropdown Section ----------------#
# Defines the dropdown inside the root window setup
style_dropdown = ttk.Combobox(
    root,
    values=["Text Watermark", "Logo Watermark"],
    state="disabled",  # This prevents the user from typing custom text into the dropdown box
    width=25
)
style_dropdown.set("Choose Watermark Type")  # Set a placeholder value
style_dropdown.pack(pady=20)
style_dropdown.bind("<<ComboboxSelected>>", handle_watermark_choice)

    #------------------- Slider Section ----------------#
# Create a slider widget
#Starts at 128 (50% opacity) as a reasonable default choice
opacity_scale = Scale(root, from_=0, to=255, orient="horizontal", label="Opacity Level")
opacity_scale.set(128)

    #------------------- Radio Button Section ----------------#
#Creates the shared variable to hold the position string
position_var = StringVar(value="Center") # Sets "Center" as the automatic default!
#Three radio buttons sharing that same variable
rad_left = Radiobutton(options_frame, text="Top-Left", variable=position_var, value="Top-Left")
rad_center = Radiobutton(options_frame, text="Center", variable=position_var, value="Center")
rad_right = Radiobutton(options_frame, text="Bottom-Right", variable=position_var, value="Bottom-Right")

root.mainloop()