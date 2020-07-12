import cv2 as cv
import sys
# cv.imread()--> can be used to create a read_image object,which can be later made to be shown

# ARGS: ( STRING filepathname ,[CONSTANTS])

# CONSTANTS=

# cv.IMREAD_GRAYSCALE SHOWS a grayscale image
# cv.IMREAD_COLOR shows a color image(default)
# cv.IMREAD_UNCHANGED shows a unchanged image.
'''
read_img_obj = cv.imread("lenna.png", cv.IMREAD_GRAYSCALE)
'''
# imshow(STRING displaytitle,read object)
# shows the image by creating awindow with the title
'''
cv.imshow("lenna image", read_img_obj)
'''
# 0 args mean to wait at this stage for erternity for future action unless,
'''
k = cv.waitKey(0)
'''

# if value in k is other than zero the function waits for that many milliseconds, for example for 1=>1ms

# you add an action

# cv.imwrite(STRING filepathname, read object)
# this fution just frickin saves the new created image for you.
'''
if(k == ord("s")):
    cv.imwrite("jiagio.png", read_img_obj)
'''
