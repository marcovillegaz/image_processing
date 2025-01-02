import os
import cv2 as cv
import numpy as np

folder = "Hazeladd"

# Load the image
image = cv.imread(r"Hazeladd\test.jpeg", cv.IMREAD_GRAYSCALE)

# Prints Dimensions of the image
print(image.shape)

# Display the image
cv.imshow("original", image)
cv.waitKey(0)
cv.destroyAllWindows()


# Threshold the image to isolate the white body from the background
_, binary = cv.threshold(image, 200, 255, cv.THRESH_BINARY)

# Display the cropped image
cv.imshow("tresholh", binary)
cv.waitKey(0)
cv.destroyAllWindows()

# Find contours of the white body
contours, _ = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

# Find the largest contour (assuming it is the white body of the material)
largest_contour = max(contours, key=cv.contourArea)

# Get the bounding box of the largest contour
x, y, w, h = cv.boundingRect(largest_contour)
# Crop the image to the white material region
cropped_image = image[y : y + h, x : x + w]

""" # Input: Expected height of the material (in pixels)
expected_height_pixels = 250  # Replace with the known height of the material in pixels

# Crop the image using the bounding box with the expected height
crop_y2 = min(y + expected_height_pixels, image.shape[0])  # Ensure within image bounds
cropped_image = image[y:crop_y2, x : x + w]
 """
# Save or display the cropped image
cv.imshow("Cropped Image", cropped_image)
cv.imwrite(os.path.join(folder, "cropped.jpg"), cropped_image)
cv.waitKey(0)
cv.destroyAllWindows()

# Threshold the image to separate pores (black) from the background (white)
_, binary = cv.threshold(cropped_image, 140, 255, cv.THRESH_BINARY_INV)


# Step 6: Find contours of pores within the cropped image
pore_contours, _ = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

# Step 7: Filter contours by area (to remove noise)
filtered_contours = [
    c for c in pore_contours if 5 < cv.contourArea(c) < 500
]  # Adjust as needed

# Step 8: Draw the filtered contours on the cropped image
output = cv.cvtColor(
    cropped_image, cv.COLOR_GRAY2BGR
)  # Convert to BGR for visualization
cv.drawContours(output, filtered_contours, -1, (0, 255, 0), 1)

# Display or save the result
cv.imshow("Pores Detected", output)
cv.imwrite(os.path.join(folder, "porous.jpg"), output)
cv.waitKey(0)
cv.destroyAllWindows()

""" # Find contours of the pores
contours, _ = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

# draw contours on the original image
image_copy = cropped_image.copy()
cv.drawContours(
    image=image_copy,
    contours=contours,
    contourIdx=-1,
    color=(0, 255, 255),
    thickness=2,
    lineType=cv.LINE_AA,
)

# Optional: Display the binary image with detected contours
contour_image = cv.cvtColor(binary, cv.COLOR_GRAY2BGR)
cv.drawContours(contour_image, contours, -1, (0, 255, 0), 1)

# see the results
cv.imshow("None approximation", contour_image)
cv.waitKey(0)
cv.destroyAllWindows() """

# Output the results
# print(f"Number of pores: {len(contours)}")

print(f"Number of pores: {len(filtered_contours)}")
