import os  # Import OS module for handling file paths
import shutil  # Import shutil module for copying files

# Define input folders
INPUT_IMAGES_FOLDER = r"C:\Users\User\Desktop\Monitoring System"  # Folder containing all images
INPUT_LABELS_FOLDER = r"C:\Users\User\Desktop\yolo_annotations"  # Folder containing YOLO annotation files

def copy_files(image_list, dest_images_folder, dest_labels_folder):
    """
    Copies image and corresponding label files to their respective directories.

    Args:
        image_list (list): List of filenames (including extensions).
        dest_images_folder (str): Destination folder for images.
        dest_labels_folder (str): Destination folder for label files.

    Returns:
        None
    """

    # Iterate through each image filename in the provided list
    for img_file in image_list:
        # Construct the full path for the image file
        img_path = os.path.join(INPUT_IMAGES_FOLDER, img_file)

        # Construct the corresponding label file name by replacing the extension with ".txt"
        label_file = os.path.splitext(img_file)[0] + ".txt"

        # Construct the full path for the label file
        label_path = os.path.join(INPUT_LABELS_FOLDER, label_file)

        try:
            # Copy image file to the destination folder
            shutil.copy(img_path, os.path.join(dest_images_folder, img_file))

            # Copy corresponding label file to the destination folder
            shutil.copy(label_path, os.path.join(dest_labels_folder, label_file))
        
        except FileNotFoundError as e:
            print(f"⚠️ Warning: File not found - {e}")
        except Exception as e:
            print(f"❌ Error while copying files: {e}")
