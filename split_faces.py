"""
Use another face splitting technique.
This was not generating the photos as expected.
Faces were blue.
"""

import time
import os
import os.path
import glob
from pathlib import Path
from PIL import Image

import cv2
import face_recognition
from sklearn.cluster import DBSCAN




folder = r"I:\Photos"
faces_folder = r"I:\Photos\faces1"




def split_faces():
  extensions = ('jpg', 'jpeg', 'gif', 'png')
  start = False
  i = 0
  for path in Path(folder).rglob('*'):
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

    # Skip old photos
    t = os.path.getmtime(filename)
    if time.localtime(t).tm_year < 2020: continue

    print(f"{i:>6}: {filename}: {time.localtime(t).tm_year}")
    img = face_recognition.load_image_file(filename)
    face_locations = face_recognition.face_locations(img)
    for i,(x, y, w, h) in enumerate(face_locations):
      fn = filename.replace(folder, '').replace('\\', '_')[1:]
      outfile = os.path.join(faces_folder, fn.replace('.', f"_{i}."))
      pil_image = Image.fromarray(img)
      crop = pil_image.crop((x, y, x+w, y+h))
      cv2.imwrite(outfile, crop)


split_faces()

'''
# Load images
image_files = ['image1.jpg', 'image2.jpg', 'image3.jpg']
images = [face_recognition.load_image_file(file) for file in image_files]

face_encodings = []
for image in images:
  image = face_recognition.load_image_file(file)
  face_locations = face_recognition.face_locations(image)
  encodings = face_recognition.face_encodings(image, face_locations)
  face_encodings.extend(encodings)

# Use DBSCAN to cluster face embeddings
clt = DBSCAN(metric="euclidean")
clt.fit(face_encodings)

# Print cluster labels for each face
for i, label in enumerate(clt.labels_):
    print(f"Face {i+1} is in cluster {label+1}")
'''