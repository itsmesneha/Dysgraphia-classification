import cv2
import os


input_dir = 'input-dataset/Potential Dysgraphia'
output_dir = 'resized-dataset/Potential-resized'

#input_dir = 'input-dataset/Low Potential Dysgraphia'
#output_dir = 'resized-dataset/Low-Potential-resized'

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Define target width and height
target_width = 1300
target_height = 600

# Function to resize images without padding
def resize_without_padding(image_path, target_width, target_height):
    img = cv2.imread(image_path)
    h, w = img.shape[:2]
    aspect_ratio = w / h

    if aspect_ratio > 1:  # Landscape orientation
        new_w = target_width
        new_h = int(new_w / aspect_ratio)
    else:  # Portrait or square orientation
        new_h = target_height
        new_w = int(new_h * aspect_ratio)

    resized_img = cv2.resize(img, (new_w, new_h))

    # Crop the center part of the image to fit the target size
    crop_x = max(0, (new_w - target_width) // 2)
    crop_y = max(0, (new_h - target_height) // 2)
    cropped_img = resized_img[crop_y:crop_y + target_height, crop_x:crop_x + target_width]

    return cropped_img

# Loop over images in input directory
for filename in os.listdir(input_dir):
    if filename.endswith(".jpg"):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)
        resized_img = resize_without_padding(input_path, target_width, target_height)
        cv2.imwrite(output_path, resized_img)

print("Image resizing completed successfully.")
