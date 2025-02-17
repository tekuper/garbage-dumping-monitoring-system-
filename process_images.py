from PIL import Image, ImageDraw  # Importing PIL (Pillow) for image processing and annotation
import os  # Importing os for file path operations

# Define input and output folders
INPUT_FOLDER = r"C:\Users\User\Desktop\Monitoring System"  # Folder with input images
OUTPUT_FOLDER = "outputted_images"  # Folder for processed images

def process_image(image_path, detections):
    """ 
    Annotates an image with bounding boxes based on detected objects 
    and saves it with the annotations.

    Args:
        image_path (str): Path to the input image file.
        detections (dict): JSON-like dictionary containing detection data.

    Returns:
        tuple: (output_image_path, status_message) - Path to the processed image and status message.
    """

    # Check if detections exist and contain valid data
    if not detections or "data" not in detections:
        return None, "Detection Failed"  # Return failure if no detections are found

    annotations = detections["data"][0]  # Extract the list of detected objects

    # Open the image file
    image = Image.open(image_path)

    # Create a drawing context to annotate the image
    draw = ImageDraw.Draw(image)

    # Iterate through detected objects and draw bounding boxes
    for obj in annotations:
        x1, y1, x2, y2 = obj["bounding_box"]  # Extract bounding box coordinates
        label = obj["label"]  # Extract object label
        score = obj["score"]  # Extract confidence score

        # Draw a red bounding box around the detected object
        draw.rectangle([x1, y1, x2, y2], outline="red", width=3)

        # Add label text with confidence score above the bounding box
        draw.text((x1, y1 - 10), f"{label} ({score:.2f})", fill="red")

    # Prepare output file path
    output_image_name = os.path.basename(image_path)  # Extract the filename from the path
    output_image_path = os.path.join(OUTPUT_FOLDER, output_image_name)  # Set output file location

    # Save the annotated image
    image.save(output_image_path)

    # Return the path of the processed image along with a success message
    return output_image_path, "Processed Successfully"
