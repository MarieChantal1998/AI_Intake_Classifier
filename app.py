import streamlit as st
from classifier import classify_intake

st.set_page_config(page_title="AI Legal Intake Classifier", layout="centered")

st.title("📄 AI Legal Intake Classifier")
st.markdown("Paste your client's message below and get classification results:")

user_input = st.text_area("Client Intake Message", height=200)

if st.button("Classify"):
    if user_input.strip() == "":
        st.warning("Please enter a client intake message.")
    else:
        with st.spinner("Classifying..."):
            result = classify_intake(user_input)
            st.subheader("🔍 Classification Result")
            st.code(result, language="json")