import streamlit as st

st.markdown(
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
    
    .stButton button {
        color: #ffffff;  /* Button text color set to white */
        background-color: #d8a15d;
        display: flex;
        justify-content: center;
        border-radius: 8px;
        padding: 5px 60px;
        font-size: 18px;
        border: 1px solid transparent;  /* Transparent border */
        display: flex;
        justify-content: center;
        margin: auto;  /* Center the button */
    }
    
    .stButton button:hover {
        background-color: #B99058;  /* Change background on hover */
        border: 1px solid white;   /* White border on hover */
        color: white;  /* Keep text color white on hover */
    }    
    </style>
    """,
    unsafe_allow_html=True
)

# Title with new color
st.markdown('<h2>Address</h2>', unsafe_allow_html=True)

# Description text
st.markdown('<p>Kindly select your address for delivery purposes. </p>', unsafe_allow_html=True)

# Define the selectboxes for each V
V1 = st.selectbox("V1 options", ["V1", "V1A", "V1B", "V1C"],index=None)
V2 = st.selectbox("V2 options", ["V2", "V2A", "V2B", "V2C"],index=None)
V3 = st.selectbox("V3 options", ["V3", "V3A", "V3B", "V3C", "V3D", "V3E", "V3F"],index=None)
V4 = st.selectbox("V4 options", ["V4", "V4A", "V4B", "V4C", "V4D", "V4E"],index=None)
V5 = st.selectbox("V5 options", ["V5", "V5A", "V5B", "V5H", "V5K"],index=None)
V6 = st.selectbox("V6 options", ["V6", "V6A", "V6B"],index=None)
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

# Button to switch page
contune_btn = st.button("Next")
if contune_btn:
    # Switch to the selected page
    st.switch_page("./pages/06 - Loading.py")
