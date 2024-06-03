import os
import shutil
from datetime import datetime
from PIL import Image
from PIL import ExifTags


def images_between_dates(
    source_folder,
    destination_folder,
    start_date,
    end_date,
    action="Copy",
):

    # Create destintation folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # List filenames in source folder
    for filename in os.listdir(source_folder):

        if filename.lower().endswith((".jpg", ".jpeg")):
            # print(filename)
            filepath = os.path.join(source_folder, filename)
            image = Image.open(filepath)

            # Get the metadata and translate the EXIF code into a dictionary
            exif = {}
            if image._getexif() is not None:
                for tag, value in image._getexif().items():
                    if tag in ExifTags.TAGS:
                        exif[ExifTags.TAGS[tag]] = value
            # print(exif)

            if "DateTime" in exif:
                image_date = exif["DateTime"]  # Extract date from exif dictionary
                image_date = image_date.split(" ")  # Split date and time
                image_date = image_date[0].replace(":", "-")  # replace delimiter

                print(f"{filename}\tDatetime: {image_date}")

                # Create datetime object
                image_date = datetime.strptime(image_date, r"%Y-%m-%d")

                """ # Move/Copy the image that meet the time interval
                if start_date <= image_date <= end_date:
                    if action == "Copy":
                        print(f"\tCopyng {filename} to destination folder")
                        shutil.copy(filepath, destination_folder)

                    elif action == "Move":
                        print(f"\tMoving {filename} to destination folder")
                        shutil.move(filepath, destination_folder) """
