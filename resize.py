# python code resize.py
# LR Mayer from OpenCV book (pdf)
# 08/23/2016
#
# Resize an image

import sys
sys.path.append(r'C:\Users\mdeeds\Documents\Mayer\NASA\CatalogImages\CatalogImages\Modules/')

import numpy as np
import argparse
import imutils  # importing my imutils
import cv2

ap = argparse.ArgumentParser()

ap.add_argument("-i", "--image", required = True,help = "Path to the image")

args = vars(ap.parse_args())

print "Name of original image is :  {} ".format(args["image"])

# use cv2.imread to read the original image
image = cv2.imread(args["image"])

# show the image
cv2.imshow("Original", image)

#----------------------------------------------------
# resize the image by specifying height
#----------------------------------------------------

# compute the aspect ratio. new image width to be 150
# pixels. In order to compute the ratio of the new height to
# the old height, we simply define our ratio r to be the new
# width (150 pixels) divided by the old width, image.shape[1]
# ratio = new width/old width
r = 150.0 / image.shape[1]

# new image dimensions = 150 width x old height * ratio
dim = (150, int(image.shape[0] * r))

# new resized image : old image, dimension, interpolation method for resizing
# From openCV book (pdf) : I find that using cv2.INTER_AREA obtains the best results when resizing; how-
# ever, other appropriate choices include cv2.INTER_LINEAR,
# cv2.INTER_CUBIC, and cv2.INTER_NEAREST.
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

# show the resized image
cv2.imshow("Resized (Width)", resized)

cv2.waitKey(0)

#----------------------------------------------------
# resize the image by specifying height
#----------------------------------------------------
r = 500.0 / image.shape[0]

dim = (int(image.shape[1] * r), 500)

resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

cv2.imshow("Resized (Height)", resized)

cv2.waitKey(0)

#----------------------------------------------
# resize using my imutils function resize :
#----------------------------------------------
# resized = imutils.resize(image, width = 1000)
#
# cv2.imshow("Resized with Function", resized)
#
# cv2.waitKey(0)
#
# # write the image to a jpg
# cv2.imwrite("SmallSnowBetty.jpg", resized)

# ---------------------------
# Convert to hsv color space
# ---------------------------
from hsvcolorblock import HSVCOLORBLOCK

# --------------------------------------
# Find the corners of the green image
# --------------------------------------
colorLower = np.array([8, 50, 90], dtype="uint8")  # if this gets > .1%, def is aurora
colorUpper = np.array([15, 200, 110], dtype="uint8")

# find the pixels in that color range
# Get the color blocked binary image
block = HSVCOLORBLOCK(resized, colorLower, colorUpper)

# Get the largest contour around the color block
cnt = block.get_largest_contour()

if cnt.any() :
    rect = np.int32(cv2.boxPoints(cv2.minAreaRect(cnt)))

    # draw the boundaries of the box
    # cv2.drawContours(resized, [rect], -1, (0, 255, 0), 2)
    # cv2.imshow("green", resized)

    print "There is some green "

    # determine the most extreme points along the contour
    # cnt[:, :, 0]   is all the x's in cnt
    extLeft = tuple(cnt[cnt[:, :, 0].argmin()][0])
    # extRight = tuple(cnt[cnt[:, :, 0].argmax()][0])
    # extTop = tuple(cnt[cnt[:, :, 1].argmin()][0])
    # extBot = tuple(cnt[cnt[:, :, 1].argmax()][0])

    #extLeft = cnt[:, :, 0].argmin()
    extRight = tuple(cnt[cnt[:, :, 0].argmax()][0])
    extTop = tuple(cnt[cnt[:, :, 1].argmin()][0])
    extBot = tuple(cnt[cnt[:, :, 1].argmax()][0])

    print "corners : {}{}{}{} ".format(extLeft, extRight, extTop, extBot)

    print cnt[0,0,0]
    print cnt[0, 0, 1]
    print cnt[0, 0, :]
    print cnt[1, 0, :]
    print cnt[2, 0, :]
    #print cnt[:, 0, 0]

    #print cnt[:, :, 0]

    #xxx = [1,3]


    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(resized, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow('rectangle', resized)

    cv2.waitKey(0)

    # Resize the map image
    mapName = r'C:\Users\mdeeds\Documents\Mayer\GIS\Boulder Maps/BoulderCity_v3_300dpi_11x14.jpg'
    # use cv2.imread to read the original image
    image = cv2.imread(mapName)
    dim = (w,h)
    print dim
    print x,y
    mapResized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

    cv2.imshow('Resized Map',mapResized)
    cv2.waitKey(0)

    print "x, x+h, y, y+h : {}{}{}{} ".format(x, x+h, y, y+h)

    resized[x:x+h, y:y+w] = mapResized

    cv2.imshow('pip', resized)

    cv2.waitKey(0)
