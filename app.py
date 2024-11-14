import streamlit as st
from main import generate_response, genai_upload

st.set_page_config(page_title="SocialShelf")

st.header(":green[Social]:blue[Shelf]")
st.write("Generate Amazon product listings from Instagram Posts.")

image = st.file_uploader("Upload image")

if image:
    with open(f'uploads/{image.name}', "wb") as f:
        f.write(image.getbuffer())

caption = st.text_input("Enter caption")
generate = st.button("Generate")

if generate:
    response = generate_response(caption, f'/uploads/{image.name}')
    st.markdown(response)