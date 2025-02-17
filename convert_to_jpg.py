# 📷 Image Processing Functions
# -------------------
import os  # Import OS module for file operations
from PIL import Image  # Import PIL (Pillow) for image processing

def convert_to_jpg(image_path):
    """
    Converts an image to JPG format if it's not already in that format.

    Args:
        image_path (str): Path to the input image.

    Returns:
        str: Path to the converted JPG image.
    """

    # Check if the image is already in JPG format (case-insensitive check)
    if image_path.lower().endswith(".jpg"):  # Fix `.JPG` to `.jpg` for consistency
        return image_path  # If already JPG, return the original path

    # Open the image file
    img = Image.open(image_path)

    # Generate a new file path with the .jpg extension (removes original extension)
    jpg_path = os.path.splitext(image_path)[0] + ".jpg"

    # Convert the image to RGB (removes transparency if PNG) and save as JPEG format
    img.convert("RGB").save(jpg_path, "JPEG")

    return jpg_path  # Return the path of the converted JPG image
