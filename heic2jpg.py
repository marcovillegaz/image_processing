""" HEIC to jpg
ref: https://www.youtube.com/watch?v=7Bc3uDi0WHw
"""

import os
from PIL import Image
from pillow_heif import register_heif_opener


input_folder = r"C:\Users\marco\Imágenes\FOTOS EDITADAS\Instagram\javi_heic"
output_folder = r"C:\Users\marco\Imágenes\FOTOS EDITADAS\Instagram\BCN_1"
files = os.listdir(input_folder)

register_heif_opener()

# Convert each file to JPEG
for i, photo in enumerate(files):
    counter = f"({i+1}/" + str(len(files)) + ")"
    print(counter + f" Converting {photo} ... ", end=" ")

    temp_img = Image.open(os.path.join(input_folder, photo))
    temp_img.save(os.path.join(output_folder, photo.replace(".HEIC", ".jpg")))

    print("done")
