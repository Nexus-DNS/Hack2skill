import cv2
import numpy as np
import matplotlib.pyplot as plt

def analyze_crop_health_from_jpeg(image_path, threshold=120):
    """Analyzes a JPEG image and outlines potentially unhealthy areas with black borders."""
    image = cv2.imread(image_path)

    if image is None:
        raise FileNotFoundError(f"Image not found at: {image_path}")

    # Calculate Excess Green Index (ExG) as a proxy for NDVI
    red_band = image[:, :, 2]
    green_band = image[:, :, 1]
    blue_band = image[:, :, 0]
    exg = 2 * green_band - red_band - blue_band

    # Normalize ExG
    exg = (exg - exg.min()) / (exg.max() - exg.min())

    # Threshold to identify unhealthy areas
    unhealthy_mask = exg < threshold / 255.0

    # Find contours (outlines) of unhealthy areas
    contours, _ = cv2.findContours(unhealthy_mask.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw black borders around the contours
    result_image = image.copy()
    cv2.drawContours(result_image, contours, -1, (0, 0, 0), thickness=2)  # Black color, thickness=2

    # Display the result
    plt.figure(figsize=(10, 8))
    plt.imshow(cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB))
    plt.title('Estimated Crop Health with Unhealthy Areas Outlined')
    plt.axis('off')
    plt.show()


# Main Execution

# Get image path
image_path = r'C:\Users\kiran\OneDrive\Desktop\Crop_Drone\image\Crop4.jpg'  # Replace with your image path

# Analyze the image
analyze_crop_health_from_jpeg(image_path)
