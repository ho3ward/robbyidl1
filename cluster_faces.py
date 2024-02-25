"""
"""

import time
import os
import os.path
import glob
import numpy as np
from pathlib import Path
from PIL import Image

import cv2
import face_recognition
from sklearn.cluster import DBSCAN




faces_folder = r"I:\Photos\faces"




def cluster_faces():
  extensions = ('jpg', 'jpeg', 'gif', 'png')
  start = False
  images = []
  filenames = []
  encodings  = []

  i = 0
  iLoaded = 0
  for path in Path(faces_folder).rglob('*'):
    # Skip all but files
    if not os.path.isfile(path): continue

    # Skip all but files with desired extensions
    if not path.suffix[1:].lower() in extensions: continue

    i += 1
    filename = str(path)

    if not start:
      #if r'2020-11-19\IMG_6438.JPG' in filename:
      if True:
        start = True
      else:
        continue

    print(f"{i:>6}: {filename}")
    iLoaded += 1
    if iLoaded > 100: break

    filenames.append(filename)
    img = face_recognition.load_image_file(filename)
    encoding = face_recognition.face_encodings(img)
    encodings.append(encoding)

  # Use DBSCAN to cluster face embeddings
  clt = DBSCAN(metric="euclidean")
  clt.fit(encodings)

  # Print cluster labels for each face
  for i, label in enumerate(clt.labels_):
      print(f"Face {i+1} is in cluster {label+1}")

    #cv2.imwrite(outfile, crop)


cluster_faces()
