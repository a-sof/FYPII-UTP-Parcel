import streamlit as st

# Set page layout to wide
st.set_page_config(layout="wide")

# CSS styles for custom buttons and layout
st.markdown("""
    <style>
    .button-container {
        display: flex;
        justify-content: center;
        margin-top: 100px;
    }
    
    .button {
        display: inline-flex;
        align-items: center;
        padding: 30px 40px;
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        border-radius: 15px;
        cursor: pointer;
        margin-right: 20px;
        border: none;
    }
    
    .student-btn {
        background-color: #002F6C;  /* Navy blue */
        color: white;
    }
    
    .staff-btn {
        background-color: #4A68CC;  /* Lighter blue */
        color: white;
    }
    
    .student-btn:hover, .staff-btn:hover {
        opacity: 0.9;
    }
    
    .icon {
        width: 40px;
        height: 40px;
        margin-left: 10px;
    }
    
    </style>
""", unsafe_allow_html=True)

# Layout: Two columns for the buttons
col1, col2 = st.columns([1, 1])

# Adding buttons with actions to navigate to different pages
with col1:
    if st.button('UTP Student & Staff'):
        # Logic to navigate to the "Sign Up" page
        st.write("Navigating to the Sign Up page...")
        st.switch_page("./pages/04 - Sign.py")
        st.experimental_rerun()  # Assuming 'sign_up.py' is the page to navigate to
        # You should configure the correct page link in your app's multipage structure

with col2:
    if st.button('Parcel Hub / Bro Staff'):
        # Logic to navigate to the "Admin" page
        st.write("Navigating to the Admin page...")
        st.experimental_rerun()  # Assuming 'admin.py' is the page to navigate to
        # You should configure the correct page link in your app's multipage structure

# You can add logic here for additional actions or updates.
st.write("Click on one of the buttons above to proceed!")

