# pip install picamera2 pillow numpy argparse opencv-python
# curl -L https://raw.github.com/pageauc/picamera-motion/master/install.sh | bash

import argparse
import cv2
import datetime
import io
import sys
import time
import numpy as np
from picamera import PiCamera
from PIL import Image

start = datetime.datetime.now()

camera = PiCamera()
time.sleep(2)  # Allow the camera to warm-up

size = (1024,768)
size = (1280, 720)
size = (1920,1024)
camera.resolution = size
threshold = 0
format = 'yuv'
format = 'rgb'
ext = 'jpeg'

def run():
  global size
  if format == 'rgb':
    size = size + (3,)
  print(f"""
Format    = {format}
Extension = {ext}
Size      = {size}""")


  img0 = np.empty(size, dtype=np.uint8)
  img1 = np.empty(size, dtype=np.uint8)

  # Capture the first image
  buf = io.BytesIO()
  camera.capture(buf, 'jpeg')
  img0 = buf.getvalue()
  buf.seek(0)
  a0 = np.array(Image.open(buf))

  while True:
    #print('.', end='')
    #sys.stdout.flush()

    # Capture the image.
    buf = io.BytesIO()
    camera.capture(buf, 'jpeg')
    img1 = buf.getvalue()
    buf.seek(0)
    a1 = np.array(Image.open(buf))

    # Compare it to the previous image
    diff = np.mean(np.abs(a1 - a0)))
    print(diff, end='')
    motion = np.any(diff > threshold)

    if motion:
      ts = datetime.datetime.today().strftime("%Y%m%d%H%M%S")
      fn = f"/mnt/dell/spy/image_{ts}.{ext}"
      fn = f"image_{ts}.{ext}"
      print(f" --> {fn}")
      #img = img1[..., 0]  # Keep only the Y channel for grayscale
      img = img1
      with open(fn, 'wb') as f:
        f.write(img)
    else:
      print('')
    img0 = img1
    a0 = a1

  delta = datetime.datetime.now() - start
  seconds = delta.seconds + float(delta.microseconds)/1000000
  print(f"{seconds} seconds")

parser = argparse.ArgumentParser(
  prog='Spy',
  description='Watch a room for changes',
  epilog='By Robby')
parser.add_argument('-t', '--threshold', default=150)
args = parser.parse_args()
if args.threshold:
  threshold = float(args.threshold)

run()