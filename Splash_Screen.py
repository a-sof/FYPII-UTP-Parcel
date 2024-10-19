import streamlit as st
import time

# Set page configuration
st.set_page_config(page_title="UTP ParcelHub", page_icon=":package:", layout="centered")

# Initialize session state to control splash screen visibility
if 'splash_shown' not in st.session_state:
    st.session_state.splash_shown = False  # Track if splash screen has been shown

# Define custom CSS styling for both screens
st.markdown(
    """
    <style>
    .stApp {
        background-color: #F1F0EC;
    }
    .centered-content {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        flex-direction: column;
        text-align: center;
    }
    
    h1 { text-align: center;
        color: #344EAD;
    }
    
    p {
        text-align: center;
        color: #000000;
    }
    

    </style>
    """, 
    unsafe_allow_html=True
)

# Splash screen implementation
placeholder = st.empty()  # Create a placeholder for the splash screen

with placeholder.container():
    # Splash screen content
    st.markdown(
        """
        <div class="centered-content">
            <h1>UTP<br>ParcelHub</h1>
            <p>By student for students</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Keep splash screen for 3 seconds
    time.sleep(3)
    
# Clear the placeholder and display the main content
placeholder.empty()

# Switch to the selected page
st.switch_page("./FeatureOffering")  # Use the exact name without .py

 
