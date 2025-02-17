import pandas as pd  # Import pandas for handling tabular data (CSV processing)
import json  # Import JSON module for parsing detection data

def process_littering_data(input_csv, output_csv):
    """
    Processes a CSV file containing littering detection results and converts it into a structured format.

    Args:
        input_csv (str): Path to the input CSV file.
        output_csv (str): Path to save the processed annotations.

    Returns:
        None
    """
    print(f"Starting the processing of {input_csv}...")  # Indicate function execution start

    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv(input_csv)
    print(f"CSV file loaded successfully. Total rows: {len(df)}")  # Confirm CSV load and print total row count

    # Initialize an empty list to store structured annotation data
    rows = []
    
    # Iterate through each row in the DataFrame
    for _, row in df.iterrows():
        filename = row["Filename"]  # Extract the filename
        detections = row["Detections"]  # Extract detections, which is a JSON-like string

        # Skip rows where detections are empty or invalid (not a string or empty string)
        if not isinstance(detections, str) or len(detections.strip()) == 0:
            print(f"Skipping empty detections for {filename}")  # Log skipped detections
            continue  # Move to the next row

        try:
            # Convert the JSON string to a dictionary (Fix improperly formatted JSON using string replacement)
            detections = json.loads(detections.replace("'", '"'))  # Ensure valid JSON format

            # Check if the "data" key exists and contains at least one detection
            if "data" in detections and detections["data"]:
                for obj in detections["data"][0]:  # Iterate through the list of detected objects
                    label = obj["label"]  # Extract object class label
                    x_min, y_min, x_max, y_max = obj["bounding_box"]  # Extract bounding box coordinates
                    rows.append([filename, label, x_min, y_min, x_max, y_max])  # Append structured data
        except Exception as e:
            print(f"Error parsing detections for {filename}: {e}")  # Log JSON parsing errors
            continue  # Skip to the next row

    # Convert the extracted annotation data into a new DataFrame
    output_df = pd.DataFrame(rows, columns=["Filename", "Label", "x_min", "y_min", "x_max", "y_max"])

    # Save the structured annotations to a new CSV file
    output_df.to_csv(output_csv, index=False)

    print(f"Training annotations saved successfully to {output_csv}")  # Confirm function completion
