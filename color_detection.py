import numpy as np
import cv2

def detect_color(hsv_frame, lower, upper):
    color_mask = cv2.inRange(hsv_frame, lower, upper)
    color_mask = cv2.dilate(color_mask, None)
    return color_mask
