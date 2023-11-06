import streamlit as st
import requests

URL = "http://localhost:8000/generate"


def send_client_request():
    params = {"prompt": test_text}
    response = requests.get(url=URL, params=params)
    return response.json()


st.title("Testing content generation")

st.markdown("***")
st.markdown(
    """ 
    ### Sending a test request
    """
)

st.text("\n")
test_text = st.text_input("Prompt", value="How old are you?")
st.text("\n")

if st.button("Generate"):
    with st.spinner(text='In progress'):
        response_json = send_client_request()

        result = response_json.get("result")

        st.success(f" Response: {result}.")
