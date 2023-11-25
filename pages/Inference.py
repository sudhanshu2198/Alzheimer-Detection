import streamlit as st
from PIL import Image
import cv2
import numpy as np
import os
import torch
import torchvision
from utils import classify_img,get_alzheimer_model

st.title("Dementia Stages Classification")

classes=['Mild_Demented', 'Moderate_Demented', 'Non_Demented', 'Very_Mild_Demented']
model=get_alzheimer_model()
model.eval()
dirname=os.path.dirname(os.path.abspath(__file__))
root_dir=os.path.join(dirname,os.pardir)
density_img_dir=os.path.join(root_dir,"images","alzheimer_img")

file=st.file_uploader("Input Image File",type = ['jpg','png','jpeg'])
button=st.button("Detect")
if button:
    if file is not None:
        title="Uploaded Image"
        img=Image.open(file)
        img=np.array(img)
        if len(img.shape)==2:
            img=cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)
        img=cv2.resize(img,(480,480))
        label,probability=classify_img(model,img)
    else:
        title="Default Image"
        idx=np.random.choice(range(10),1)[0]
        default_img_path=os.path.join(density_img_dir,f"{idx}.jpg")
        img=cv2.imread(default_img_path)
        if len(img.shape)==2:
            img=cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)
        img=cv2.resize(img,(480,480))
        label,probability=classify_img(model,img)

    if label==0 or label==3:
        st.warning(f"Predicted Class is {classes[label]} with probability {probability:.4f}")
    elif label==2:
        st.success(f"Predicted Class is {classes[label]} with probability {probability:.4f}")
    else:
        st.error(f"Predicted Class is {classes[label]} with probability {probability:.4f}")
    st.image(img)