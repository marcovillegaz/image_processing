"""This scripts organize multiple photos by year and folders. I use it because
i save all the photos of my cellphone by year."""

from utils.images_in_time_interval import images_in_time_interval
from datetime import datetime

import os

years = [2021, 2022, 2023, 2024]
folders = ["Camera", "Instagram", "Screenshots", "WhatsApp Images", "WhatsApp VIdeos"]


def create_folders(destination_folder, years, folders):
    """This fucntion create multiple folder to organize the photos and videos of your cellphone
    by year and the typical foldeer find in your smartphone directories."""

    # Create years folders
    for year in years:
        year_path = os.path.join(destination_folder, str(year))
        os.mkdir(year_path)

        # Create internal folders inside year
        for folder in folders:
            folder_path = os.path.join(year_path, folder)
            os.mkdir(folder_path)

            # WhatsApp diferientiate between sent and recived files
            if folder == "WhatsApp Images" or folder == "WhatsApp Video":
                sent_path = os.path.join(folder_path, "sent")
                os.mkdir(sent_path)


###################################################################################################
years = [2021]
source_folder = r"C:\Users\marco\Escritorio\y9 2019 (viejo)"
destination_folder = r"D:\Fotos"

folders = os.listdir(source_folder)  # List folders in source directory

# create_folders(destination_folder, years, folders)

for year in years:
    year_folder = os.path.join(destination_folder, str(year))

    for folder in folders:
        print(folder.center(50, "-"))
        images_in_time_interval(
            source_folder=os.path.join(source_folder, folder),
            destination_folder=os.path.join(year_folder, folder),
            start_date=datetime(year=year, month=1, day=1),
            end_date=datetime(year=year, month=12, day=31),
            action="Copy",
        )
