import streamlit as st

st.set_page_config(page_title="Home", layout="wide")

# Custom CSS for styling the page elements 
st.markdown(
    """
    <style>
        .stApp {
            background-color: white;
        }
        
        .header {
            font-size: 30px !important;
            font-weight: bold;
            color: #091F5B;
        }
        
        .stButton > button {
        background-color: #091F5B;
        color: white;
        font-weight: bold;
        font-size: 20px;
        width: 100%;  
        height: 90px;  
        padding: 10px;  
        border-radius: 10px; 
        cursor: pointer; 
        border: none;
        
        .notifBtn, .infoBtn, .deliveryBtn, .parcelBtn, .helpBtn {
            font-size: 18px;
            font-weight: bold;
            color: #091F5B;
            width: 100%;
            height: 90px;
            padding: 10px;
            border-radius: 10px;
            cursor: pointer;
            border: none;
        }
        
        .notifBtn {
            font-size: 30px;
            color: #344EAD; 
            background: transparent;
        }

        .infoBtn, .deliveryBtn {
            background-color: #F0F0F0;
            color: #091F5B;
        }

        .parcelBtn {
            background-color: #091F5B;
            color: white;
        }
        
        .helpBtn {
            background-color: #B99058;
            color: white;
        }

        .text {
            color: black;
        }
    </style>
    """, unsafe_allow_html=True
)

left_column, right_column = st.columns([1, 1])

with left_column: 
    # Main greeting and notice section
    st.markdown('<p class="header">Hello, Sofiya!</p>', unsafe_allow_html=True)

st.image("C:/Users/Ainin Sofiya/Documents/UTP/YEAR 3/FYP I/Images/holiday_notice_image.png.png")

st.markdown('<p class="subheader">Current Address:</p>', unsafe_allow_html=True)

# Create columns for buttons
left_col, right_col = st.columns([1, 1])

# Handling button clicks for page navigation
with left_col:    
    # Create Information button using st.button and switch_page
    if st.button("Information", key="infoBtn"):
        st.switch_page("./pages/Information.py")  # Switch to the information page

with right_col:    
    # Create Delivery button using st.button and switch_page
    if st.button("Delivery", key="deliveryBtn"):
        st.switch_page("./pages/Delivery.py")  # Switch to the delivery page

# Full-width buttons for parcel availability and help
if st.button("Parcel Availability", key="parcelBtn"):
    st.switch_page("10 - Information Page")  # Switch to the parcel availability page

if st.button("Need Help? Reach out to us.", key="helpBtn"):
    st.switch_page("./pages/Information.py")  # Switch to the help page
