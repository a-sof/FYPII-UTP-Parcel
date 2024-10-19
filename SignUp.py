import streamlit as st
import pandas as pd

# CSS styling
st.markdown (
    """
    <style>
    
    .stApp {
        background-color: #F1F0EC;
    }
    
    h2 {
        text-align: left;
        color: #344EAD;      
    }
    
    p {
        text-align: left;
        color: #000000;
    }

    /* Change input fields (name, phoneNum) background and border color */
    input {
        background-color: white;
        border: 1px solid grey;
        color: #000000;
    }

    /* Adjust the button position by adding margin to push it lower */
    .stButton button {
        color: white;
        background-color: #344EAD;
        display: flex;
        justify-content: center;
        border-radius: 8px;
        padding: 5px 60px;
        font-size: 18px;
        border: 1px solid transparent;
        display: flex;
        justify-content: center;
        margin: 20px auto;  /* Adds space between button and input */
    }

    .stButton button:hover {
        background-color: #223372;
        border: 1px solid white;
        color: white;
    }
    
    </style>
    """,
    unsafe_allow_html=True
)

# Title with new color
st.markdown('<h2>Personal Details</h2>', unsafe_allow_html=True)

# Description text
st.markdown('<p>Get yourself started with Parcel Hub! Fill in the details below.</p>', unsafe_allow_html=True)

# Input fields for user data
name = st.text_input("Name", "Enter your full name")
phoneNum = st.text_input("Phone Number", "Enter your Phone Number")
studID = st.text_input("Student ID", "Enter your Student ID" )

# Title with new color
st.markdown('<h2>Address</h2>', unsafe_allow_html=True)

# Description text
st.markdown('<p>Kindly select your address for delivery purposes. </p>', unsafe_allow_html=True)

# Define the selectboxes for each V
V1 = st.selectbox("V1 options", ["Select an option", "V1", "V1A", "V1B", "V1C"], index=0)
V2 = st.selectbox("V2 options", ["Select an option", "V2", "V2A", "V2B", "V2C"], index=0)
V3 = st.selectbox("V3 options", ["Select an option", "V3", "V3A", "V3B", "V3C", "V3D", "V3E", "V3F"], index=0)
V4 = st.selectbox("V4 options", ["Select an option", "V4", "V4A", "V4B", "V4C", "V4D", "V4E"], index=0)
V5 = st.selectbox("V5 options", ["Select an option", "V5", "V5A", "V5B", "V5H", "V5K"], index=0)
V6 = st.selectbox("V6 options", ["Select an option", "V6", "V6A", "V6B"], index=0)
others = st.text_input("Others", "Your preferred address (if not listed)")

# Variable to store the selected value
selected_value = None

# Determine which selectbox was used and set the selected value based on the actual selection
if V1 != "Select an option" and V1:
    selected_value = V1
elif V2 != "Select an option" and V2:
    selected_value = V2
elif V3 != "Select an option" and V3:
    selected_value = V3
elif V4 != "Select an option" and V4:
    selected_value = V4
elif V5 != "Select an option" and V5:
    selected_value = V5
elif V6 != "Select an option" and V6:
    selected_value = V6
elif others:  # In case user types in their custom address
    selected_value = others

# Display the selected value
if selected_value:
    st.write(f"You selected: {selected_value}")

# Button to save the data and switch the page
continue_btn = st.button("Next")

# Saving data to a CSV file
if continue_btn:
    # Data to be saved in CSV
    user_data = {
        "Name": [name],
        "Phone Number": [phoneNum],
        "Student ID": [studID],
        "Address": [selected_value]  # Save the selected address
    }
    
    # Convert the data into a pandas DataFrame
    df = pd.DataFrame(user_data)
    
    # Save the data to CSV file
    df.to_csv('user_data.csv', mode='a', index=False, header=False)
    
    st.success("Details saved successfully!")
    
    # Switch to the next page (assuming page navigation setup)
    st.switch_page("./pages/Address.py")
