import streamlit as st
import requests

summarize_url = "http://127.0.0.1:8000/summarize"
tone_detection_url = "http://127.0.0.1:8000/tone_detect"
reply_generation_url = "http://127.0.0.1:8000/reply_generation"


st.title("AI-powered Email Assistant")
st.markdown("Enter Your Email : ")

text = st.text_area("Text")


option = st.selectbox("Choose output", ["Summarize", "Detect tone", "Generate Reply"])

if st.button("Check Output"):
    input_data = {
      "text" : text
    }


    with st.spinner("Processing... Please wait ⏳"):
         
        if option == "Summarize":
            response = requests.post(summarize_url,json = input_data)                  
          
        elif option == "Detect tone":
            response = requests.post(tone_detection_url,json = input_data)
             
        else: 
            response = requests.post(reply_generation_url,json = input_data)
          

    if response.status_code == 200:
        result = response.json()
        st.success(f"Output: {result}")
    else:
        st.error(f"Error: {response.status_code}")
