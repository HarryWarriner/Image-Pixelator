import cv2

def pixelate_image(image_path, pixel_size=10):
    # Read the image
    image = cv2.imread(image_path)

    # Get image dimensions
    height, width = image.shape[:2]

    # Resize image to small size
    small_image = cv2.resize(image, (width // pixel_size, height // pixel_size), interpolation=cv2.INTER_LINEAR)

    # Resize back to original size
    pixelated_image = cv2.resize(small_image, (width, height), interpolation=cv2.INTER_NEAREST)

    return pixelated_image

# Load and pixelate an image
image_path = "Cookie1.jpg"
pixelated = pixelate_image(image_path, pixel_size=5)

# Show and save the result
cv2.imshow("Pixelated Image", pixelated)
cv2.imwrite("pixelated_output.jpg", pixelated)
cv2.waitKey(0)
cv2.destroyAllWindows()
