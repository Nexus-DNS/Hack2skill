Hack4change2024

Problem Statement : Difficulty in Early Detection of Crop Health Issues
.
.
.
OUR SOLUTION
.
.
.
🌱 Crop Health Analyzer 📸
This Python project provides a basic crop health analysis using regular JPEG images. It leverages the Excess Green Index (ExG) as a proxy for NDVI to estimate plant health and visually highlights potentially unhealthy areas.

🚀 Getting Started
Prerequisites

Python (3.x recommended)
OpenCV (pip install opencv-python)
NumPy (pip install numpy)
Matplotlib (pip install matplotlib)
Prepare Your Image

Place your crop image (JPEG format) in the same directory as this script, or update the image_path variable in the code with the correct file path.
Run the Code

Execute the Python script (python your_script_name.py)
View the Results

The script will print the estimated percentage of healthy and unhealthy areas in the console.
A Matplotlib window will display the analyzed image, highlighting potentially unhealthy areas with black borders.
💡 How It Works
Calculates ExG: The script calculates the Excess Green Index (ExG) from the RGB channels of the image as a proxy for NDVI.
Thresholding: It applies a threshold to the ExG values to identify potentially unhealthy areas.
Contour Detection: The script detects the boundaries (contours) of these unhealthy areas.
Visualization: Finally, it overlays black borders around the detected unhealthy regions on the original image.
⚠️ Limitations
Accuracy: The analysis relies on ExG as an NDVI proxy, which might not be as accurate as true multispectral analysis.
Environmental Factors: Factors like shadows, soil color, and other plant features can influence the results.
Limited Scope: This approach only focuses on overall greenness and might not detect specific pests, diseases, or nutrient deficiencies.
✨ Future Enhancements
Advanced Analysis: Incorporate additional color indices, texture analysis, or machine learning for a more comprehensive assessment.
User Interface: Develop a user-friendly interface for interactive visualization and data management.
Multispectral Integration: If possible, adapt the code to work with true multispectral data for more accurate results.

Happy farming and coding!! 👨‍🌾👩‍🌾 💻
