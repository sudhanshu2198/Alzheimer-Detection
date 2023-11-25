import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import image
from PIL import Image
import os

st.title("Alzheimer's Detection")
st.subheader("The main goal of this is to classify brain scans into different stages of Dementia")


root_dir=os.path.dirname(os.path.abspath(__file__))
img_pth=os.path.join(root_dir,"images","intro_img.jpeg")
img=Image.open(img_pth)
st.image(img)

st.write("Alzheimer's disease is a brain disorder that gets worse over time. It's characterized by changes in the brain \
          that lead to deposits of certain proteins. Alzheimer's disease causes the brain to shrink and brain cells to \
          eventually die. Alzheimer's disease is the most common cause of dementia — a gradual decline in memory, \
          thinking, behavior and social skills. These changes affect a person's ability to function.")
st.write("People with Alzheimer's disease may:")
st.markdown("""
            - Repeat statements and questions over and over.
            - Forget conversations, appointments or events.
            - Misplace items, often putting them in places that don't make sense.
            - Have trouble finding the right words for objects, expressing thoughts or taking part in conversations.""")

col1,col2=st.columns(2)
with col1:
    st.write("[Github Link](https://github.com/sudhanshu2198/Alzheimer-Detection)")
with col2:
    st.write("[Kaggle Notebook](https://www.kaggle.com/code/sudhanshu2198/alzheimer-s-detection/notebook)")
