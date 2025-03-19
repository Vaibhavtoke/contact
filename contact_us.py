import streamlit as st
from streamlit_option_menu import option_menu
import requests

# Webhook URL
WEBHOOK_URL = "https://connect.pabbly.com/workflow/sendwebhookdata/IjU3NjYwNTY5MDYzMzA0MzE1MjY5NTUzZDUxMzci_pc"  # Replace with your actual webhook URL

# Function for the "Contact Us" tab
def contact_us():
    st.header(":mailbox: Get in touch with me!")
    
    # Form fields
    name = st.text_input("Your Name", "")
    email = st.text_input("Your Email", "")
    message = st.text_area("Your Message", "")
    
    if st.button("Send"):
        if name and email and message:
            payload = {
                "name": name,
                "email": email,
                "message": message
            }
            response = requests.post(WEBHOOK_URL, json=payload)
            
            if response.status_code == 200:
                st.success("Message sent successfully!")
            else:
                st.error("Failed to send message. Please try again later.")
        else:
            st.warning("Please fill in all fields before submitting.")

# Main function
def main():
    selected = option_menu(
        menu_title=None,  # required
        options=["Contact Us"],  # Only "Contact Us" tab
        icons=["envelope"],  # Icon for the tab
        menu_icon="cast",  # optional
        default_index=0,  # Set default selection
        orientation="horizontal"
    )

    if selected == "Contact Us":
        contact_us()

if __name__ == "__main__":
    main()