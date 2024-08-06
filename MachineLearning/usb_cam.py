#!/usr/bin/env python

import cv2

cam_port = 0
cam = cv2.VideoCapture(cam_port)

result, image = cam.read()

if result:
    cv2.imshow("picture", image)

    cv2.imwrite("picture.png", image)
    cv2.waitKey(0)
    cv2.destroyWindow("picture")

else:
    print("No image detected. Please try again!")
