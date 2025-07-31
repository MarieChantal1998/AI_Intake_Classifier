#FRONTEND

import streamlit as st                # Streamlit is our UI framework — it helps us build web apps fast, straight from Python.
from classifier import classify_intake # This is our backend function — it sends the message to OpenAI for classification.
import json                           # We use json to parse the AI's structured response.
import logging                        # We use logging to track usage and keep a basic audit trail of user inputs.

# This sets up the layout and page title of the app
st.set_page_config(page_title="AI Legal Intake Classifier", layout="centered")

# Add the app title and instructions
st.title("AI Legal Intake Classifier")
st.markdown("Paste your client's message below and get classification results:")

# Create a large input box for the user to paste their intake message
user_input = st.text_area("Client Intake Message", height=200)

# When the "Classify" button is clicked:
if st.button("Classify"):
    if user_input.strip() == "":
        # Show a warning if the user didn't type anything
        st.warning("Please enter a client intake message.")
    else:
        # Show a loading spinner while the AI processes the request
        with st.spinner("Classifying..."):
            response = classify_intake(user_input)
            
            try:
                # Try to parse the response as JSON
                result = json.loads(response)
                st.success("Classification Complete!")  # Display success message

                # Display the results in a clean format
                st.markdown("### Result Summary")
                st.markdown(f"**Case Type:** {result.get('case_type', 'N/A')}")
                st.markdown(f"**Urgency Level:** {result.get('urgency_level', 'N/A')}")
                st.markdown(f"**Status Recommendation:** {result.get('status_recommendation', 'N/A')}")
            except json.JSONDecodeError:
                # If parsing fails, show the raw response
                st.error("Could not parse response as JSON. Here’s what was returned:")
                st.code(response)

# Set up logging to track what users enter and what the AI returns
logging.basicConfig(filename='usage.log', level=logging.INFO)

# Log the input and output — this helps us track API usage later
logging.info(f"User submitted: {user_input}")
logging.info(f"Response: {result}")
