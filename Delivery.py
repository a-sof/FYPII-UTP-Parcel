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
        h1, h2, h3, h4, h5, h6, p, label, span {
            color: #000000 !important;
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
