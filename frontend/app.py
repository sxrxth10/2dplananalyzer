import streamlit as st
import tempfile
from backend import analyze_floor_plan

# Streamlit page config
st.set_page_config(page_title="Floor Plan Analyzer", layout="centered")

st.title("🏠 Floor Plan Analyzer")
st.write("Upload a floor plan image to detect **doors** and highlight selected **text labels**.")

# Image upload
uploaded_file = st.file_uploader("Upload Floor Plan Image", type=["jpg", "jpeg", "png"])

# Input for target labels
target_labels_input = st.text_input(
    "Enter labels to highlight (comma-separated):",
    placeholder="Example: STR, BEDROOM, HALL"
)

# Analyze button
if uploaded_file and target_labels_input:
    target_labels = [label.strip() for label in target_labels_input.split(",") if label.strip()]

    if st.button("Analyze Floor Plan"):
        # Save uploaded file to a temporary path
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name

        # Run analysis
        with st.spinner("Analyzing floor plan... ⏳"):
            result_img_path, door_count, detected_labels = analyze_floor_plan(tmp_path, target_labels)

        # Show results
        st.success(f"✅ Analysis Complete!")

        st.subheader("🔹 Results")
        st.write(f"**Total Doors Detected:** {door_count}")
        st.write(f"**Detected Labels:** {', '.join(detected_labels) if detected_labels else 'None'}")

        # Display annotated image
        st.image(result_img_path, caption="Annotated Floor Plan", use_column_width=True)

else:
    st.info("👆 Upload an image and enter labels to highlight before running analysis.")
