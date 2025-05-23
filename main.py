import streamlit as st
from pages.chat import contact_form

# Set wide layout and a vibrant page title
st.set_page_config(page_title="PRICETAG - AI Shopping Assistant", layout="wide")

# Custom HTML for colorful gradient title
st.markdown("""
    <style>
        .main-title {
            font-size: 3em;
            font-weight: 700;
            background: linear-gradient(90deg, #00c6ff, #0072ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
            margin-bottom: 0.5em;
        }
        .subtitle {
            font-size: 1.3em;
            color: #ff7f50;
            text-align: center;
            font-weight: bold;
            margin-bottom: 1em;
        }
        .description {
            text-align: center;
            color: #444;
            font-size: 1.1em;
            margin-bottom: 2em;
        }
        .stButton>button {
            background: linear-gradient(to right, #6a11cb, #2575fc);
            color: white;
            font-weight: bold;
            border-radius: 8px;
            padding: 0.5em 1.2em;
            font-size: 1.1em;
        }
    </style>
    <div class="main-title">PRICETAG - AI SHOPPING ASSISTANT</div>
    <div class="subtitle">Compare prices of Electronics and Gadgets using AI</div>
    <div class="description">
        Welcome to <strong>Pricetag</strong>, your AI-powered shopping assistant. <br/>
        Compare prices, explore deals, and inquire about product specs. <br/>
        Got questions? Reach out using the contact form below!
    </div>
""", unsafe_allow_html=True)
# Reusable function to show product section with icons or thumbnails
def product_section(title, links):
    with st.container():
        st.markdown(f"### :blue[{title}]")
        cols = st.columns(3)
        for col, (label, url) in zip(cols, links):
            with col:
                st.link_button(f":blue[{label}]", url, type="secondary", use_container_width=True)

# Electronics section
product_section("Refrigerators", [
    ("Amazon Refrigerators", "https://amazon.com/Refrigerators"),
    ("eBay Refrigerators", "https://ebay.com/Refrigerators"),
    ("BestBuy Refrigerators", "https://bestbuy.com/Refrigerators")
])

product_section("Laptops", [
    ("Amazon Laptops", "https://amazon.com/laptops"),
    ("eBay Laptops", "https://ebay.com/laptops"),
    ("Newegg Laptops", "https://newegg.com/laptops")
])

product_section("Smartphones", [
    ("Amazon Phones", "https://amazon.com/Smartphones"),
    ("eBay Phones", "https://ebay.com/Smartphones"),
    ("BestBuy Phones", "https://bestbuy.com/Smartphones")
])

st.divider()

# Travel Section
st.subheader(":blue[AFTER SHOPPING, EXPLORE TRAVEL DEALS!]")
st.subheader(":green[TRAVEL PACKAGES]", divider="blue")
product_section("Vacation Packages", [
    ("Expedia Deals", "https://expedia.com"),
    ("Booking.com Offers", "https://booking.com"),
    ("Airbnb Stays", "https://airbnb.com")
])

# Contact Form
@st.dialog(title="Contact Us")
def show_form():
    contact_form()

if st.button("📩 Contact Us Here", type="primary"):
    show_form()
