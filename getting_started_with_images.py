import cv2 as cv
import sys
# cv.imread()--> can be used to create a read_image object,which can be later made to be shown

# ARGS: ( STRING filepathname ,[CONSTANTS])

# CONSTANTS=

# IMREAD_GRAYSCALE SHOWS a grayscale image
# IMREAD_COLOR shows a color image(default)
# IMREAD_UNCHANGED shows a unchanged image.

read_img_obj = cv.imread("lenna.png", cv.IMREAD_GRAYSCALE)

# imshow(STRING displaytitle,read object)
# shows the image by creating awindow with the title

cv.imshow("lenna image", read_img_obj)

# 0 args mean to wait at this stage for erternity for future action unless,

k = cv.waitKey(0)

# you add an action

# cv.imwrite(STRING filepathname, read object)
# this fution just frickin saves the new created image for you.

if(k == ord("s")):
    cv.imwrite("jiagio.png", read_img_obj)
