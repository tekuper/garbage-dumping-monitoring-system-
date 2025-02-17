from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2
from ultralytics import YOLO

# -------------------
# Function 1: Run YOLO Inference
# -------------------
def predict_objects(image_path, model):
    """Runs YOLO object detection on an image and returns the processed image with bounding boxes."""
    results = model(image_path)  # Perform detection

    if results:
        result = results[0]  # Get first detection result
        img_with_boxes = result.plot()

        if img_with_boxes is not None:
            output_path = image_path.replace(".jpg", "_detected.jpg")  # Save with a new name
            
            # Save using Pillow instead of OpenCV
            Image.fromarray(img_with_boxes).save(output_path)

            return output_path  # Return path of the saved image
        else:
            print("❌ ERROR: `result.plot()` returned None. No image to save.")
    else:
        print("❌ ERROR: No detection results found.")
    
    return None  # Return None if no valid image is created

# -------------------
# Function 2: Display Image Without OpenCV
# -------------------
def display_image(image_path):
    """Reads and displays an image using Matplotlib (without OpenCV)."""
    try:
        img = Image.open(image_path)  # Open image using Pillow

        # Display the image using Matplotlib
        plt.figure(figsize=(10, 6))
        plt.imshow(img)  # No need to convert BGR to RGB
        plt.axis("off")  # Hide axis labels
        plt.title("Detection Results")
        plt.show(block=True)  # Display the image in Jupyter Notebook
    except Exception as e:
        print(f"❌ ERROR: Could not load image from {image_path}: {e}")