Floor Plan Analyzer — Door & Label Detection
📌 Overview

This project analyzes architectural floor plan images and performs:

Door detection & counting using YOLOv8

Text label detection & highlighting using EasyOCR

Interactive UI with Streamlit

It is designed to help  extracting structural details from complex floor plans.


✨ Features

✅ Upload a floor plan image via the Streamlit UI
✅ Uses YOLOv8 for door detection
✅ Uses EasyOCR for text label recognition
✅ Highlights detected labels on the image
✅ Displays total door count for each floor plan
✅ Simple, standalone backend using Python functions
✅ Streamlit frontend for user interaction


🛠️ Tech Stack

Language-	Python 3.10+
Door Detection-	Ultralytics YOLOv8
Text Detection-	EasyOCR
Backend-	Python (no API required)
Frontend-	Streamlit
Visualization-	OpenCV, PIL
Deployment-	Streamlit 




📂 Dataset

Total Images: ~200
(40 original + augmented)

Augmentation Techniques:

Horizontal flip
Vertical flip
90° & 180° rotation
Labeling Tool: LabelImg
 (YOLO format)


Note 
Its not yet a effitient system due to the availability of datasets. Yet you can test the trained model by running the testing.ipynb notebook. And also can run the UI by installing the required libraries mentioned in the requirements.txt file.