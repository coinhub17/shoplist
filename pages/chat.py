import streamlit as st
import requests
import re

# Pabbly Webhook URL (replace with your actual webhook URL from Pabbly)
PABBLY_WEBHOOK_URL =st.secrets["WEBHOOK"]

EMAIL_REGEX = r"[^@]+@[^@]+\.[^@]+"

def validate_input(name, email, message):
    errors = []
    
    if not name.strip() or not name.replace(" ", "").isalpha():
        errors.append("Please enter a valid name (letters only).")
        
    if not re.match(EMAIL_REGEX, email):
        errors.append("Please enter a valid email address.")
    
    if not message.strip() or len(message.strip()) < 2:
        errors.append("Message must be at least 2 characters long.")
        
    return errors

def contact_form():
    with st.form("contact_form"):
    # Collect user input
        name = st.text_input("Name", placeholder="Enter your full name")
        email = st.text_input("Email", placeholder="Enter your email address")
        message = st.text_area("Message", placeholder="Enter your message here", height=200)
        submit_button=st.form_submit_button("SUBMIT")


# When the "Send Message" button is clicked
        if submit_button:
            validation_errors = validate_input(name, email, message)

            if validation_errors:
                for error in validation_errors:
                    st.warning(error)
            if name and email and message:
                # Data to send to Pabbly
                data = {
                    "name": name,
                    "email": email,
                    "message": message
                }

                # Send a POST request to Pabbly webhook
                response = requests.post(PABBLY_WEBHOOK_URL, data=data)

                # Check if the request was successful
                if response.status_code == 200:
                    st.success("Your message has been sent successfully!")
                else:
                    st.error("Failed to send your message. Please try again later.")
            else:
                st.warning("Please fill out all fields before sending the message.")

