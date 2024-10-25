import streamlit as st
import os

# Set up a folder to store uploaded images and announcement text
UPLOAD_DIR = "uploaded_images"
ANNOUNCEMENT_FILE = "announcement.txt"

if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

st.title("Admin: Upload Images, Post Announcement, and Manage Content")

# File uploader for uploading images
uploaded_files = st.file_uploader(
    "Choose images to upload", accept_multiple_files=True, type=["png", "jpg", "jpeg"]
)

if uploaded_files:
    for uploaded_file in uploaded_files:
        # Save each uploaded image to the 'uploaded_images' folder
        with open(os.path.join(UPLOAD_DIR, uploaded_file.name), "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        st.success(f"Uploaded {uploaded_file.name} successfully!")

# Text box for admin to enter an important announcement
st.subheader("Post an Important Announcement")
announcement = st.text_area("Write your announcement here:")

if st.button("Post Announcement"):
    # Save the announcement to a text file
    with open(ANNOUNCEMENT_FILE, "w") as f:
        f.write(announcement)
    st.success("Announcement posted successfully!")

# Option to delete the previous announcement
if os.path.exists(ANNOUNCEMENT_FILE):
    st.subheader("Manage Announcement")
    with open(ANNOUNCEMENT_FILE, "r") as f:
        current_announcement = f.read()
    
    if current_announcement:
        st.write("Current Announcement:")
        st.write(current_announcement)
        
        # Button to delete the announcement
        if st.button("Delete Announcement"):
            os.remove(ANNOUNCEMENT_FILE)
            st.success("Announcement deleted successfully!")
    else:
        st.write("No announcement posted yet.")

# Display and manage uploaded images
st.subheader("Manage Uploaded Images")

if os.path.exists(UPLOAD_DIR):
    image_files = [f for f in os.listdir(UPLOAD_DIR) if f.endswith(('.png', '.jpg', '.jpeg'))]

    if image_files:
        for image_file in image_files:
            st.write(f"Image: {image_file}")
            st.image(os.path.join(UPLOAD_DIR, image_file), caption=image_file, use_column_width=True)
            
            # Button to delete each image
            if st.button(f"Delete {image_file}", key=image_file):
                os.remove(os.path.join(UPLOAD_DIR, image_file))
                st.success(f"Deleted {image_file} successfully!")
    else:
        st.write("No images uploaded yet.")
else:
    st.write("No images folder found.")
