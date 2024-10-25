import streamlit as st

st.set_page_config(page_title="Home", layout="wide")

# CSS styles for custom buttons and layout
st.markdown("""
    <style>
    .stApp {
        background-color: #F1F0EC;
    }
    
    /* Custom styles for the button */
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
    }
    
    .admin-btn {
        background-color: #4A68CC;
        color: white;
    }

    .stButton > button:hover {
        opacity: 0.9;
    }
    
    </style>
""", unsafe_allow_html=True)

# Layout: Two columns for the buttons
col1, col2 = st.columns([1, 1])

# Adding buttons with actions to navigate to different pages
with col1:
    # Using st.button for the interaction
    student_btn = st.button('UTP Student & Staff')
    if student_btn:
        # Logic to navigate to the "Sign Up" page
        st.switch_page("./pages/Home.py")
    
with col2:   
    st.image("C:/Users/Ainin Sofiya/Documents/UTP/YEAR 3/FYP I/Images/cardbox box/cardboxy.png", width=150)
    
staff_btn_clicked = st.button('Parcel Hub / Bro Staff')
if staff_btn_clicked:
    # Logic to navigate to the "Admin" page
    st.write("Navigating to the Admin page...")
    st.switch_page("admin")  # Replace with correct page name
