import os
import numpy as np
import torch
import torch.nn as nn
import torchvision
import torchvision.transforms.functional as tf
from torchvision.models import efficientnet_b0
import streamlit as st

root_dir=os.path.dirname(os.path.abspath(__file__))
weights_dir=os.path.join(root_dir,"weights")

def classify_img(model,img):
    img=tf.to_tensor(img)
    img=img.unsqueeze(0)
    with torch.no_grad():
        predict=model(img)
        predict=nn.functional.softmax(predict,1)
        label=torch.argmax(predict)
        probability=torch.max(predict)
        return label,probability

@st.cache_resource
def get_alzheimer_model():
    model=efficientnet_b0(weights=None)
    in_features=model.classifier[1].in_features
    model.classifier[1]=nn.Linear(in_features=in_features,out_features=4)
    weights_path=os.path.join(weights_dir,"alzheimer_weight.pth")
    weights=torch.load(weights_path,map_location="cpu")
    model.load_state_dict(weights)
    return model
