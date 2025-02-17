def normalize_bbox(x_min, y_min, x_max, y_max, img_width, img_height):
    """
    Normalize bounding box coordinates to YOLO format (0-1 scale).

    Args:
        x_min (int/float): Minimum x-coordinate of the bounding box.
        y_min (int/float): Minimum y-coordinate of the bounding box.
        x_max (int/float): Maximum x-coordinate of the bounding box.
        y_max (int/float): Maximum y-coordinate of the bounding box.
        img_width (int): Width of the image.
        img_height (int): Height of the image.

    Returns:
        tuple: Normalized (x_center, y_center, width, height), each in the range [0,1].
    """

    # Compute the normalized center of the bounding box
    x_center = (x_min + x_max) / 2 / img_width  # Normalize x-center
    y_center = (y_min + y_max) / 2 / img_height  # Normalize y-center

    # Compute the normalized width and height of the bounding box
    width = (x_max - x_min) / img_width  # Normalize width
    height = (y_max - y_min) / img_height  # Normalize height

    return x_center, y_center, width, height  # Return YOLO-format bounding box
