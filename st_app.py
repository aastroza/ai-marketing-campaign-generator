import streamlit as st
import json
import requests

endpoint = "https://aastroza--example-fastapi-app-fastapi-app-dev.modal.run/campaign"

st.title("Marketing Campaign Generator 🔥")

# User Input

prompt = st.text_area("Enter your brand name and a short description of your brand. We will generate a marketing campaign for you 🚀.")

input = {"prompt": prompt}
if st.button("Generate"):
    res = requests.post(url=endpoint, data=json.dumps(input))
    res_json = res.json()
    st.subheader("Generated Campaign")
    st.markdown(res_json["campaign_text"])