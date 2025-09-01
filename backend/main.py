import cv2
import os
from ultralytics import YOLO
import easyocr

# Load YOLO door detection model (load once for performance)
door_model = YOLO("runs/detect/door_detector8/weights/best.pt")

# Initialize EasyOCR reader (English)
reader = easyocr.Reader(['en'])

def analyze_floor_plan(image_path, target_labels):
    """
    Detects door symbols and highlights specific text labels in a floor plan image.

    Args:
        image_path (str): Path to the floor plan image.
        target_labels (list): List of text labels to highlight, e.g. ["STR", "WASH", "HALL"]

    Returns:
        result_img_path (str): Path to annotated image.
        door_count (int): Total number of detected door symbols.
        detected_labels (list): List of found labels.
    """

    # Load image
    image = cv2.imread(image_path)

    # -------------------------------
    # STEP 1: Door Detection using YOLO
    # -------------------------------
    door_results = door_model.predict(
        source=image_path,
        conf=0.4,
        device="cuda" if cv2.cuda.getCudaEnabledDeviceCount() > 0 else "cpu",
        verbose=False
    )

    door_count = len(door_results[0].boxes)

    # -------------------------------
    # STEP 2: Text Detection using EasyOCR
    # -------------------------------
    results = reader.readtext(image)
    detected_labels = []

    for (bbox, text, prob) in results:
        text_upper = text.upper().strip()
        if text_upper in [label.upper() for label in target_labels]:
            detected_labels.append(text_upper)

            # Draw rectangle around detected label
            (top_left, top_right, bottom_right, bottom_left) = bbox
            top_left = tuple(map(int, top_left))
            bottom_right = tuple(map(int, bottom_right))

            cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)
            cv2.putText(image, text_upper, (top_left[0], top_left[1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # Save annotated image to output folder
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "annotated_floorplan.jpg")
    cv2.imwrite(output_path, image)

    return output_path, door_count, detected_labels
