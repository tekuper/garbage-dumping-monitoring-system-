# 🎯 Object Detection Function
# -------------------
import os  # Import OS module for handling environment variables and file paths
import sys  # Import sys module for modifying the system path

# Add the directory of the convert_to_jpg module to the system path
sys.path.append("Landing_ai_agent\\convert_to_jpg.py")

# Import the convert_to_jpg function to ensure all images are in JPG format
from convert_to_jpg import convert_to_jpg

# Import dotenv to load environment variables from a .env file
from dotenv import load_dotenv

# Load environment variables (override=True ensures existing values are updated)
load_dotenv(override=True)

# Import requests module for making API calls
import requests

# Retrieve API key and URL from environment variables
api_key = os.getenv('API_key')  # API authentication key
api_url = os.getenv('API_url')  # API endpoint URL

def detect_objects(image_path):
    """
    Sends an image to the Landing AI API for object detection.

    Args:
        image_path (str): Path to the image file.

    Returns:
        dict or str: JSON response containing detected objects or an error message.
    """

    # Ensure the input image is in JPG format
    converted_image_path = convert_to_jpg(image_path)

    # Open the converted image file in binary mode
    with open(converted_image_path, "rb") as img:
        files = {"image": img}  # Prepare image file for API request

        # Define the request payload
        data = {
            "prompts": ["person", "garbage", "litter", "trash"],  # Object categories to detect
            "model": "owlv2",  # AI model to use for detection
            "function_name": "owl_v2_video"  # API function being called
        }

        # Set request headers, including API authentication
        headers = {"Authorization": f"Bearer {api_key}"}

        # Send POST request to the AI API with the image, data, and headers
        response = requests.post(api_url, files=files, data=data, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            return response.json()  # Return JSON response with detected objects
        else:
            return f"❌ Error {response.status_code}: {response.text}"  # Return error message
