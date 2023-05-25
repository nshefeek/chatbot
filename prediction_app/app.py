import requests
from logging import getLogger

import streamlit as st
from streamlit_tags import st_tags

from choices import processed_choices


log = getLogger("logger")

# Define the title
st.title("Disease Prediction Model")
st.write(
    "The model predicts possible diseases based on the symptoms you input.\
    Pass upto five symptoms below."
)

# Input 1
symptom1 = st.text_input(
    "Enter",
    processed_choices
)

# Input 2
symptom2 = st.selectbox(
    "Secondary Symptom",
    processed_choices
)

# Input 3
symptom3 = st.selectbox(
    "Other symptom 3",
    processed_choices
)

# Input 4
symptom4 = st.selectbox(
    "Other symptom 4",
    processed_choices
)

# Input 5
symptom5 = st.selectbox(
    "Other symptom 5",
    processed_choices
)


# When 'Submit' is selected
if st.button("Submit"):

    # Inputs to ML model
    inputs =[
            symptom1,
            symptom2,
            symptom3,
            symptom4,
            symptom5,
        ]
    print(inputs)
    # Posting inputs to ML API
    response = requests.post(f"http://prediction_api:8001/api/v1/predict/", json=inputs, verify=False)
    json_response = response.json()

    prediction = json_response.get("predictions")

    st.subheader(f"**{prediction}!**")