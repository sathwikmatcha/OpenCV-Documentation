import numpy as np
import cv2 as cv
# you can draw rectangles,lines,circles and polygons over an image
# let image be img
# the arguemnts here are generally important and they are either co-ordinates relative to img origin standard or the dimensions
# of the shape drawn or the color of the shape


# Create a black image
'''
img = np.zeros((512, 512, 3), np.uint8)
'''
# arguments:
# img=>image
# x1,x2,y1,y2 => co-ordinates
# bgr=>bgr color
# t=>thickness

'''
x1=0
x2=0
y1=0
y2=0
b=234
g=234
r=234
t=5
'''
'''
cv.line(img, (x1, y1), (x2, y2), (b, g, r), t)
'''
'''
cv.rectangle(img,(x1,y1),(x2,y2),(b,g,r),t)
'''
'''
xc=100
yc=100
r=20
'''
# -1 fills the circle
'''
cv.circle(img, (xc, yc), r, (b, g, r), -1)
'''
# ellipse
# arguments
# img=>image
# center=>center of ellipse
# axes=>(1/2M,1.2m)
# angle=>angle of rotation
# start angle,end angle
# color
# thickness
'''
xc=100
yc=100
M=200
m=150
ar=45
sa=0
ea=180
b=234
g=234
r=234
t=-1
'''
'''
cv.ellipse(img, (xc,yc),(M,m),ar,sa,ea,(b,g,r),t)
'''
# Similarly we get polylines and adding text to images by poly lines and puttext method'''
# for polylines we just need to resize the coordinates in ROWSx1x2 formatted array using numpy
# with other arguments
'''
pts = np.array([[10,0],[20,30],[70,20],[50,50]], np.int32)
pts = pts.reshape((-1,1,2))
cv.polylines(img,[pts],True,(0,255,255))
'''
# text
# get a font and pass a string as an Argument along with other's like thickness
'''
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2, cv.LINE_AA)
'''
