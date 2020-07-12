# one can explicitly call events for something to happen
# you just have to set a MouseCallback

import numpy as np
import cv2 as cv
# setMouseCallback
# arguments
# namedWindow->str=>name of the window
# functions->function
'''
img = np.zeros((512, 512, 3), np.uint8)
cv.namedWindow('image')


def click(event):
    if(event == cv.EVENT_LBUTTONDOWN):
        print("left button down")

cv.setMouseCallback("image", click)

'''
# to create a trackbar, use cv.createTrackbar()
# arguments:
# trackbar name->str
# window name->str
# optional arguments
# value ->int->position of slider
# count->max value
# onChange->bool=>helps us to chage thevalue upon
# userdata->?
'''
cv.createTrackbar()
'''
# to get the position of the trackbar, use get trackbar pos
# arguments:
# trackbarname->str=>name of trackbar
# winname->str=>name of window
'''
cv.getTrackbarPos()
'''
