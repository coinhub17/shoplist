import streamlit as st
from pages.chat import contact_form


st.title(":green[PRICETAG - AI SHOPPING ASSISTANT]")
st.subheader(":orange[Compare prices of Electronics and Gadgets using AI to inquire more about their characteristics and specifications]", divider="green")
st.write("Welcome to Pricetag. AI Shopping Assistant! Here, you can compare prices of various electronics and gadgets. If you have any questions or need assistance, feel free to reach out to us using the contact form below.")


st.subheader("Refrigerator", divider="blue")
left, middle, right=st.columns(3)
with st.container():
    left.link_button(":blue Amazon Refrigerators", "https://streamlit.io/gallery",type="secondary", icon=None,use_container_width=False)
    middle.link_button(":blue ebay Refrigerators", "https://streamlit.io/gallery",type="secondary", icon=None,use_container_width=False)
    right.link_button(":blue ebay Refrigerators", "https://streamlit.io/gallery",type="secondary", icon=None,use_container_width=False)

st.subheader("Refrigerator", divider="blue")
left, middle, right=st.columns(3)
with st.container():
    left.link_button(":blue Amazon Refrigerators", "https://streamlit.io/gallery",type="secondary", icon=None,use_container_width=False)
    middle.link_button(":blue ebay Refrigerators", "https://streamlit.io/gallery",type="secondary", icon=None,use_container_width=False)
    right.link_button(":blue ebay Refrigerators", "https://streamlit.io/gallery",type="secondary", icon=None,use_container_width=False)

st.subheader("Refrigerator", divider="blue")
left, middle, right=st.columns(3)
with st.container():
    left.link_button(":blue Amazon Refrigerators", "https://streamlit.io/gallery",type="secondary", icon=None,use_container_width=False)
    middle.link_button(":blue ebay Refrigerators", "https://streamlit.io/gallery",type="secondary", icon=None,use_container_width=False)
    right.link_button(":blue ebay Refrigerators", "https://streamlit.io/gallery",type="secondary", icon=None,use_container_width=False)


"\n\n\n\n\n\n"



st.subheader(":blue[AFTER SHOPPING YOU CAN TRAVEL.]")

st.subheader(":green[TRAVEL PACKAGES]", divider="blue")
left, middle, right=st.columns(3)
with st.container():
    left.link_button(":blue[Option 1]", "https://hotellook.tp.st/SUR7llTq",type="secondary", icon=None,use_container_width=False)
    middle.link_button(":blue[Option 2]", "https://wayaway.tp.st/Kk6nVbjq",type="secondary", icon=None,use_container_width=False)

@st.dialog(title="Contact Us")
def show_form():
    contact_form()

if st.button("contact Us here",type="primary"):
    show_form()
