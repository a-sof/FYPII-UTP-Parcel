import streamlit as st
import os
from PIL import Image

st.markdown("""
    <style>

/* Set the background color of the main container */
        .main {
            background-color: white;
            padding: 10px;
        }
        
        /* Global text color to black */
        h1, h2, h3, h4, h5, h6, p, label, span {
            color: #000000 !important;
        }
</style> 
""", unsafe_allow_html=True)

# Folder where images are stored
UPLOAD_DIR = "uploaded_images"
ANNOUNCEMENT_FILE = "announcement.txt"


st.title("Information")

# Display the latest announcement
st.subheader("Important Announcement")

if os.path.exists(ANNOUNCEMENT_FILE):
    with open(ANNOUNCEMENT_FILE, "r") as f:
        announcement = f.read()
    if announcement:
        st.write(announcement)
    else:
        st.write("No announcements at the moment.")
else:
    st.write("No announcement posted yet.")


# Check if the folder has any images
if os.path.exists(UPLOAD_DIR):
    image_files = [f for f in os.listdir(UPLOAD_DIR) if f.endswith(('.png', '.jpg', '.jpeg'))]

    if image_files:
        for image_file in image_files:
            image = Image.open(os.path.join(UPLOAD_DIR, image_file))
            st.image(image, use_column_width=True)
    else:
        st.write("No images uploaded yet.")
else:
    st.write("No images folder found.")

