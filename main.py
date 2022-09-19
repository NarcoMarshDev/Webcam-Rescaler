import cv2
import pyvirtualcam
import numpy as np
import cvlib as cv

# always x_pos, y_pos, width, height
camPosition = []
with open("config.ini", "r") as file:
    for line in file:
        arr = line.split("=")
        camPosition.append(arr[1])

video = cv2.VideoCapture(0)

x = int(camPosition[0])
y = int(camPosition[1])
w = int(camPosition[2])
h = int(camPosition[3])

fmt = pyvirtualcam.PixelFormat.BGR
with pyvirtualcam.Camera(width=w, height=h, fps=60, fmt=fmt) as cam:
    print(f'Using virtual camera: {cam.device}')
    while True:
        ret, frame = video.read()

        croppedFrame = frame[y:y+h, x:x+w]

        cam.send(croppedFrame)
        cam.sleep_until_next_frame()
