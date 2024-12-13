##CODE SNIPPET FOR HEALTH MANAGEMENT APP INITIALIZATION
from dotenv import load_dotenv

load_dotenv()
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## FUNCTION TO LOAD GOOGLE GEMINI PRO  API AND GET RESPONSE

def get_gemini_response(input,image,prompt):
    model=genai.GenerativeModel('gemini-1.5-pro')
    response=model.generate_content([input,image[0],prompt])
    return response.text

## FUNCTION TO READ THE IMAGE

def input_image_setup(uploaded_file):

    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        return input
    
input_prompt="""You are an expert in nutrition where you need to read the input, and answer accordindly i.e analyse health goals ,provide insights and suggest meal plans based on the input. 
                Also you need to see the food items present in the image uploaded and determine the overall calories present and also the nutrition. Also determine the calorie and nutrion (i.e proteins,fats,carbohydrates,minerals,vitamins) of each food item present in the image and list them in below format:
                1.Item 1 - Calories and Nutrion
                2.Item 2 - Calories and Nutrion
                ----
                ----
                Also mention whether the food is healthy or unhealthy.
                and if there is no image provided, just read the input and answer accordingly."""

st.set_page_config(page_title= "Nutritionist AI")

st.header("AI Nutrionist")
input=st.text_input("Input:",key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""
if uploaded_file is not None:
    image= Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)


submit=st.button("Know it")
##If submit button is clicked
if submit:
    image_data=input_image_setup(uploaded_file)
    response=get_gemini_response(input_prompt,image_data,input)
    st.subheader("The Response is")
    st.write(response)
