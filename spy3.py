import numpy as np
import cv2
import time
import io
from picamera import PiCamera
from PIL import Image

camera = PiCamera()
time.sleep(2)

size = (1920,1024)
camera.resolution = size

# Create a bytes buffer for the capture
buf = io.BytesIO()

# Capture into the bytes buffer
camera.capture(buf, 'jpeg', use_video_port=True)

# Get the byte value from the buffer
byte_value = buf.getvalue()

# Write the byte value to the disk
with open('spy3.jpeg', 'wb') as f:
    f.write(byte_value)
