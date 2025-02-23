# import cv2
# import os
#
# # Specify the path to your image
# image_path = r'C:\Users\varsh\PycharmProjects\facedetection\Imagesof\ramya.jpeg'
#
# # Check if the file exists
# if not os.path.exists(image_path):
#     print(f"Error: The file {image_path} does not exist.")
# else:
#     # Load the image using OpenCV
#     imgRamya = cv2.imread(image_path)
#
#     # Check if the image was loaded correctly
#     if imgRamya is None or imgRamya.size == 0:
#         print(f"Error: Failed to load the image {image_path}.")
#     else:
#         # Convert the image from BGR to RGB
#         try:
#             imgRamya_rgb = cv2.cvtColor(imgRamya, cv2.COLOR_BGR2RGB)
#             print("Image loaded and converted successfully.")
#         except cv2.error as e:
#             print(f"Error: {e}")


import cv2
import os

# Path to the image
image_path = r'Imagesof/ramya.jpeg'

# Check if the file exists
if not os.path.isfile(image_path):
    print(f"Error: The file {image_path} does not exist.")
else:
    # Load the image
    imgRamya = cv2.imread(image_path)

    # Check if the image was loaded successfully
    if imgRamya is None:
        print(f"Error: Could not load the image from {image_path}.")
    else:
        # Original image dimensions
        original_height, original_width = imgRamya.shape[:2]

        # Desired display size
        new_width, new_height = 500, 500

        # Resize the image
        resized_img = cv2.resize(imgRamya, (new_width, new_height))

        # Example data for fLoc (should be a list of tuples with coordinates from the original image)
        fLoc = [(50, 100, 150, 200)]  # (top, right, bottom, left)

        # Calculate scale factors
        x_scale = new_width / original_width
        y_scale = new_height / original_height

        # Scale the coordinates
        scaled_fLoc = [(int(top * y_scale), int(right * x_scale), int(bottom * y_scale), int(left * x_scale)) for (top, right, bottom, left) in fLoc]

        # Draw rectangles using scaled coordinates
        for (top, right, bottom, left) in scaled_fLoc:
            cv2.rectangle(resized_img, (left, top), (right, bottom), (255, 0, 255), 2)

        # Display the resized image with the rectangle
        cv2.imshow('Resized Image with Rectangle', resized_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

