# -*- coding: utf-8 -*-
"""Invoice Extractor Using Google Gemini

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15HdK0sLUfB1Ph996Z7I-Nr8KPJ9vujoR
"""

API_KEY='AIzaSyAyGrTbjkU6cGEVSOZB5z4E044GuNY4Z-Q'

import pathlib
import textwrap

import google.generativeai as genai


genai.configure(api_key=API_KEY)

# For text generation from input

model =genai.GenerativeModel('gemini-1.5-flash')

# Commented out IPython magic to ensure Python compatibility.
# %%time
# response = model.generate_content("What is the meaning of life?")





model=genai.GenerativeModel('gemini-1.5-flash')


# Commented out IPython magic to ensure Python compatibility.


import streamlit as st
import google.generativeai as genai
from PIL import Image
# 
API_KEY='AIzaSyAyGrTbjkU6cGEVSOZB5z4E044GuNY4Z-Q'
genai.configure(api_key=API_KEY)
# 
model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat(history=[])
# 
# 
def get_gemini_response(input,image,prompt):
#   #Loading the Gemini Model
# 
    model=genai.GenerativeModel('gemini-1.5-flash')
    response=model.generate_content([input,image[0],prompt])
    return response.text

# 
def input_image_setup(uploaded_file):
    
    if uploaded_file is not None:
     # Read the file into bytes
     bytes_data =uploaded_file.getvalue()
    
     image_parts =[
         {
             "mime_type": uploaded_file.type,
             "data": bytes_data
         }
     ]
     return image_parts
    else :
     raise FileNotFoundError("No file uploaded")

 
st.set_page_config(page_title="invoice Extractor")
 
 # Building the streamlit application
# 
st.header("Top G Invoice Extractor 🧾")

uploaded_file=st.file_uploader("choose an image...",type=["jpg","jpeg","png"])
# 
image=""
if uploaded_file is not None:

    image=Image.open(uploaded_file)
    st.image(image,caption="uploaded Image.",use_column_width=True)
# 
input=st.text_input("input prompt: ",key="input")
submit=st.button("Tell me about the invoice")
# 
input_prompt="""
You are an expert in understanding invoices. You wil
receive input images as invoices and you will hae to
answer questions based on the input image
"""
# 
if submit:
    
    image_data=input_image_setup(uploaded_file)
    response=get_gemini_response(input_prompt,image_data,input)
    
    st.subheader("The Response is")
    st.write(response)

 
# 
# 
# 
# 
# 
# 
# 
# 
# 
#


