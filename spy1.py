import numpy as np
import cv2
import time
from picamera import PiCamera
from PIL import Image

camera = PiCamera()
time.sleep(2)

size = (1024,768)
camera.resolution = size
img = np.empty(size + (3,), dtype=np.uint8)
camera.capture(img, 'jpeg', use_video_port=True)
image = Image.fromarray(img)
image.save('image.jpeg')