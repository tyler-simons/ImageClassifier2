# Dooders Image Classification App

This is a Streamlit app that allows you to classify images and record their classifications to a CSV file.

## Requirements

We need a venv. Install and source a virtual enviornment  

`python3 -m venv venv`
  
`source venv/bin/activate`

Before running the app, you need to have the streamlit requirements installed
You can install them by running:  

`pip install -r requirements.txt`

## Usage

1. Clone the repository and navigate to the project folder.
2. Create a `./images` folder and add your images to it. 
3. Run the app by running the following command in your terminal:
   `streamlit run streamlit_app.py`
4. In the sidebar, enter the folder path where your images are located.
5. The app will load the images and display them one by one.
6. Click one of the classification buttons ('f', 'p', or 'q') below the image to classify it.
7. The app will record the image classification to a CSV file and proceed to the next image.
8. The recorded classifications will be displayed in a data table on the right-hand side of the app, which you can edit and save back to the CSV file.

## Notes

- The recorded classifications are stored in a CSV file named `classifications.csv`, which will be created in the project folder if it doesn't exist.
- The app will display a "No more images to classify" message and stop when all the images have been classified.
- If you make changes to the CSV file while the app is running in the data editor section, click the "Save edited CSV file" button to save the changes and refresh the app.

Enjoy!
