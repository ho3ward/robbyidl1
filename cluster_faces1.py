import numpy as np
from pathlib import Path
from PIL import Image
from sklearn.cluster import DBSCAN

images = []

def load_image(filename):
  img = Image.open(filename)
  img = img.resize((64, 64))
  img_array = np.array(img).flatten()
  images.append(img_array)

load_image('image1.jpg')
load_image('image1.jpg')
load_image('image2.jpg')

clt = DBSCAN(eps=0.5, min_samples=5, metric="euclidean")
clt.fit(images)

for i, label in enumerate(clt.labels_):
    print(f"Face {i+1} is in cluster {label+1}")

