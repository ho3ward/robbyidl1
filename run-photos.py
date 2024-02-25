'''
Read all the image files from "folder".
Pull out all the faces
'''
import time
import os
import os.path
import glob
from pathlib import Path
from PIL import Image

import cv2



folder = r"I:\Photos"
faces_folder = r"I:\Photos\faces1"




haarfile = 'haarcascade_frontalface_alt2.xml'
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + haarfile)


def display(img):
  # Resize the image
  img1 = img
  max = 256
  x = img.shape[0]
  y = img.shape[1]
  if x > max or y > max:
    if x > max:
      s = max/x
      width = max
      height = int(y * s)
    else:
      s = max/y
      height = max
      width = int(x * s)



    dim = (width, height)
    img1 = cv2.resize(img, dim)

    # Display the result
    cv2.imshow('Face Detection', img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



def process(filename):
  # Read the input image
  img = cv2.imread(filename)

  # Convert the image to grayscale
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

  # Perform face detection
  faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4, minSize=(20, 20))

  # Draw rectangles around the detected faces
  for i,(x, y, w, h) in enumerate(faces):
      fn = filename.replace(folder, '').replace('\\', '_')[1:]
      outfile = os.path.join(faces_folder, fn.replace('.', f"_{i}."))

      crop = img[y:y+h, x:x+w]

      max = 256
      x = crop.shape[0]
      y = crop.shape[1]
      if x > max or y > max:
        if x > max:
          s = max/x
          width = max
          height = int(y * s)
        else:
          s = max/y
          height = max
          width = int(x * s)
        crop = crop.resize((width, height))

      cv2.imwrite(outfile, crop)
      #cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

  # display(filename)



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
    if r'2020-11-19\IMG_6438.JPG' in filename:
      start = True
    else:
      continue

  # Skip old photos
  t = os.path.getmtime(filename)
  if time.localtime(t).tm_year < 2020: continue

  print(f"{i:>6}: {filename}: {time.localtime(t).tm_year}")
  try:
    process(filename)
  except Exception as e:
    print(e)

