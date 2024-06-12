import os
from PIL import Image


def get_image_dpi(image_path):
    """
    Get the DPI of an image.

    :param image_path: Path to the image file.
    :return: DPI as a tuple (x_dpi, y_dpi).
    """
    with Image.open(image_path) as img:
        dpi = img.info.get("dpi", (0, 0))
    return dpi


def check_images_dpi(folder_path, dpi_limit):
    """
    Check the DPI of all images in a folder and identify those below the specified DPI limit.

    :param folder_path: Path to the folder containing images.
    :param dpi_limit: Minimum acceptable DPI.
    :return: List of image file names with DPI below the limit.
    """
    images_below_dpi = []
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(("png", "jpg", "jpeg", "tiff", "bmp", "gif")):
            image_path = os.path.join(folder_path, filename)
            dpi = get_image_dpi(image_path)
            if dpi[0] < dpi_limit or dpi[1] < dpi_limit:
                images_below_dpi.append((filename, dpi))
    return images_below_dpi


# Example usage:
folder_path = r"dpi_test"
dpi_limit = 700  # Set your DPI limit here

images_below_dpi = check_images_dpi(folder_path, dpi_limit)
print("Images with DPI below the limit:")
for image in images_below_dpi:
    print(f"Image: {image[0]}, DPI: {image[1]}")
