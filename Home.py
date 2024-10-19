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
        
        .notifBtn {
            font-size: 30px; 
            color: #344EAD; /* Notification icon color */
            display: flex; /* Use flexbox */
            justify-content: flex-end; /* Align the icon to the right */
            background: transparent; /* Transparent background */
            border: none; /* No border */
            cursor: pointer; /* Cursor style */
            width: 100%;
        }

        .subheader {
            font-size: 20px !important;
            font-weight: bold;
            color: #344EAD;
            text-align: left; 
            margin-left: 10px;
        }

        .infoBtn {
            background-color: #F0F0F0;
            color: #091F5B;
            font-weight: bold;
            font-size: 18px;
            width: 100%;  
            height: 90px;  
            padding: 10px;  
            border-radius: 10px; 
            cursor: pointer; 
            border: none; 
        }

        .deliveryBtn {
            background-color: #F0F0F0;
            color: #091F5B;
            font-weight: bold;
            font-size: 18px;
            width: 100%;  
            height: 90px;  
            padding: 10px;  
            border-radius: 10px; 
            cursor: pointer; 
            border: none; 
        }

        .parcelBtn {
            background-color: #091F5B;
            color: white;
            font-weight: bold;
            font-size: 18px;
            width: 100%;  
            height: 90px;  
            padding: 10px;  
            border-radius: 10px; 
            cursor: pointer; 
            border: none; 
        }
        
        .helpBtn {
            background-color: #B99058;
            color: white;
            font-weight: bold;
            font-size: 18px;
            width: 100%;  
            height: 90px;  
            padding: 10px;  
            border-radius: 10px; 
            cursor: pointer; 
            border: none; 
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

with right_column:
    # Create a notification button using the correct class
    if st.markdown('<button class="notifBtn" onclick="window.location.href=\'./pages/09 - Delivery.py\'">🔔</button>', unsafe_allow_html=True):
        pass

st.image("C:/Users/Ainin Sofiya/Documents/UTP/YEAR 3/FYP I/Images/holiday_notice_image.png.png")

st.markdown('<p class="subheader">Current Address:</p>', unsafe_allow_html=True)

# Create columns for buttons
left_col, right_col = st.columns([1, 1])

with left_col:    
    # Create the Information button using HTML
    if st.markdown('<button class="infoBtn" onclick="window.location.href=\'./pages/10 - Information Page.py\'">Information</button>', unsafe_allow_html=True):
        pass

with right_col:    
    # Create the Delivery button using HTML
    if st.markdown('<button class="deliveryBtn" onclick="window.location.href=\'./pages/09 - Delivery.py\'">Delivery</button>', unsafe_allow_html=True):
        pass

# Create a full-width button for parcel availability using HTML
if st.markdown('<button class="parcelBtn" onclick="window.location.href=\'./pages/10 - Information Page.py\'">Parcel Availability</button>', unsafe_allow_html=True):
    pass

if st.markdown('<button class="helpBtn" onclick="window.location.href=\'./pages/10 - Information Page.py\'">Need Help? <br> Reach out to us.</button>', unsafe_allow_html=True):
    pass
