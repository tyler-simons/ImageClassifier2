import os
import pandas as pd
import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")


def classify_image(image_path, image_index, classification, csv_file):
    """Classify an image and record its classification to a CSV file"""
    with open(csv_file, "a") as f:
        image_basename = os.path.basename(image_path)
        f.write(f"{image_index},{image_basename},{classification}\n")


st.title("Dooders Image Classification App")

# Sidebar for folder selection
folder_path = st.sidebar.text_input("Enter folder path")

# Load the images in the folder
if folder_path:
    images = sorted(os.listdir(folder_path))
    images = [image for image in images if image.endswith(".jpg") or image.endswith(".png")]
    st.write(f"Total number of images found: {len(images)}")

    # Load the recorded classifications from the CSV file
    csv_file = "classifications.csv"
    if os.path.exists(csv_file):
        df = pd.read_csv(csv_file, names=["Index", "Filepath", "Classification"])
        if df.empty:
            last_index = 0
        else:
            last_index = df["Index"].max() + 1
        classifications = dict(zip(df["Index"], df["Classification"]))
    else:
        last_index = 0
        classifications = {}
        df = pd.DataFrame(columns=["Index", "Filepath", "Classification"])
        df.to_csv(csv_file, index=False, header=False)

    # Define the two columns
    col1, col2 = st.columns(2)

    # Loop through the images and display them one by one
    image_index = last_index
    col1.write(f"Current image index: {image_index}")

    # Display the current image
    with col1:
        if image_index >= len(images):
            st.title("No more images to classify")
            st.write(df)
            st.balloons()
            st.stop()
        image_file = images[image_index]
        image_path = os.path.join(folder_path, image_file)
        st.image(Image.open(image_path), caption=image_file, use_column_width=True)

        # Display the classification buttons
        cola, colb, colc = st.columns(3)
        classify_f = cola.button("Classify as 'f'")
        classify_p = colb.button("Classify as 'p'")
        classify_q = colc.button("Classify as 'q'")

        if classify_f:
            classifications[image_index] = "f"
            classify_image(image_path, image_index, "f", csv_file)
        elif classify_p:
            classifications[image_index] = "p"
            classify_image(image_path, image_index, "p", csv_file)
        elif classify_q:
            classifications[image_index] = "q"
            classify_image(image_path, image_index, "q", csv_file)

        # Increment to the next image when classified
        if classify_f or classify_p or classify_q:
            image_index += 1
            st.experimental_rerun()

    # Display the recorded classifications in the second column
    with col2:
        st.write("Recorded classifications")
        df = pd.read_csv(csv_file, names=["Index", "Filepath", "Classification"])
        df = st.experimental_data_editor(df)
        overwrite = st.button("Save edited CSV file")
        if overwrite:
            df.to_csv(csv_file, index=False, header=False)
            st.experimental_rerun()
