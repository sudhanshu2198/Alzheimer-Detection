import numpy as np
import torch
import torch.nn as nn
import torchvision
import os
from torchvision.models import efficientnet_b0
import torchvision.transforms.functional as tf

root_dir=os.path.dirname(os.path.abspath(__file__))
weights_pth=os.path.join(root_dir,"alzheimer_weight.pth")

def classify_img(model,img):
    img=tf.to_tensor(img)
    img=img.unsqueeze(0)
    with torch.no_grad():
        predict=model(img)
        predict=nn.functional.softmax(predict,1)
        label=torch.argmax(predict)
        probability=torch.max(predict)
        return label,probability

def get_alzheimer_model():
    model=efficientnet_b0(weights=None)
    in_features=model.classifier[1].in_features
    model.classifier[1]=nn.Linear(in_features=in_features,out_features=4)
    weights=torch.load(weights_pth,map_location="cpu")
    model.load_state_dict(weights)
    model.eval()
    return model