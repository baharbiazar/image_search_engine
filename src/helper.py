import os
import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.models import Model
from pathlib import Path


import requests
from io import BytesIO

import PIL
from PIL import Image, ImageFilter

import os
import pickle



class FeatureExtractor:
    def __init__(self):
        # Use VGG-16 as the architecture and ImageNet for the weight
        base_model = VGG16(weights='imagenet')
        # Customize the model to return features from fully-connected layer
        self.model = Model(inputs=base_model.input, outputs=base_model.get_layer('fc1').output)
    
    def extract(self, img):
        # Resize the image
        img = img.resize((224, 224))
        # Convert the image color space
        img = img.convert('RGB')
        # Reformat the image
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        # Extract Features
        feature = self.model.predict(x)[0]
        return feature / np.linalg.norm(feature)


def search(query_path):

    fe = FeatureExtractor()

    # Insert the image query
    img = Image.open(query_path)
    # Extract its features
    query = fe.extract(img)
    # Calculate the similarity (distance) between images
    dists = np.linalg.norm(array_reloaded - query, axis=1)
    # Extract 30 images that have lowest distance
    ids = np.argsort(dists)[:30]
    scores = [(dists[id], image_paths[id][1]) for id in ids]
    # Visualize the result
    axes=[]
    fig=plt.figure(figsize=(8,8))
    for a in range(5*6):
        score = scores[a]
        axes.append(fig.add_subplot(5, 6, a+1))
        subplot_title=str(score[0])
        axes[-1].set_title(subplot_title)  
        plt.axis('off')
        plt.imshow(Image.open(score[1]))
    fig.tight_layout()
    plt.show()
    




if __name__ == '__main__':

    array_reloaded = np.load('model/alloffeatnumpy.npy')
    
    with open("model/image_paths.txt", "rb") as fp: # Unpickling
        image_paths = pickle.load(fp)

    print(image_paths)


    query_path = '/Users/bahar/Desktop/search/22.png'
    search(query_path)