import cv2 as cv
# to caputure your videos from your camera use VideoCapture()

# additional arguments:

# filename->str=>name of file to be opened
# apiPreference->cv.CAP_ANY=>used for os specific preference
#

'''
cap = cv.VideoCapture()
'''
# to record videos use Videowriter with the necessary four_cc codec for example
# arguments:
# filename
# four_cc
# frame_rate
# size
'''
out=cv.VideoWriter()
'''
