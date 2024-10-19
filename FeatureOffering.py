import streamlit as st 
import time    
    
    
# Define custom CSS styling for both screens
st.markdown(
    """
    <style>
    .stApp {
        background-color: #F1F0EC;
    }
        
    h2 {
        text-align: center;
        color: #1c53d6;
    }
    
    p {
        text-align: center;
        color: #000000;
    }
    
    .stButton button {
        color: white;  /* Button text color set to white */
        background-color: #344EAD;
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
        background-color: #223372;  /* Change background on hover */
        border: 1px solid white;   /* White border on hover */
        color: white;  /* Keep text color white on hover */
    }
    
</style>
    """, 
    unsafe_allow_html=True
)
    
    # Screen 2: Main Content
with st.container():
    
    # Centered container
    st.markdown('<div class="centered-content">', unsafe_allow_html=True)

    left_co, cent_co,last_co = st.columns(3)
    with cent_co:
        st.image("C:/Users/Ainin Sofiya/Documents/UTP/YEAR 3/FYP I/Images/savetime2 again.png", width=200)
    
    # Image container for centering
    st.markdown('<div class="image-container">', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # Title with new color
    st.markdown('<h2>Save Time and Energy!</h2>', unsafe_allow_html=True)

    # Description text
    st.markdown('<p>Get your parcels delivered in a day with our fast delivery service</p>', unsafe_allow_html=True)

    # Pagination dots
    st.markdown('<p>•  •</p>', unsafe_allow_html=True)

    # Button to switch page
    continue_btn = st.button("Continue")
    if continue_btn:
        # Switch to the selected page
        st.switch_page("SignUp")
        
    st.markdown('</div>', unsafe_allow_html=True)
