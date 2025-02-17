import pandas as pd  # Importing pandas for data manipulation
import json  # Importing JSON module for handling JSON formatted data

def process_littering_data(input_csv, output_csv):
    """
    Processes a CSV file containing littering detection results and converts it into a structured format.

    Args:
        input_csv (str): Path to the input CSV file.
        output_csv (str): Path to save the processed annotations.

    Returns:
        None
    """
    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv(input_csv)

    # Initialize an empty list to store processed rows
    rows = []
    for _, row in df.iterrows():  # Iterate over each row in the CSV file
        filename = row["Filename"]  # Extract the filename
        detections = row["Detections"]  # Extract detections column (JSON formatted)

        # Skip empty or invalid detections
        if not isinstance(detections, str) or len(detections.strip()) == 0:
            print(f"Skipping empty detections for {filename}")  # Log skipped entries
            continue  # Move to the next row

        try:
            # Replace single quotes with double quotes and parse JSON
            detections = json.loads(detections.replace("'", '"'))  # Convert improperly formatted JSON to valid JSON
            if "data" in detections and detections["data"]:  # Ensure "data" key exists and is not empty
                for obj in detections["data"][0]:  # Iterate over detected objects in the first detection set
                    label = obj["label"]  # Extract the object label
                    x_min, y_min, x_max, y_max = obj["bounding_box"]  # Extract bounding box coordinates
                    rows.append([filename, label, x_min, y_min, x_max, y_max])  # Append structured data
        except Exception as e:
            print(f"Error parsing detections for {filename}: {e}")  # Log parsing errors
            continue  # Skip to the next row

    # Convert processed data into a pandas DataFrame
    output_df = pd.DataFrame(rows, columns=["Filename", "Label", "x_min", "y_min", "x_max", "y_max"])

    # Save the structured dataset to a CSV file
    output_df.to_csv(output_csv, index=False)

    # Confirm successful processing
    print(f"Training annotations saved to {output_csv}")
