from PIL import Image
import cv2
import numpy as np
from fastapi import FastAPI, UploadFile
from .utils import classify_img,get_alzheimer_model

app=FastAPI(title="Alzheimer Detection API")

@app.get("/")
def display():
    return "Welcome to Alzheimer Detection Api"

@app.post("/predict")
def predict(file: UploadFile):
    img=Image.open(file.file)
    img=np.array(img)
    if len(img.shape)==2:
        img=cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)
    img=cv2.resize(img,(480,480))
    model= get_alzheimer_model()
    label,probability=classify_img(model,img)
    return {"label":label.item(),"probability":probability.item()}