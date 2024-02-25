import numpy as np
import cv2
import time
from picamera import PiCamera
from PIL import Image

camera = PiCamera()
time.sleep(2)

size = (1024,768)
camera.resolution = size
camera.capture('spy2.jpeg', 'jpeg', use_video_port=True)
