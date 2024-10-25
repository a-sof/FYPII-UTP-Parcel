import streamlit as st
import pandas as pd

# Set page title and layout
st.set_page_config(page_title="Parcel Collection Admin", layout="wide")

# Function to load CSV file (parcel data)
def load_parcel_data(file_path="parcel_data.csv"):
    try:
        return pd.read_csv(file_path, dtype={"Phone Number": str})  # Ensure Phone Number is read as string
    except FileNotFoundError:
        return pd.DataFrame(columns=["Phone Number", "Tracking Number", "Location"])

# Function to save parcel data to CSV
def save_parcel_data(data, file_path="parcel_data.csv"):
    data.to_csv(file_path, index=False)

# Function to add new parcel to the CSV file
def add_new_parcel(phone_num, tracking_num, location):
    df = load_parcel_data()
    new_data = pd.DataFrame({"Phone Number": [phone_num], "Tracking Number": [tracking_num], "Location": [location]})
    
    # Concatenate the new data with the existing data
    df = pd.concat([df, new_data], ignore_index=True)
    
    # Save the updated DataFrame to the CSV file
    save_parcel_data(df)
    st.success(f"Parcel added successfully! Tracking Number: {tracking_num}")

# Function to check parcel details for collection
def collect_parcel(phone_num=None, tracking_num=None):
    df = load_parcel_data()
    
    if phone_num:
        result = df[df["Phone Number"] == phone_num]  # Phone number comparison as a string
    elif tracking_num:
        result = df[df["Tracking Number"] == tracking_num]
    else:
        st.warning("Please enter either Phone Number or Tracking Number.")
        return
    
    if not result.empty:
        st.success(f"Parcel found! Location: {result.iloc[0]['Location']}")
        st.write(result)
    else:
        st.error("No parcel found with the provided details.")

# Admin Page Layout
st.title("Parcel Collection System - Admin Page")
st.write("Choose an action below:")

# Two columns for the buttons
col1, col2 = st.columns(2)

# Button to show the add new parcel form
with col1:
    if st.button("Input New Parcel"):
        st.session_state['show_add_parcel_form'] = True
        st.session_state['show_collect_parcel_form'] = False

# Button to show the collect parcel form
with col2:
    if st.button("Parcel Collection"):
        st.session_state['show_add_parcel_form'] = False
        st.session_state['show_collect_parcel_form'] = True

# Add new parcel form
if st.session_state.get('show_add_parcel_form', False):
    st.subheader("Add New Parcel")
    
    # Input fields for parcel details
    phone_num = st.text_input("Phone Number", "")
    tracking_num = st.text_input("Parcel Tracking Number", "")
    location = st.text_input("Location to Store Parcel", "")
    
    # Button to save the parcel details
    if st.button("Submit New Parcel"):
        if phone_num and tracking_num and location:
            add_new_parcel(phone_num, tracking_num, location)
            st.session_state['parcel_data_submitted'] = True
        else:
            st.warning("Please fill all the fields.")

# Collect parcel form
if st.session_state.get('show_collect_parcel_form', False):
    st.subheader("Collect Parcel")
    
    # Input fields for client details (Phone Number or Tracking Number)
    option = st.radio("Search by", ("Phone Number", "Parcel Tracking Number"))
    
    if option == "Phone Number":
        phone_num_input = st.text_input("Enter Phone Number", "")
        if st.button("Collect by Phone Number"):
            if phone_num_input:
                collect_parcel(phone_num=phone_num_input)
            else:
                st.warning("Please enter the Phone Number.")
    else:
        tracking_num_input = st.text_input("Enter Tracking Number", "")
        if st.button("Collect by Tracking Number"):
            if tracking_num_input:
                collect_parcel(tracking_num=tracking_num_input)
            else:
                st.warning("Please enter the Tracking Number.")
