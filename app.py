import streamlit as st
from classifier import classify_intake
import json
import logging

st.set_page_config(page_title="AI Legal Intake Classifier", layout="centered")

st.title("AI Legal Intake Classifier")
st.markdown("Paste your client's message below and get classification results:")

user_input = st.text_area("Client Intake Message", height=200)

if st.button("Classify"):
    if user_input.strip() == "":
        st.warning("Please enter a client intake message.")
    else:
        with st.spinner("Classifying..."):
            response = classify_intake(user_input)
            
            try:
                result = json.loads(response)
                st.success("Classification Complete!")
                st.markdown("### Result Summary")
                st.markdown(f"**Case Type:** {result.get('case_type', 'N/A')}")
                st.markdown(f"**Urgency Level:** {result.get('urgency_level', 'N/A')}")
                st.markdown(f"**Status Recommendation:** {result.get('status_recommendation', 'N/A')}")
            except json.JSONDecodeError:
                st.error("Could not parse response as JSON. Here’s what was returned:")
                st.code(response)

# Setup logging
logging.basicConfig(filename='usage.log', level=logging.INFO)

# Inside your classify_intake function or main code
logging.info(f"User submitted: {user_input}")
logging.info(f"Response: {result}")