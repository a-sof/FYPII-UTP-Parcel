import streamlit as st

# Set page layout to center content
st.set_page_config(layout="centered", page_title="Delivery", page_icon="📦")

# Custom CSS to style the page
st.markdown("""
    <style>
        /* Set the background color of the main container */
        .main {
            background-color: white;
            padding: 10px;
        }
        
        /* Global text color to black */
        h1, h4, h5, h6, p, label, span {
            color: #000000 !important;
        }
        
        h2, h3{
            color: #344EAD;
        }

        /* Reduce gap between radio buttons and subheaders */
        div[role='radiogroup'] {
            margin-top: -30px; /* Adjust the top margin to reduce space */
        }

        /* Styling the close button */
        .close-button {
            display: flex;
            justify-content: flex-end;
            margin-bottom: 10px;
        }
        .close-button button {
            background-color: #d8a15d;
            color: white;
            border: none;
            font-size: 1.5rem;
            border-radius: 50%;
            cursor: pointer;
            width: 40px;
            height: 40px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
            transition: background-color 0.3s ease;
        }
        .close-button button:hover {
            background-color: #c2924d;
        }
        
        /* Set the radio button text color to black */
        div[role='radiogroup'] label {
            font-family: 'Arial', sans-serif;
            color: #000000;
        }
        
        /* Customize the st.date_input fields */
        input[type='date'] {
            background-color: white !important;
            color: white !important;
            border: 1px solid #d8a15d;
            padding: 5px;
            border-radius: 5px;
        }
        
        /* Styling the Next button */
        .next-button {
            background-color: #d8a15d;
            color: white;
            border: none;
            padding: 10px 25px;
            font-size: 17px;
            border-radius: 50px;
            cursor: pointer;
            text-align: center;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
            transition: background-color 0.3s ease;
        }
        .next-button:hover {
            background-color: #c2924d;
        }
        
    </style>
    """, unsafe_allow_html=True)

# Main layout container
with st.container():
# Close button on the right
    col1, col2 = st.columns([9, 1])
    with col2:
        st.markdown(
            "<div class='close-button'><button>✕</button></div>",
            unsafe_allow_html=True
        )
        
with col1:
    # Delivery title
    st.markdown("<h1>Delivery</h1>", unsafe_allow_html=True)
    
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
    
        st.divider()

    # Card 1: Quantity of Parcel
    st.subheader("Quantity of Parcel")
    quantity = st.radio("", ['1', '2', '3', 'Others:'])
    if quantity == 'Others:':
        other_quantity = st.text_input("Specify other quantity")
        
    # Line break
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Card 2: Earliest & Latest Parcel Arrival Dates
    st.subheader("Earliest & Latest Parcel Arrival Dates")
    earliest_date = st.date_input("Earliest Date")
    latest_date = st.date_input("Latest Date")
    
    # Line break
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Card 3: Tracking Number
    st.subheader("Tracking Number")
    st.write("Note: If you have a parcel that arrived today or is still 'out for delivery', please put it in the bracket")
    st.write("Example:\nSPXM09255252 (Out for Delivery)\nSPX12984933 (Today)")
    tracking_number = st.text_area("Enter your tracking number")

    # Line break
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Card 4: Fragile Parcel
    st.subheader("Fragile Parcel")
    fragile = st.radio("", ['Yes', 'No'])
    
    # Line break
    st.markdown("<br>", unsafe_allow_html=True)

    # Card 5: What Items are in Your Parcel
    st.subheader("What Items are in Your Parcel")
    items = st.text_input("Enter item details")


# Card 6: Parcel Categories, Weight and Price Details
st.markdown("<h3 class='card-subheader'>PARCEL CATEGORIES, WEIGHT AND PRICE DETAILS (PER PARCEL, EXC. CHARGED PR)</h3>", unsafe_allow_html=True)
st.markdown("<p class='card-text'>Parcel Hub categorizes and labels your parcels according to size and weight, starting with the smallest as 'K' and moving up to A, B, C, D, and finally E (>12kg).</p>", unsafe_allow_html=True)
st.markdown("<p class='card-text'>Please be assured that our team will re-confirm the categories for each parcel before delivering it to you.</p>", unsafe_allow_html=True)

# Multi-select dropdown box for categories
categories = st.multiselect("Select applicable categories:", ['K', 'A', 'B', 'C', 'D', 'E'])
